# tests

This folder contains test scripts for various utilities used in data visualization and image handling within the Termux environment.

## Contents

1. `test_save.py`: A lightweight alternative to using a VNC Viewer in a Termux Graphical Environment.
2. `test_combine.py`: A script for creating and combining multiple plots into a single image.

## Termux:API and Android OS Compatibility

Due to the nuances of Android OS, command-line utilities work on the file system using Linux APIs, bypassing the Android OS. This means that created or modified files may not be immediately visible to other applications. To address this, we use the Termux:API package, specifically the `termux-media-scan` command, to trigger a media rescan manually.

Example usage:
```
termux-media-scan -r /storage/emulated/0/
```

This ensures that our generated plots are properly registered in the Android media database and visible to other apps.

## Multi-Plot Combination Utility

The `combine_test.py` script demonstrates how to create multiple plots and combine them into a single image. This approach is useful for creating complex visualizations or dashboards.

### Future Enhancement Example

Here's an example of how we might extend the multi-plot combination utility with additional features:

```python
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageDraw, ImageFont

def create_plot(data, title, filename):
    plt.figure(figsize=(8, 6))
    plt.plot(data)
    plt.title(title)
    plt.savefig(filename)
    plt.close()

def combine_plots(plot_files, layout=(2,2), title="Dashboard"):
    images = [Image.open(f) for f in plot_files]
    widths, heights = zip(*(i.size for i in images))

    max_width = max(widths)
    max_height = max(heights)

    dashboard = Image.new('RGB', (max_width*layout[1], max_height*layout[0] + 50), color='white')
    
    for i, image in enumerate(images):
        row = i // layout[1]
        col = i % layout[1]
        dashboard.paste(image, (col*max_width, row*max_height + 50))

    # Add title
    draw = ImageDraw.Draw(dashboard)
    font = ImageFont.truetype("/path/to/font.ttf", 36)
    draw.text((10, 10), title, font=font, fill="black")

    return dashboard

# Usage
plot_files = ['plot1.png', 'plot2.png', 'plot3.png', 'plot4.png']
for i, file in enumerate(plot_files):
    create_plot(np.random.rand(100), f"Plot {i+1}", file)

combined = combine_plots(plot_files, layout=(2,2), title="My Dashboard")
combined.save("dashboard.png")
```

This enhanced version allows for custom layouts and adds a title to the combined image, providing more flexibility in creating complex visualizations.
