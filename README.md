# Overview

This is the repository for the Jupyter notebook and dataset used for the following conference paper:

Michael T. Lopez, Cheska Elise Hung, and Maria Regina Justina E. Estuar.\
**Network Density Analysis of Health Seeking Behavior in Metro Manila: A Retrospective Analysis on COVID-19 Google Trends Data**\
In Proceedings of the 9th International Conference on Medical and Health Informatics (ICMHI 2025)\
Link: https://doi.org/10.48550/arXiv.2503.21162 (currently available as a pre-print on arXiv)

It was the first part of the undergraduate thesis of Michael T. Lopez II and Cheska Elise Hung from the Ateneo de Manila University, Philippines. Our supervisor for this work is Dr. Maria Regina Justine E. Estuar, PhD. 

This paper's goal is to determine the online health-seeking behavior of those residing in Metro Manila (National Capital Region) on how they utilized Google for searching terms related to the COVID-19 pandemic. However, instead of investigating each term individually, we converted them into a network graph using correlation and adjacency matrices.

## Requirements

The following code was ran on an Apple Macbook Air M1 (2020). Here are the specifications of the hardware:

| Hardware | Specification |
|----------|---------------|
| Processor | Apple M1 chip with 8-core CPU |
| Memory | 8GB unified memory |
| Storage | 256GB SSD |

We then used the `python` programming language (version 3.12.2) on Jupyter notebook.

# How to Cite

If you will use or build upon on top of the code materials, please use the following BibTeX entry below to cite the concerned paper depending on the purpose of what code you will be using. Take note that you should *not* be citing this Github repository directly.

## Google Trends Scraper

If you will be using the Google Trends scraper using the `pytrends` API, the scripts are located at the `gt_scraper` directory. This code was originated from: 

Amanda M Y Chu, Andy C Y Chong, Nick H T Lai, Agnes Tiwari, and Mike K P So. 2023. Enhancing the Predictive Power of Google Trends Data Through Network Analysis: Infodemiology Study of COVID-19. *JMIR Public Health Surveill.* 9, (September 2023). https://doi.org/10.2196/42446

Below is the BibTeX entry of the article:

```bibtex
@article{chuEnhancing2023,
  title = {Enhancing the {{Predictive Power}} of {{Google Trends Data Through Network Analysis}}: {{Infodemiology Study}} of {{COVID-19}}},
  shorttitle = {Enhancing the {{Predictive Power}} of {{Google Trends Data Through Network Analysis}}},
  author = {Chu, Amanda M Y and Chong, Andy C Y and Lai, Nick H T and Tiwari, Agnes and So, Mike K P},
  year = {2023},
  month = sep,
  journal = {JMIR Public Health and Surveillance},
  volume = {9},
  issn = {2369-2960},
  doi = {10.2196/42446},
}
```

## Google Trends Preprocessing and Network Analysis Conversion

For the remainder of the other code and all datasets used, these were all original work from our team. Please use the following BibTeX entry to cite our paper if you have used any part of the code or dataset (besides the Google Trends scraper script):

```bibtex
@misc{lopezNetwork2025,
  title = {Network {{Density Analysis}} of {{Health Seeking Behavior}} in {{Metro Manila}}: {{A Retrospective Analysis}} on {{COVID-19 Google Trends Data}}},
  shorttitle = {Network {{Density Analysis}} of {{Health Seeking Behavior}} in {{Metro Manila}}},
  author = {Lopez, Michael T. II and Hung, Cheska Elise and Estuar, Maria Regina Justina E.},
  year = {2025},
  month = mar,
  number = {arXiv:2503.21162},
  eprint = {2503.21162},
  primaryclass = {cs},
  publisher = {arXiv},
  doi = {10.48550/arXiv.2503.21162},
}
```

This will be updated accordingly in the future once we have received the official DOI when the conference indexed our work. For now, the pre-print version could be viewed at arXiv.

# Navigating Contents of Repository

## Google Trends Scraper

```
gt_scraper/
├── download_data.py    # Main script with command line interface
└── download.py         # Helper functions for data retrieval
```

The `gt_scraper` directory contains two scripts. These facilitate the collection of Google Trends data for specified search terms over custom date ranges.

### Installation

Please install the required packages using `pip`:

```bash
pip install pytrends click
```

### Parameters

* `--tag`: The search term to track in Google Trends
* `--region` or `-r`: Geographic location of interest (e.g., "US", "GB", "JP", "PH")
* `--start-date`: Beginning of the date range in YYYY-MM-DD format
* `--end-date`: End of the date range in YYYY-MM-DD format
* `--days` or `-n`: Number of days per request (default: 29)
* `--proxy` or `-p`: Use proxies for requests (optional)
* `--delay` or `-d`: Delay between requests in seconds (default: 60)

### Output

The script creates directories named after the search term (with '/' replaced by '.') and saves CSV files containing the Google Trends data. Files are named according to the date range they cover:

* Regular files: `YYYY MM DD.csv`
* Incomplete data: `YYYY MM DD.partial.csv`

### Usage of GT Scraper Scripts

The script uses a command-line interface to download Google Trends data. Below is a sample of collecting data from the Metro Manila region in the Philippines:

```bash
python download.py --tag "covid-19" --region "PH-00" --start-date "2023-01-01" --end-date "2023-12-31" --days 30
```

### Notes for GT Scraper

* The script handles Google Trends' limitations by breaking requests into smaller time periods
* Incomplete data is marked with `.partial.csv`
* If you encounter rate limiting, try increasing the `--delay` parameter
* For international searches, specify the appropriate region code

## Output Dataset of Google Trends Scraper

```
gt_raw_daily30daywindow_volumes/
├── cough/
│   ├── extra_day/2021 02 20.csv
│   └── ... (30-day rolling window CSV files from March 16, 2020 until March 15, 2021)
├── ecq/
│   ├── extra_day/2021 02 20.csv
│   └── ... (30-day rolling window CSV files from March 16, 2020 until March 15, 2021)
├── face-shield/
│   ├── extra_day/2021 02 20.csv
│   └── ... (30-day rolling window CSV files from March 16, 2020 until March 15, 2021)
└── ... (12 more directories)
```

You may see on the `gt_raw_daily30daywindow_volumes` directory for the 30-day rolling window datasets of each search term. The subdirectory's name is that search keyword used. There are 15 directories that represents the 15 keywords used in the study.

On each subdirectory, you may see the comma separated value (CSV) files named after the first day when it scraped the popularity score of that search term. For example, if it is named `2020 03 16.csv`, then you will see the popularity scores for that term from March 16, 2020 until April 15, 2020. 

There is also an additional folder named `extra_day` for the purpose of completing the one-year timeline for the data preprocessing used in the conference paper. This is formally known as **Rescaling Daily Data Method**. Take note this was referred to as "RSV" in the filenames for simplicity.

## Preprocessing Google Trends Dataset

Under the `gt_preprocessed_data` directory, there are two subdirectories that featured two different data preprocessing method. Then under each subdirectory there are Jupyter notebooks, further subdirectories, and CSV dataset files. Here is an overview for it:

```
gt_preprocessed_data/
├── gt_msv_stitched/
│   ├── 1_gt_msv_compute.ipynb
│   ├── 2_gt_msv_merge.ipynb
│   ├── 3_gt_msv_stitched_compute.csv
│   └── ... (15 files of "{keyword}_msv_stitched_30day.csv") 
├── gt_rsv_stitched/
│   ├── gt_rsv_daily_raw_stitched/
│   │   └── ... (15 files of "{keyword}_rsv_daily_raw_stitched.csv")
│   ├── gt_rsv_weekly_raw_volumes/
│   │   └── ... (15 files of "{keyword}_weekly_raw.csv")
│   ├── gt_weekly_weight/
│   │   └── ... (15 files of "{keyword}_weekly_search_weight.csv")
│   ├── 1_gt_rsv_keyword_daily_value.ipynb
│   ├── 2_gt_rsv_merge.ipynb
│   ├── 3_gt_rescaled_rsv.csv
│   ├── 4_gt_normal_rescaled_rsv.csv
└── └── ... (15 files of {keyword}_rsv_stitched.csv)
```

### Rescaling Daily Data Method

The preprocessed data used for the conference paper can be found on the `gt_rsv_stitched` directory. 

This Rescaling Daily Data algorithm uses weekly data as a reference to rescale daily data, ensuring consistent relative search volumes across different time periods. It was also originally derived from the data preprocessing used in the study below:

Abel Brodeur, Andrew E. Clark, Sarah Fleche, and Nattavudh Powdthavee. 2021. COVID-19, lockdowns and well-being: Evidence from Google Trends. *J. Public Econ.* 193, (January 2021). https://doi.org/10.1016/j.jpubeco.2020.104346


There are three subdirectories under this:

* `gt_rsv_daily_raw_stitched`: This contains all the comma separated value (CSV) filenames of `{keyword}_rsv_daily_raw_stitched.csv`. The data came from adjacently putting together the CSV files from each search term in the `gt_raw_daily30daywindow_volumes` directory. For example, under `ubo`, we will combine together the CSV files of March 16, 2020 until April 15, 2020, then April 16, s2020 until May 15, 2020, and so on until it reaches March 15, 2021. That is the reason why we have the `extra_day` directory to complete the one-year series.

* `gt_rsv_weekly_raw_volumes`: This contains all CSV files which were weekly data's worth for one-year on each search term. If you read the paper, we could only download a resolution of daily data until nine months. Beyond that, Google Trends will return a weekly resolution of data.

* `gt_weekly_weight`: This contains all the weekly weights by comparing the direct weekly values (downloaded directly from GT) to the daily averages (manually computed the mean from the CSV files in `gt_rsv_daily_raw_stitched`)

There are two Jupyter notebooks under this:

* `1_gt_rsv_keyword_daily_value.ipynb`: It calculates the weekly metrics based on daily data. Then, it computes the rescaling weights from weekly data. The weights will then apply to the daily data to ensure consistent scaling. Optionally, it will normalize the rescaled values to a 0-100 range. Take note that we used the non-normalized version for the paper to capture a more accurate representation of the popularity values.

  * Input: 
    * Raw daily Google Trends data files in 30-day windows in `gt_raw_daily30daywindow_volumes/{keyword}/`
    * Weekly Google Trends data files (from `gt_rsv_weekly_raw_volumes` subdirectory within)

  * Output: 
    * Stitched daily data files (`gt_rsv_daily_raw_stitched`)
    * Weekly weight calculation files (`gt_weekly_weight`) 
    * Final rescaled data files for each keyword (`{keyword}_rsv_stitched.csv`)

* `2_gt_rsv_merge.ipynb`: This script combines the individual keyword files into consolidated datasets. So it reads first all processed keyword files. Then, combines them into two comprehensive datasets. 

  * Input: 
    * Individual keyword rescaled files (`{keyword}_rsv_stitched.csv`)
  
  * Output:
    * Raw rescaled values (`3_gt_rescaled_rsv.csv`)
    * Normalized (0-100) values (`4_gt_normal_rescaled_rsv.csv`)

### Merged Search Volume Method

Another pre-processing method was used (never featured in the conference paper) was the Merged Search Volume Algorithm. This process can be found in the `gt_msv_stitched` subdirectory. This was also fetched from the Chu, et al. (2023) study stated earlier. 

The stitching works by having a 30-day overlapping window, wherein it will identify the common dates. For each of these common dates, we need to calculate the quotient wherein it is the $`\text{value_in_first_csv_file} / \text{value_in_second_csv_file}`$. Then, we will average these quotients to create the correction factor. The edge cases such as `NaNs`, zeroes, and infinities were handled by using default factors.

The data stitching happens when we get the first 29 days from the first file (this is unchanged). Then, for each subsequent file, we will apply the correction factor to the 30th day, and add this corrected value to the stitched time series. We will continuously do this until we have filled every gap to complete the one year.

There are two Jupyter notebooks under this:

* `1_gt_msv_compute.ipynb`: This processes raw Google Trends data files for each keyword, and indentifies the overlapping dates between the consecutive 30-day windows. We will calculate the correction factors based on these overlaps. Finally, it applies the correction factors to create consistently scaled time series until the cutoff date of March 15, 2021.

  * Input:

    * Raw 30-day window Google Trends data files in `gt_raw_daily30daywindow_volumes/{keyword}/`
  * Output:

    * Individual keyword files (`{keyword}_msv_stitched_30day.csv`)

* `2_gt_msv_merge.ipynb`: This script combines individual keyword files into a consolidated dataset. First, it will load and standardize each keyword's processed data. Then, merges all keywords based on date. This also ensures consistent date formats. The expected result is a single comprehensive dataset with all search terms.

  * Input:

    * Individual keyword files (`{keyword}_msv_stitched_30day.csv`)

  * Output:

    * 3_gt_msv_stitched_compute.csv (`3_gt_msv_stitched_compute.csv`)

### Keywords Used on Both Preprocessing Methods

The Jupyter notebooks on either strategies of data preprocessing used the following keywords:

```
flu, cough, fever, headache, lagnat, rashes, sipon, ubo, ecq, 
face-shield, Frontliners, masks, Quarantine, social-distancing, work-from-home
```

These include both symptom terms and pandemic-related social terms in English and Filipino languages.