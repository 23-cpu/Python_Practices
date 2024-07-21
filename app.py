import matplotlib.pyplot as plt
import pandas as pd

# Create a sample data frame to mimic the trend over years
data = {
    'Year': [2010, 2012, 2014, 2016, 2018, 2020, 2022, 2024],
    'Functional Bugs Detection': [60, 65, 70, 75, 78, 80, 82, 85],
    'Transient Execution Vulnerabilities Detection': [5, 7, 10, 12, 15, 18, 20, 22]
}

df = pd.DataFrame(data)

# Plotting the time series graph
plt.figure(figsize=(10, 6))

plt.plot(df['Year'], df['Functional Bugs Detection'], marker='o', label='Functional Bugs Detection', color='blue')
plt.plot(df['Year'], df['Transient Execution Vulnerabilities Detection'], marker='o', label='Transient Execution Vulnerabilities Detection', color='orange')

# Adding labels and title
plt.xlabel('Year')
plt.ylabel('Adoption Rate (%)')
plt.title('Adoption of Pre-Silicon Verification Techniques Over Time')
plt.legend()

# Save as PNG
plt.savefig('/mnt/data/pre_silicon_verification_time_series.png')
plt.show()
