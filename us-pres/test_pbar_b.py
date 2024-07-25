import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import subprocess
from PIL import Image
import os
from tqdm import tqdm

# Load the dataset
df = pd.read_csv('1976-2020-president.csv')

# Create a directory to save plots
save_dir = '/storage/emulated/0/Download/election_plots_d/'
os.makedirs(save_dir, exist_ok=True)

plot_files = []

# Define plot functions
def plot_total_votes(df):
    plt.figure(figsize=(10, 6))
    df_yearly = df.groupby('year')['totalvotes'].sum().reset_index()
    sns.lineplot(x='year', y='totalvotes', data=df_yearly)
    plt.title('Total Votes in US Presidential Elections (1976-2020)')
    plt.ylabel('Total Votes')
    return 'total_votes_trend.png'

def plot_party_vote_share(df):
    plt.figure(figsize=(10, 6))
    df_party = df[df['party_simplified'].isin(['DEMOCRAT', 'REPUBLICAN'])].groupby(['year', 'party_simplified'])['candidatevotes'].sum().unstack()
    df_party = df_party.div(df_party.sum(axis=1), axis=0)
    df_party.plot(kind='area', stacked=True)
    plt.title('Democrat vs Republican Vote Share (1976-2020)')
    plt.ylabel('Vote Share')
    return 'party_vote_share.png'

def plot_top_states_turnout(df):
    plt.figure(figsize=(10, 6))
    df_state_turnout = df.groupby('state')['totalvotes'].mean().sort_values(ascending=False).head(10)
    sns.barplot(x=df_state_turnout.index, y=df_state_turnout.values)
    plt.title('Top 10 States with Highest Average Turnout')
    plt.ylabel('Average Total Votes')
    plt.xticks(rotation=45)
    return 'top_states_turnout.png'

def plot_writein_votes_trend(df):
    plt.figure(figsize=(10, 6))
    df_writein = df[df['writein'] == True].groupby('year')['candidatevotes'].sum()
    sns.lineplot(x=df_writein.index, y=df_writein.values)
    plt.title('Write-in Votes Trend (1976-2020)')
    plt.ylabel('Total Write-in Votes')
    return 'writein_votes_trend.png'

def plot_party_diversity(df):
    plt.figure(figsize=(10, 6))
    df_party_count = df.groupby('year')['party_detailed'].nunique()
    sns.lineplot(x=df_party_count.index, y=df_party_count.values)
    plt.title('Number of Distinct Parties Over Time')
    plt.ylabel('Number of Parties')
    return 'party_diversity.png'

def plot_top_third_party_candidates(df):
    plt.figure(figsize=(10, 6))
    df_third_party = df[(df['party_simplified'] == 'OTHER') & (df['writein'] == False)]
    top_5_third_party = df_third_party.groupby('candidate')['candidatevotes'].sum().sort_values(ascending=False).head()
    sns.barplot(x=top_5_third_party.index, y=top_5_third_party.values)
    plt.title('Top 5 Third-Party Candidates (1976-2020)')
    plt.ylabel('Total Votes')
    plt.xticks(rotation=45, ha='right')
    return 'top_third_party_candidates.png'

# List of plot functions
plot_functions = [
    plot_total_votes,
    plot_party_vote_share,
    plot_top_states_turnout,
    plot_writein_votes_trend,
    plot_party_diversity,
    plot_top_third_party_candidates
]

# Create plots with progress bar
for plot_func in tqdm(plot_functions, desc="Creating plots"):
    filename = plot_func(df)
    save_path = os.path.join(save_dir, filename)
    plt.savefig(save_path)
    plt.close()
    plot_files.append(save_path)

# Stitch images together
images = [Image.open(f) for f in plot_files]
widths, heights = zip(*(i.size for i in images))

max_width = max(widths)
max_height = max(heights)

new_im = Image.new('RGB', (max_width*3, max_height*2))

x_offset = 0
y_offset = 0
for i, im in enumerate(images):
    new_im.paste(im, (x_offset, y_offset))
    if (i+1) % 3 == 0:
        y_offset += max_height
        x_offset = 0
    else:
        x_offset += max_width

final_image = os.path.join(save_dir, 'combined_plots.png')
new_im.save(final_image, 'PNG')

# Run termux-media-scan on all files with progress bar
all_files = plot_files + [final_image]
for file in tqdm(all_files, desc="Running media scan"):
    subprocess.run(['termux-media-scan', file])

print("Media scan completed")

# Open the combined image
try:
    subprocess.run(['termux-open', final_image])
    print("Opened the combined image file")
except FileNotFoundError:
    print("Could not open the image automatically. Please open it manually.")
