# datasets

This repository contains various datasets intended for practicing data visualization with Python, specifically in a Termux development environment. The primary goal is to explore different visualization techniques and improve data analysis skills using limited mobile resources.

## Datasets

### 1. US Presidential Elections (us-pres)
This dataset includes US presidential election data from 1976 to 2020, providing information on candidates, parties, and voting results.

### 2. UFC Match History (ufc)
This dataset contains the entire history of UFC matches, including details such as fighters, weight classes, and fight outcomes.

## Planned Features

Beyond traditional matplotlib graphs, we plan to explore:

1. ASCII art visualizations
2. Text-based heatmaps
3. Terminal-friendly interactive plots
4. Custom color schemes for improved readability on mobile devices
5. Geospatial visualizations for election data

## Tests

The `tests` folder in the root directory contains utilities for:

- Combining multiple graphs
- Saving and displaying graphs
- Color palette generation

### Future Utilities to Test

- Data preprocessing functions
- Custom text-based plotting functions
- Performance optimization for large datasets
- Error handling and input validation
- Data export in various formats

### Code Example

```python
# Combining utilities: data preprocessing, custom color palette, and multiple graph combination

# Pseudo-code for demonstration purposes
from tests import preprocess_data, generate_color_palette, combine_graphs

# Preprocess the UFC dataset
ufc_data = preprocess_data('ufc')

# Generate a custom color palette
palette = generate_color_palette(5)

# Create multiple graphs
graph1 = create_fighter_win_loss_chart(ufc_data, palette[0:2])
graph2 = create_weight_class_distribution(ufc_data, palette[2:4])
graph3 = create_finish_type_pie_chart(ufc_data, palette[4])

# Combine the graphs into a single visualization
combined_graph = combine_graphs([graph1, graph2, graph3])

# Display or save the combined graph
combined_graph.show()
```
