# Making Scatter Plot

import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('seaborn')

#reading/fetching the data
data = pd.read_csv('data2.csv')
view_count = data['view_count']
likes = data['likes']
ratio = data['ratio']

#Working with the csv file
plt.scatter(view_count, likes ,edgecolors='black',linewidths=1,c=ratio,cmap='summer',alpha=0.75)

cbar=plt.colorbar()
cbar.set_label('Likes/Dislikes Ratio')

#To transfer in to the logarithm scale
plt.xscale('log')
plt.yscale('log')







#basic data
"""x = [5, 7, 8, 5, 6, 7, 9, 2, 3, 4, 4, 4, 2, 6, 3, 6, 8, 6, 4, 1]
y = [7, 4, 3, 9, 1, 3, 2, 5, 2, 4, 8, 7, 1, 6, 4, 9, 7, 7, 5, 1]

colors = [7, 5, 9, 7, 5, 7, 2, 5, 3, 7, 1, 2, 8, 1, 9, 2, 5, 6, 7, 5]
sizes = [209, 486, 381, 255, 191, 315, 185, 228, 174,
       538, 239, 394, 399, 153, 273, 293, 436, 501, 397, 539]"""

# plt.scatter(x,y,s=50,c='green',marker='x')
#To Change The Size of dot used s=sizer_value
#To change the color of dot we use c=color_name
# plt.scatter(x,y,s=50,c='green',edgecolors='black',linewidths=1,alpha=0.75)

# plt.scatter(x,y,s=sizes,c=colors,cmap='Oranges_r',edgecolors='black',linewidths=1,alpha=0.75) #To change the color of dot here used cmap
#we can s=size_value here directly

#To mark down the dot
# cbar=plt.colorbar()
# cbar.set_label('Satisfaction')








plt.title('Trending YouTube Videos')
plt.xlabel('View Count')
plt.ylabel('Total Likes')
plt.savefig('Scatter_plot.png')
plt.tight_layout()

plt.show()