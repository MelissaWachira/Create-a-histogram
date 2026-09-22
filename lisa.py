import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Generate realistic synthetic age data (500 samples, mean age ~35)
np.random.seed(42)
ages = np.random.normal(loc=35, scale=12, size=500).astype(int)
ages = np.clip(ages, 18, 75)  # Keep ages between 18 and 75

# Create a DataFrame
data = pd.DataFrame({'Age': ages})

# Create the histogram
data['Age'].hist(bins=15, color='green', edgecolor='black')

# Add labels and title
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Histogram of Age')

# Display the histogram
plt.show()
