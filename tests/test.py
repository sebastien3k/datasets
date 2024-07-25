import matplotlib.pyplot as plt
import numpy as np
import os
import subprocess

# Generate some sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(x, y)
plt.title('Sine Wave')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Define the save path (adjust as needed)
save_path = '/sdcard/Download/sine_wave_plot.png'

# Save the plot
plt.savefig(save_path)
plt.close()

print(f"Graph saved to: {save_path}")

# Run termux-media-scan
subprocess.run(['termux-media-scan', save_path])
print("Media scan completed")

# Open the image using termux-open
subprocess.run(['termux-open', save_path])
print("Opening the image...")
