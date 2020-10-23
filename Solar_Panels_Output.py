import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel('solar_data.xlsx', 'June 7th')
new_df = df.drop(columns=['Time', 'solar model'])
df500 = new_df[new_df > 500]
mean_df = df500.mean(axis=0)
std_df = df500.std(axis=0)
mean_df = mean_df.reset_index(name="Mean")
std_df = std_df.reset_index(name="STD")

print mean_df
print std_df

mean_df['Mean'].hist(bins=100)
plt.title("Mean of values above 500")
plt.xlabel("Mean Values", fontsize=15)
plt.ylabel("Number of Values", fontsize=15)
plt.show()

std_df['STD'].hist(bins=100)
plt.title("STD of values above 500")
plt.xlabel("STD Values", fontsize=15)
plt.ylabel("Number of Values", fontsize=15)
plt.show()

#sns.barplot(x=mean_df.index, y=mean_df.Mean)
#plt.show()
#sns.barplot(x=std_df.index, y=std_df.STD)
#plt.show()
