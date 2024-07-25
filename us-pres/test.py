import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
import subprocess
import os

# Load the dataset
df = pd.read_csv('1976-2020-president.csv')

# Create a directory to save plots
save_dir = '/storage/emulated/0/Download/election_plots_b/'
os.makedirs(save_dir, exist_ok=True)

plot_files = []

# 1. Voter Turnout Over Time
plt.figure(figsize=(10, 6))
df_turnout = df.groupby('year')['totalvotes'].sum().reset_index()
sns.lineplot(x='year', y='totalvotes', data=df_turnout)
plt.title('Voter Turnout Over Time')
plt.ylabel('Total Votes')
save_path = os.path.join(save_dir, 'turnout_over_time.png')
plt.savefig(save_path)
plt.close()
plot_files.append(save_path)

# 2. Party Vote Share
plt.figure(figsize=(10, 6))
df_party = df[df['party_simplified'].isin(['DEMOCRAT', 'REPUBLICAN'])]
df_party_share = df_party.groupby(['year', 'party_simplified'])['candidatevotes'].sum().unstack()
df_party_share = df_party_share.div(df_party_share.sum(axis=1), axis=0)
df_party_share.plot(kind='area', stacked=True)
plt.title('Party Vote Share Over Time')
plt.ylabel('Vote Share')
save_path = os.path.join(save_dir, 'party_vote_share.png')
plt.savefig(save_path)
plt.close()
plot_files.append(save_path)

# 3. Top 10 States by Average Voter Turnout
plt.figure(figsize=(10, 6))
df_state_turnout = df.groupby('state')['totalvotes'].mean().sort_values(ascending=False).head(10)
sns.barplot(x=df_state_turnout.index, y=df_state_turnout.values)
plt.title('Top 10 States by Average Voter Turnout')
plt.xticks(rotation=45)
plt.ylabel('Average Total Votes')
save_path = os.path.join(save_dir, 'top_states_turnout.png')
plt.savefig(save_path)
plt.close()
plot_files.append(save_path)

# 4. Write-in Votes Over Time
plt.figure(figsize=(10, 6))
df_writein = df[df['writein'] == True].groupby('year')['candidatevotes'].sum()
sns.lineplot(x=df_writein.index, y=df_writein.values)
plt.title('Write-in Votes Over Time')
plt.ylabel('Total Write-in Votes')
save_path = os.path.join(save_dir, 'writein_votes.png')
plt.savefig(save_path)
plt.close()
plot_files.append(save_path)

# 5. Party Distribution (Simplified)
plt.figure(figsize=(10, 6))
df['party_simplified'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('Party Distribution (Simplified)')
save_path = os.path.join(save_dir, 'party_distribution.png')
plt.savefig(save_path)
plt.close()
plot_files.append(save_path)

# 6. Candidate Votes Distribution (Top 10)
plt.figure(figsize=(10, 6))
df_candidate = df.groupby('candidate')['candidatevotes'].sum().sort_values(ascending=False).head(10)
sns.barplot(x=df_candidate.index, y=df_candidate.values)
plt.title('Top 10 Candidates by Total Votes')
plt.xticks(rotation=45, ha='right')
plt.ylabel('Total Votes')
save_path = os.path.join(save_dir, 'top_candidates.png')
plt.savefig(save_path)
plt.close()
plot_files.append(save_path)

# Run termux-media-scan on individual plot files
for file in plot_files:
    subprocess.run(['termux-media-scan', file])

print("Individual plots saved and scanned")

# Combine plots into a 3x2 grid
images = [Image.open(file) for file in plot_files]
widths, heights = zip(*(i.size for i in images))

max_width = max(widths)
max_height = max(heights)

new_im = Image.new('RGB', (max_width * 3, max_height * 2))

x_offset = 0
y_offset = 0
for i, im in enumerate(images):
    new_im.paste(im, (x_offset, y_offset))
    if (i + 1) % 3 == 0:
        y_offset += max_height
        x_offset = 0
    else:
        x_offset += max_width

final_image = os.path.join(save_dir, 'combined_plots.png')
new_im.save(final_image, 'PNG')

# Run termux-media-scan on the final image
subprocess.run(['termux-media-scan', final_image])

print("Combined image saved and scanned")

# Open the combined image
try:
    subprocess.run(['termux-open', final_image])
    print("Opened the combined image file")
except FileNotFoundError:
    print("Could not open the image automatically. Please open it manually.")
