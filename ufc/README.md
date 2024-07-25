# ufc

This folder contains comprehensive data on UFC fights, including fighter statistics, fight outcomes, and various performance metrics.

## Dataset Overview

The dataset provides detailed information for each UFC fight, with statistics for both the red and blue corner fighters. Each row represents a single fight, with columns prefixed 'R_' for red corner and 'B_' for blue corner fighter stats.

Key features include:
- Fighter performance metrics (knockdowns, strikes, takedowns, etc.)
- Fight details (date, location, weight class, etc.)
- Fighter attributes (stance, height, reach, age)
- Career statistics (win/loss records, streaks, title bouts)

Target variable: 'Winner' (outcome of the fight)

## Development Plans

### Visualization Ideas

1. Fighter Evolution: Track a fighter's performance metrics over time
2. Stance Effectiveness: Compare win rates and fight statistics across different stances
3. Age vs Performance: Analyze the relationship between age and various performance metrics

Example code for visualizing stance effectiveness:

```python
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
ufc_data = pd.read_csv('ufc_data.csv')

# Group by stance and calculate win rate
stance_stats = ufc_data.groupby('Stance').agg({
    'Winner': lambda x: (x == x.name).mean(),
    'R_KD': 'mean',
    'R_SIG_STR_pct': 'mean'
}).reset_index()

# Create a multi-bar plot
fig, ax = plt.subplots(figsize=(10, 6))
x = stance_stats['Stance']
width = 0.25

ax.bar(x, stance_stats['Winner'], width, label='Win Rate')
ax.bar(x + width, stance_stats['R_KD'], width, label='Avg Knockdowns')
ax.bar(x + 2*width, stance_stats['R_SIG_STR_pct'], width, label='Sig Strike %')

ax.set_xlabel('Stance')
ax.set_ylabel('Metrics')
ax.set_title('Stance Effectiveness in UFC Fights')
ax.legend()

plt.tight_layout()
plt.show()
```

### Prediction Models

1. Fight Outcome Predictor:
   - Features: Fighter stats, physical attributes, and career metrics
   - Target: Winner

2. Fight Duration Predictor:
   - Features: Fighter stats, weight class, fight type
   - Target: last_round and last_round_time

Example code outline for Fight Outcome Predictor:

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load and preprocess data
ufc_data = pd.read_csv('ufc_data.csv')

# Select features and target
features = ['R_KD', 'R_SIG_STR_pct', 'R_TD_pct', 'R_SUB_ATT', 
            'B_KD', 'B_SIG_STR_pct', 'B_TD_pct', 'B_SUB_ATT',
            'R_Stance', 'B_Stance', 'R_age', 'B_age', 'weight_class']
X = ufc_data[features]
y = ufc_data['Winner']

# Encode categorical variables
X = pd.get_dummies(X, columns=['R_Stance', 'B_Stance', 'weight_class'])

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")

# Feature importance
for feature, importance in zip(X.columns, model.feature_importances_):
    print(f"{feature}: {importance:.4f}")
```

This structure provides a comprehensive overview of the UFC dataset and outlines potential areas for analysis and model development.
