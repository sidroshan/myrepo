import pandas as pd

# Load the dataset
file_path = 'path_to_your_file/Datasets.csv'
data = pd.read_csv(file_path)

# Display the first 10 rows of the dataset
print(data.head(10))
