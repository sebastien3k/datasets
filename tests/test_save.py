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
plt.xlabel('X axis')
plt.ylabel('Y axis')

# Define the save path (adjust as needed)
save_path = '/storage/emulated/0/Download/sine_wave.png'

# Save the plot
plt.savefig(save_path)
plt.close()

print(f"Graph saved to: {save_path}")

# Run termux-media-scan
subprocess.run(['termux-media-scan', save_path])

print("Media scan completed")

# Open the image (this uses xdg-open, which might not work on all Android setups)
try:
    subprocess.run(['xdg-open', save_path])
    print("Opened the image file")
except FileNotFoundError:
    print("Could not open the image automatically. Please open it manually.")

print("Script completed")
