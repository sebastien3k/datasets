import matplotlib.pyplot as plt
import numpy as np
import os
import subprocess
from PIL import Image

def create_plot(x, y, title, filename):
    plt.figure(figsize=(8, 6))
    plt.plot(x, y)
    plt.title(title)
    plt.xlabel('X axis')
    plt.ylabel('Y axis')
    plt.savefig(filename)
    plt.close()

# Define the save paths
base_path = '/storage/emulated/0/Download/'
plot_files = [
    base_path + 'plot1.png',
    base_path + 'plot2.png',
    base_path + 'plot3.png',
    base_path + 'plot4.png'
]
final_image = base_path + 'combined_plots.png'

# Generate data and create plots
x = np.linspace(0, 10, 100)

create_plot(x, np.sin(x), 'Sine Wave', plot_files[0])
create_plot(x, np.cos(x), 'Cosine Wave', plot_files[1])
create_plot(x, np.tan(x), 'Tangent Wave', plot_files[2])
create_plot(x, x**2, 'Quadratic Function', plot_files[3])

print("Individual plots saved.")

# Combine plots using Pillow
images = [Image.open(f) for f in plot_files]
widths, heights = zip(*(i.size for i in images))

max_width = max(widths)
max_height = max(heights)

new_im = Image.new('RGB', (max_width*2, max_height*2))

new_im.paste(images[0], (0, 0))
new_im.paste(images[1], (max_width, 0))
new_im.paste(images[2], (0, max_height))
new_im.paste(images[3], (max_width, max_height))

new_im.save(final_image)

print(f"Combined image saved to: {final_image}")

# Run termux-media-scan on all files
for file in plot_files + [final_image]:
    subprocess.run(['termux-media-scan', file])

print("Media scan completed")

# Open the combined image
try:
    subprocess.run(['termux-open', final_image])
    print("Opened the combined image file")
except FileNotFoundError:
    print("Could not open the image automatically. Please open it manually.")

# Clean up individual plot files
for file in plot_files:
    os.remove(file)

print("Individual plot files cleaned up")
print("Script completed")
