#Making Histogram of the dataset

import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

ages = [18, 19, 21, 25, 26, 26, 30, 32, 38, 45, 55]
bins=[10,20,30,40,50,60]# bins are here the frequency classes
plt.hist(ages,bins=bins,edgecolor='black',log=True)
#to represent data in logarithamic scale write log=True

# data = pd.read_csv('data.csv')
# ids = data['Responder_id']
# ages = data['Age']

#To mark yje median age as a line
median_age = 26
color = '#fc4f30'
plt.axvline(median_age,color=color,label='Median Age',linewidth=2)
plt.legend()

plt.title('Ages of Respondents')
plt.xlabel('Ages')
plt.ylabel('Total Respondents')

plt.tight_layout()

plt.show()