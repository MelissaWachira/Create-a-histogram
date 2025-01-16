import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_excel('data.xlsx')

# Create the histogram
data['Age'].hist(bins=15, color='green', edgecolor='black')

# Add labels and title
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Histogram of Age')

# Display the histogram
plt.show()