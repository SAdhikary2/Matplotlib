from matplotlib import pyplot as plt
plt.style.use('fivethirtyeight')

# slices=[10,30,60,40]
# label=['ten','thirty','sixty','fourty']
# #for passing the color
# color=['Blue','red','green','yellow']
# plt.pie(slices,labels=label,colors=color,wedgeprops={'edgecolor':'black'})

#Another data

# Language Popularity
# slices = [59219, 55466, 47544, 36443, 35917, 31991, 27097, 23030, 20524, 18523, 18017, 7920, 7331, 7201, 5833]
# labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java', 'Bash/Shell/PowerShell', 'C#', 'PHP', 'C++', 'TypeScript', 'C', 'Other(s):', 'Ruby', 'Go', 'Assembly']
# plt.pie(slices,labels=labels,wedgeprops={'edgecolor':'black'})



slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
#To do tha explode means slice a part in pie chart
explode=[0,0,0,0.2,0]
plt.pie(slices,labels=labels, explode=explode, shadow=True, autopct='%1.2f%%',startangle=90, wedgeprops={'edgecolor':'black'})
# Shadow =True used for the making 3d of pie chart
# To move the slice part according the angle we write startangle= angle 
#To give percentage value at every slice we use autopct='%1.2f%%'





plt.title("My Awesome Piechart")
plt.savefig('piechart.png')
plt.tight_layout()
plt.show()