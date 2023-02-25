#Data extraction from the csv data set and making by this a bar chart
import csv
import numpy as np
import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt
plt.style.use('fivethirtyeight')
width=0.25

data=pd.read_csv('Salary_dataset.csv')
Exps=data['YearsExperience']
salary=data['Salary']

plt.bar(Exps,salary,width=width)






plt.legend()
plt.xticks(ticks=Exps,labels=Exps)
plt.title("Salary By Experience")
plt.xlabel('Salary')
plt.ylabel('Experience')
plt.tight_layout()
plt.show()