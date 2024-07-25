import matplotlib.pyplot as plt
import numpy as np
import os
import subprocess
from PIL import Image

def create_and_save_plot(x, y, title, filename):
    plt.figure(figsize=(8, 6))
    plt.plot(x, y)
    plt.title(title)
    plt.xlabel('X axis')
    plt.ylabel('Y axis')
    plt.savefig(filename)
    plt.close()

# Generate sample data for four different plots
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = x**2
y4 = np.exp(x/10)

# Define the base path for saving
base_path = '/storage/emulated/0/Download/'

# Create and save individual plots
plots = [
    ('Sine Wave', y1, 'sine_wave.png'),
    ('Cosine Wave', y2, 'cosine_wave.png'),
    ('Quadratic Function', y3, 'quadratic.png'),
    ('Exponential Function', y4, 'exponential.png')
]

for title, y, filename in plots:
    full_path = os.path.join(base_path, filename)
    create_and_save_plot(x, y, title, full_path)
    print(f"Saved {filename}")

# Stitch images together
images = [Image.open(os.path.join(base_path, filename)) for _, _, filename in plots]
widths, heights = zip(*(i.size for i in images))

max_width = max(widths)
max_height = max(heights)

new_im = Image.new('RGB', (max_width*2, max_height*2))

x_offset = 0
y_offset = 0
for i, im in enumerate(images):
    new_im.paste(im, (x_offset, y_offset))
    if i % 2 == 0:
        x_offset += max_width
    else:
        x_offset = 0
        y_offset += max_height

# Save the stitched image
stitched_filename = 'stitched_plots.png'
stitched_path = os.path.join(base_path, stitched_filename)
new_im.save(stitched_path)
print(f"Saved stitched image to {stitched_path}")

# Run termux-media-scan on all saved files
for _, _, filename in plots:
    subprocess.run(['termux-media-scan', os.path.join(base_path, filename)])
subprocess.run(['termux-media-scan', stitched_path])

print("Media scan completed")

# Open the stitched image
try:
    subprocess.run(['termux-open', stitched_path])
    print("Opened the stitched image file")
except FileNotFoundError:
    print("Could not open the image automatically. Please open it manually.")

print("Script completed")
