import pandas as pd
import matplotlib.pyplot as plt
import os

# Load the dataset
df = pd.read_csv('1976-2020-president.csv')

# Filter the dataset for relevant columns and rows
df = df[['year', 'party_simplified', 'candidatevotes', 'candidate']]
df = df[df['party_simplified'].isin(['DEMOCRAT', 'REPUBLICAN'])]

# Group by year and party and sum the votes
votes_by_party_year = df.groupby(['year', 'party_simplified'])['candidatevotes'].sum().unstack()

# Get the candidates for presidential election years
election_years = [1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020]
candidates = df[df['year'].isin(election_years)].groupby(['year', 'party_simplified'])['candidate'].first().unstack()

# Plot the data
plt.figure(figsize=(12, 6))
plt.plot(votes_by_party_year.index, votes_by_party_year['DEMOCRAT'], label='Democrat', color='blue')
plt.plot(votes_by_party_year.index, votes_by_party_year['REPUBLICAN'], label='Republican', color='red')

# Annotate the points
for year in election_years:
    if year in votes_by_party_year.index:
        # Annotate Democrat candidate
        if 'DEMOCRAT' in votes_by_party_year.columns and not pd.isna(candidates.loc[year, 'DEMOCRAT']):
            plt.annotate(f"{candidates.loc[year, 'DEMOCRAT']}", 
                         (year, votes_by_party_year.loc[year, 'DEMOCRAT']),
                         textcoords="offset points", xytext=(-10,10), ha='center', color='blue')
        # Annotate Republican candidate
        if 'REPUBLICAN' in votes_by_party_year.columns and not pd.isna(candidates.loc[year, 'REPUBLICAN']):
            plt.annotate(f"{candidates.loc[year, 'REPUBLICAN']}", 
                         (year, votes_by_party_year.loc[year, 'REPUBLICAN']),
                         textcoords="offset points", xytext=(10,-10), ha='center', color='red')

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Total Votes')
plt.title('Total Votes for Democratic and Republican Candidates (1976-2020)')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()

# Termux specific graph rendering
# Define the directory and the filename.
directory = os.path.join(os.environ["HOME"], "storage", "shared", "dataviz")
filename = "votes_by_year_v2.png"

# Create the directory if it does not exist.
os.makedirs(directory, exist_ok=True)

# Define the full path to save the image.
save_path = os.path.join(directory, filename)

# Save the figure to the specified path.
plt.savefig(save_path)

# Define actual android path
android_storage_path = "/storage/emulated/0/dataviz/" + filename

os.system("termux-media-scan -r /storage/emulated/0/")

# Use termux-open to open the image.
os.system("termux-open " + android_storage_path)
