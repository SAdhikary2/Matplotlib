#Plotting the time series data
#working with the data and matplotlib

import pandas as pd
from datetime import datetime,timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates

plt.style.use('seaborn')

"""
dates=[
    datetime(2019,5,24),
    datetime(2019,5,25),
    datetime(2019,5,26),
    datetime(2019,5,27),
    datetime(2019,5,28),
    datetime(2019,5,29),
    datetime(2019,5,30)
    
]

y=[0,1,3,4,5,6,7]

plt.plot_date(dates,y,linestyle='solid')

#To rotate the date format
plt.gcf().autofmt_xdate()

#to formatting the date
date_format=mpl_dates.DateFormatter('%b,%d %y')
plt.gca().xaxis.set_major_formatter(date_format)

"""

#play with dataset means a csv file
data=pd.read_csv('data3.csv')

# To replace a date range wise 
data['Date'] = pd.to_datetime(data['Date'])
data.sort_values('Date', inplace=True)

price_date=data['Date']
price_close=data['Close']

plt.plot_date(price_date,price_close,linestyle='solid')
plt.gcf().autofmt_xdate()

plt.title('Bitcoin Price')
plt.savefig('class9_pic.png')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.tight_layout()
plt.show()