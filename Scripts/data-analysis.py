import pandas as pd

# Load the cleaned data
data = pd.read_csv('./data/cleaned_world-happiness-report.csv')

# Correlation Analysis
numeric_data = data.select_dtypes(include=['float64', 'int64'])
correlation_matrix = numeric_data.corr()
print(correlation_matrix)

# Other statistical analyses...
