import pandas as pd
from scipy.io import arff

# Load ARFF file
data, meta = arff.loadarff('Breast.arff')

# Convert to DataFrame
df = pd.DataFrame(data)

# Write DataFrame to CSV
df.to_csv('Breast.csv', index=False)
