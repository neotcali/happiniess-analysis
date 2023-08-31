import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.api.types import CategoricalDtype

    # some logic

# Load the cleaned data
data = pd.read_csv('./data/cleaned_world-happiness-report.csv')

print(data.columns)

# Histogram
plt.hist(data['Happiness Score'])
plt.title('Distribution of Happiness Scores')
plt.xlabel('Score')
plt.ylabel('Number of Countries')
plt.show()

# Scatter plot
sns.scatterplot(data=data, x='Happiness Score', y='Economy (GDP per Capita)')
plt.title('Happiness Score vs. GDP per Capita')
plt.show()

# Other visualizations...
