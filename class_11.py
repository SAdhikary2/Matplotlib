# Subplot Tutorial in Matplotlib

import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('seaborn')

data = pd.read_csv('data1.csv')
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

fig1,ax1=plt.subplots()
fig2,ax2=plt.subplots()

#This method for subplots in one frame
# fig,(ax1,ax2)=plt.subplots(nrows=1,ncols=2,sharex=True)

ax1.plot(ages,dev_salaries,linestyle='--',label='All Devs')

ax2.plot(ages,py_salaries,label='Python')
ax2.plot(ages,js_salaries,label='JavaScript')

ax1.legend()
ax1.set_title('Median salary (USD) by Age')
ax1.set_ylabel('Median salary(USD)')

ax2.legend()
ax2.set_xlabel('Ages')
ax2.set_ylabel('Median salary(USD)')

plt.tight_layout()
fig1.savefig('fig1.png')
fig2.savefig('fig2.png')
plt.show()