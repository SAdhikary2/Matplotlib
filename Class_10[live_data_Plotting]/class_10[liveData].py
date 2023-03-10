#Plotting Live Data in The Real Time


import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

x_vals = []
y_vals = []

#returns the number of element in the speccified list
index = count()

def animate(i):
    # x_vals.append(next(index))
    # y_vals.append(random.randint(0,5))

    data=pd.read_csv('data4.csv')
    x=data['x_value']
    y1=data['total_1']
    y2=data['total_2']

    plt.cla()# To fixed the same color of the plot
    plt.plot(x,y1,label='Channel 1')
    plt.plot(x,y2,label='channel 2')
    plt.legend(loc='upper left')
    plt.tight_layout()

ani=FuncAnimation(plt.gcf(),animate,interval=1000) #to generate the live plot animated pot

plt.tight_layout()
plt.savefig('live_data.png')
plt.show()

