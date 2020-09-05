from matplotlib import pyplot as plt
import numpy as np
import csv
from collections import Counter
import pandas as pd
'''
with open('file.csv','a') as c:
    csv_writer=csv.writer(c)
    csv_writer.writerow(['name','place'])
    c.close()
c=Counter()

data=pd.read_csv('file.csv')
languages_panda=data['LanguagesWorkedWith']


for languages in languages_panda:

   languages_list=languages.split(';')
   c.update(languages_list)
#print c.most_common(4)

language_x_axis=[]
language_no_y_axis=[]

for i in c.most_common(10):
    language_x_axis.append(i[0])
    language_no_y_axis.append(i[1])

#  bar

plt.style.use('fivethirtyeight')
plt.barh(language_x_axis,language_no_y_axis)
plt.xlabel('language statitics')
plt.tight_layout()
plt.show()


#x_val=[25,26,27,28,29,30,31,32,33,34,35]
#x_index=np.arange(len(x_val))
#width=0.35

#y_val=[38400,42000,46700,49300,53200,56000,63216,64900,67317,68748,73752]

plt.xlabel('ages')
plt.ylabel('salary')
plt.style.use('fivethirtyeight')
#print(plt.style.available)
#plt.xkcd()
plt.bar(x_index,y_val,width=width,label='normal')

y_val_new=[45300,48876,53850,57200,63016,65899,70003,70000,71960,75370,83640]

plt.bar(x_index+width,y_val_new,width=width,label='python')
plt.xticks(x_index+width/2,x_val)
plt.title('graph')
plt.legend()

plt.tight_layout()
plt.grid(True)

#plt.savefig('plot.png')
plt.show()

'''
'''
#pie

slices=[59219,55466,47544,36443,35917]
labels=['JavaScript','HTML/CSS','SQL','Python','Java']

explode=[0,0,0,0.1,0] # to pull out certain slice slightly outword

plt.pie(slices,labels=labels,shadow=True,wedgeprops={'edgecolor':'orange','linewidth':3},explode=explode,autopct='%1f')
plt.title('My Cool Pie')


plt.style.use('fivethirtyeight')
plt.tight_layout()
plt.show()'''

'''
#stack plots

minutes=[1,2,3,4,5,6,7,8,9]
player1=[1,2,3,3,4,4,4,4,5]
player2=[1,1,1,1,2,2,2,3,4]
player3=[1,1,1,2,2,2,3,3,3]

labels=['player1','player2','player3']

plt.stackplot(minutes,player1,player2,player3,labels=labels)

plt.legend(loc='upper left')
plt.style.use('fivethirtyeight')
plt.tight_layout()
plt.show()

'''
'''
#plotfile(area in linegraph)

age=[25,26,27,28,29,30,31,32,33,34,35]
other_languages=[38400,42000,46700,49300,89000,56000,63216,64900,67317,68748,73752]
python=[45300,30000,53850,57200,63016,65899,70003,70000,71960,32000,83640]

plt.plot(age,other_languages,label='other languages')
plt.plot(age,python,label='python')
plt.fill_between(age,python,other_languages,where=(python>other_languages),color='red',interpolate=True,alpha=0.23)
plt.fill_between(age,other_languages,python,where=(python<=other_languages),interpolate=True,color='green',alpha=0.23)
plt.style.use('fivethirtyeight')
plt.legend()
plt.tight_layout()
plt.show()
'''