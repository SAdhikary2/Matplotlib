from matplotlib import pyplot as plt
plt.style.use('fivethirtyeight')

slices=[10,30,60,40]
label=['ten','thirty','sixty','fourty']
#for passing the color
color=['white','red','green','yellow']
plt.pie(slices,labels=label,colors=color,wedgeprops={'edgecolor':'black'})





plt.title("My Awesome Piechart")
plt.tight_layout()
plt.show()