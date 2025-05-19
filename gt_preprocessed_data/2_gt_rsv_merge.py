import pandas as pd

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

# Initialize empty DataFrames with date as index
merged_rescaled = pd.DataFrame()
merged_normalized = pd.DataFrame()

for tag in tags:
    # Read the stitched RSV file
    df = pd.read_csv(f"./{tag}_rsv_stitched.csv")
    df['date'] = pd.to_datetime(df['date'])
    
    # Format tag name (replace dashes with spaces)
    tag_name = tag.replace('-', ' ')
    
    # Add columns to respective DataFrames
    if merged_rescaled.empty:
        merged_rescaled['date'] = df['date']
        merged_normalized['date'] = df['date']
    
    # Add the rescaled and normalized columns with proper names
    merged_rescaled[f'{tag_name}'] = df['rescaled_rsv']
    merged_normalized[f'{tag_name}'] = df['normalized_rescaled_rsv']

# Save the merged files
merged_rescaled.to_csv('3_gt_rescaled_rsv.csv', index=False)
merged_normalized.to_csv('4_gt_normal_rescaled_rsv.csv', index=False)

# Print information about the merged files
print("\ngt_rescaled_rsv_values.csv:")
print(f"Number of rows: {len(merged_rescaled)}")
print(f"Columns: {merged_rescaled.columns.tolist()}")
print(f"Date range: {merged_rescaled['date'].min()} to {merged_rescaled['date'].max()}")

print("\ngt_normal_rescaled_rsv.csv:")
print(f"Number of rows: {len(merged_normalized)}")
print(f"Columns: {merged_normalized.columns.tolist()}")
print(f"Date range: {merged_normalized['date'].min()} to {merged_normalized['date'].max()}")

