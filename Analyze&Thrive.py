# 1. Importing Essential Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 2. Loading Data into a DataFrame
df = pd.read_csv('data.csv')

# 3. Basic Dataframe Information
df.info()

# 4. Descriptive Statistics
df.describe()

# 5. Handling Missing Values
df = df.fillna(method='ffill')

# 6. Data Filtering
filtered_data = df[df['column_name'] > value]

# 7. Grouping and Aggregating Data
grouped_data = df.groupby('column_name').agg(np.mean)

# 8. Data Visualization with Matplotlib
plt.hist(df['numerical_column'])
plt.title('Histogram of Numerical Data')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

# 9. Creating a New Feature from Existing Data
df['new_column'] = df['column1'] / df['column2']

# 10. Saving Processed Data to a New CSV
df.to_csv('processed_data.csv', index=False)

# 11. Basic Linear Regression Model
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(df[['independent_var']], df['dependent_var'])
predictions = model.predict(df[['independent_var']])

# 12. Correlation Matrix
correlation_matrix = df.corr()

# 13. Time Series Analysis with Pandas
timeseries = df['date_column'].resample('M').mean()

# 14. Data Cleaning with Regular Expressions
import re
df['cleaned_text'] = df['text_column'].apply(lambda x: re.sub(r'\W+', '', x))

# 15. Pivot Tables for Data Summarization
pivot_table = df.pivot_table(values='data_column', index='category_column', columns='date_column')

