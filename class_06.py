# Finding The Area on The Line Plots

import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv('data1.csv')
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

plt.plot(ages, dev_salaries, color='#444444',
         linestyle='--', label='All Devs')

plt.plot(ages, py_salaries, label='Python')

overall_median = 57287

#To fill a particular area
#plt.fill_between(ages,py_salaries,overall_median,alpha=0.25)


# salary greater than overall range
plt.fill_between(ages,py_salaries,overall_median,where=(py_salaries>overall_median),interpolate=True,label='Above overall salary of py_dev',alpha=0.25)
#To change the color density we are using the alpha

# salary lesser than ovreall range
plt.fill_between(ages,py_salaries,overall_median,where=(py_salaries <= overall_median),interpolate=True,color='red',label='below overall salary of py_dev',alpha=0.25)

#To check python developer salary difference from the other developer salary
plt.fill_between(ages,py_salaries,dev_salaries,where=(py_salaries>dev_salaries),interpolate=True,color='green',label='high salary of py_dev from other dev',alpha=0.55)


plt.legend()
plt.savefig('final_salary_stats.png')
plt.title('Median Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')

plt.tight_layout()

plt.show()