
import pandas as pd
from scipy.io import arff

# Load ARFF file
data, meta = arff.loadarff('Leukemia.arff')

# Convert to DataFrame
df = pd.DataFrame(data)

# Write DataFrame to Excel
df.to_excel('Leukemia.xlsx', index=False)
