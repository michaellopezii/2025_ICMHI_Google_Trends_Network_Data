import os
import glob
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Call all tags for the name of each keyword
tags = [
    "flu",
    "cough",
    "fever",
    "headache",
    "lagnat",
    "rashes",
    "sipon",
    "ubo",
    "ecq",
    "face-shield",
    "Frontliners",
    "masks",
    "Quarantine",
    "social-distancing",
    "work-from-home",
]

pd.set_option('display.max_columns', None)
print(f'{tags}')

def get_next_filename(date_str):
    # Convert date string to next day's filename format
    
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    next_date = date_obj + timedelta(days=1)
    return next_date.strftime('%Y %m %d')

# Create necessary directories
os.makedirs('./gt_rsv_daily_raw_stitched', exist_ok=True)
os.makedirs('./gt_weekly_weight', exist_ok=True)

# Process each tag for daily stitched data
for tag in tags:
    print(f"Processing tag: {tag}")
    
    # Get the directory path for this tag
    tag_dir = f"../../gt_raw_daily30daywindow_volumes/{tag}"
    csv_files = glob.glob(os.path.join(tag_dir, "*.csv"))
        
    # Find earliest date file
    earliest_file = min(csv_files, key=lambda x: datetime.strptime(os.path.basename(x).replace('.csv', ''), '%Y %m %d'))
    
    # Initialize stitched data
    stitched_data = pd.DataFrame()
    current_file = earliest_file
    
    while current_file in csv_files:
        # Read and process current CSV
        df = pd.read_csv(current_file)
        if 'isPartial' in df.columns:
            df = df.drop('isPartial', axis=1)
        
        df['date'] = pd.to_datetime(df['date'])
        stitched_data = pd.concat([stitched_data, df], ignore_index=True)
        
        # Get next file
        last_date = df['date'].max().strftime('%Y-%m-%d')
        next_filename = os.path.join(tag_dir, f"{get_next_filename(last_date)}.csv")
        
        if not os.path.exists(next_filename) or \
           (stitched_data['date'].max() - stitched_data['date'].min()).days >= 365:
            break
            
        current_file = next_filename
    
    # Sort and save
    stitched_data = stitched_data.sort_values('date')
    output_file = f"./gt_rsv_daily_raw_stitched/{tag}_rsv_daily_raw_stitched.csv"
    stitched_data.to_csv(output_file, index=False)
    
    print(f"Completed daily stitching for {tag}")
    print(f"Total days: {len(stitched_data)}")
    print(f"Date range: {stitched_data['date'].min()} to {stitched_data['date'].max()}\n")

# Process each tag for weekly weights
for tag in tags:
    print(f"Processing tag: {tag}")
    
    # Read data
    weekly_raw_path = f"./gt_rsv_weekly_raw_volumes/{tag}_weekly_raw.csv"
    daily_path = f"./gt_rsv_daily_raw_stitched/{tag}_rsv_daily_raw_stitched.csv"
    
    weekly_df = pd.read_csv(weekly_raw_path)
    daily_df = pd.read_csv(daily_path)
    
    # Convert dates and tag name
    weekly_df['week'] = pd.to_datetime(weekly_df['week'])
    daily_df['date'] = pd.to_datetime(daily_df['date'])
    tag_col_name = tag.replace('-', ' ')
    
    # Initialize output
    output_df = pd.DataFrame({'week': weekly_df['week']})
    output_df[tag_col_name] = weekly_df[tag_col_name]
    
    # Calculate weekly metrics
    metrics = []
    for week_start in output_df['week']:
        next_week = week_start + pd.Timedelta(weeks=1)
        week_data = daily_df[
            (daily_df['date'] >= week_start) & 
            (daily_df['date'] < next_week)
        ][tag_col_name]
        
        weekly_sum = week_data.sum()
        days_count = len(week_data)
        weekly_avg = weekly_sum / days_count if days_count > 0 else 0
        metrics.append({'sum': weekly_sum, 'avg': weekly_avg, 'days': days_count})
    
    # Add metrics to output
    output_df['manual_weekly_average'] = [m['avg'] for m in metrics]
    output_df['manual_weekly_sum'] = [m['sum'] for m in metrics]
    output_df['days_in_week'] = [m['days'] for m in metrics]
    
    # Calculate weight and handle infinities
    output_df['search_interest_weight'] = output_df[tag_col_name] / output_df['manual_weekly_average']
    output_df['search_interest_weight'] = output_df['search_interest_weight'].replace([np.inf, -np.inf], np.nan) # To avoid any divisions against 0
    
    # Save output
    output_path = f"./gt_weekly_weight/{tag}_weekly_search_weight.csv"
    output_df.to_csv(output_path, index=False)
    
    print(f"Completed weekly processing for {tag}")
    print(f"Weeks processed: {len(output_df)}\n")

# Process each tag for final stitched RSV
cutoff_date = pd.to_datetime('2021-03-16')

for tag in tags:
    print(f"Processing tag: {tag}")
    
    # Read data
    daily_path = f"./gt_rsv_daily_raw_stitched/{tag}_rsv_daily_raw_stitched.csv"
    weekly_path = f"./gt_weekly_weight/{tag}_weekly_search_weight.csv"
    
    daily_df = pd.read_csv(daily_path)
    weekly_df = pd.read_csv(weekly_path)
    
    # Convert dates and filter
    daily_df['date'] = pd.to_datetime(daily_df['date'])
    weekly_df['week'] = pd.to_datetime(weekly_df['week'])
    daily_df = daily_df[daily_df['date'] <= cutoff_date]
    
    # Setup output dataframe
    tag_col_name = tag.replace('-', ' ')
    output_df = daily_df[['date', tag_col_name]].copy()
    output_df['search_interest_weight'] = None
    
    # Map weekly weights to daily dates
    for _, row in weekly_df.iterrows():
        week_start = row['week']
        week_end = week_start + pd.Timedelta(weeks=1)
        mask = (output_df['date'] >= week_start) & (output_df['date'] < week_end)
        output_df.loc[mask, 'search_interest_weight'] = row['search_interest_weight']
    
    # Calculate rescaled and normalized values
    output_df['rescaled_rsv'] = output_df.apply(
        lambda row: row[tag_col_name] if pd.isna(row['search_interest_weight']) or row['search_interest_weight'] == 0
        else row[tag_col_name] * row['search_interest_weight'],
        axis=1
    )
    
    max_rescaled = output_df['rescaled_rsv'].max()
    output_df['normalized_rescaled_rsv'] = (output_df['rescaled_rsv'] / max_rescaled * 100) if max_rescaled != 0 else 0
    
    # Save output
    output_path = f"./{tag}_rsv_stitched.csv"
    output_df.to_csv(output_path, index=False)
    
    print(f"Completed final processing for {tag}")
    print(f"Date range: {output_df['date'].min()} to {output_df['date'].max()}")
    print(f"Days processed: {len(output_df)}\n")
