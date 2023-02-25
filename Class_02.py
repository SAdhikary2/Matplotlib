#MATPLOTLIB LEARNING TUTORIAL 02
import numpy as np
from matplotlib import pyplot as plt
plt.style.use('fivethirtyeight')

ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

#for creating indiviual bar
X_indexes=np.arange(len(ages_x))
width=0.25



dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]
plt.bar(X_indexes-width, dev_y, color="#444444",linewidth=1,width=width, label="All Devs")


py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]
plt.bar(X_indexes, py_dev_y, color="#008fd5",width=width, label="Python")

js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]
plt.bar(X_indexes+width, js_dev_y, color="#e5ae38", width=width,label="JavaScript")


plt.legend()
#to name all the x axis
plt.xticks(ticks=X_indexes,labels=ages_x)
plt.title("Median Salary (USD) by Age")
plt.xlabel("Ages")
plt.ylabel("Median Salary (USD)")

plt.tight_layout()
plt.savefig('plot2.png')
plt.show()