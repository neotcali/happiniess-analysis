import pandas as pd

# Load the data
data = pd.read_csv('./data/2015.csv')

# Inspect the first few rows
print(data.head())

# Handle missing values, drop or impute
data.dropna(inplace=True)

# Save cleaned data
data.to_csv('./Data/cleaned_world-happiness-report.csv', index=False)
