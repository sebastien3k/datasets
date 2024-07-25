# us-pres

This Python script analyzes and visualizes data from US presidential elections from 1976 to 2020. It generates six different plots to showcase various trends and patterns in the election data, combines these plots into a single image, and provides functionality to view the results on a Termux environment.

## Prerequisites

- Python 3.x
- Termux (for Android)
- The following Python libraries:
  - pandas
  - matplotlib
  - seaborn
  - Pillow (PIL)
  - tqdm

You can install these libraries using pip:

```
pip install pandas matplotlib seaborn Pillow tqdm
```

## Dataset

The script expects a CSV file named `1976-2020-president.csv` containing the following columns:

- year: Year of the election
- office: Always "US PRESIDENT"
- state: State name
- state_po: US postal code state abbreviation
- state_fips: State FIPS code
- state_cen: US Census state code
- state_ic: ICPSR state code
- candidate: Name of the candidate
- party_detailed: Detailed party affiliation
- party_simplified: Simplified party affiliation (DEMOCRAT, REPUBLICAN, LIBERTARIAN, OTHER)
- writein: Boolean indicating if the candidate was a write-in
- candidatevotes: Number of votes received by the candidate
- totalvotes: Total number of votes cast in the election
- version: Dataset version date
- mode: Voting mode (e.g., absentee, election day, early)

## Script Overview

The script performs the following main tasks:

1. Loads the election data from the CSV file.
2. Creates six different plots:
   - Total votes over the years
   - Party vote share (Democrat vs Republican)
   - Top 10 states with highest average turnout
   - Write-in votes trend
   - Party diversity over time
   - Top 5 third-party candidates
3. Saves each plot as an individual PNG file.
4. Combines all six plots into a single 3x2 grid image.
5. Runs `termux-media-scan` on all generated images.
6. Attempts to open the combined image using `termux-open`.

## Functions

### Plot Creation Functions

1. `plot_total_votes(df)`: Creates a line plot of total votes over the years.
2. `plot_party_vote_share(df)`: Creates an area plot of Democrat vs Republican vote share.
3. `plot_top_states_turnout(df)`: Creates a bar plot of the top 10 states with highest average turnout.
4. `plot_writein_votes_trend(df)`: Creates a line plot of write-in votes trend.
5. `plot_party_diversity(df)`: Creates a line plot of the number of distinct parties over time.
6. `plot_top_third_party_candidates(df)`: Creates a bar plot of the top 5 third-party candidates.

## Usage

1. Ensure you have the required CSV file in the same directory as the script.
2. Run the script in a Termux environment:

```
python test_analysis_final.py
```

3. The script will create individual plot images and a combined image in the `/storage/emulated/0/Download/election_plots/` directory.
4. Progress bars will show the status of plot creation and media scanning.
5. The script will attempt to open the combined image automatically.

## Output

- Six individual plot images (PNG format)
- One combined image containing all six plots in a 3x2 grid (PNG format)
- Console output showing progress and any errors

## Notes

- The script uses a consistent figure size (10x6 inches) for all plots to ensure uniform appearance in the combined image.
- The combined image has a white background to avoid any visible misalignments.
- The script uses `termux-media-scan` to ensure the Android media scanner recognizes the new images.
- If `termux-open` fails to open the combined image, you may need to open it manually from the specified directory.

## Customization

You can customize the script by:

- Changing the `fig_size` variable to adjust the size of individual plots.
- Modifying the plot functions to change the appearance or data representation.
- Adjusting the `save_dir` variable to change where the images are saved.

## Troubleshooting

If you encounter any issues:

1. Ensure all required libraries are installed.
2. Check that the CSV file is in the correct location and format.
3. Verify that Termux has permission to access your device's storage.
4. If plots are not visible or are cut off, try adjusting the `fig_size` or using `plt.tight_layout()` in the plotting functions.
