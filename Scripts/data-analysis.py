import pandas as pd

# Load the cleaned data
data = pd.read_csv('./data/cleaned_world-happiness-report.csv')

# Correlation Analysis
correlation_matrix = data.corr()
print(correlation_matrix)

# Other statistical analyses...
