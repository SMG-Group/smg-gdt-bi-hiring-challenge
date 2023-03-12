import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import colors as mcolors
import numpy as np 

colors = {0: ['#7CB9E8'],
1: [ '#00308F'],
2: ['#72A0C1'],
3: ['#1CAC78'],
4: ['#fd5c63', '#FBCEB1', '#A52A2A', '#FF7F50'],
5: ['#F0E68C', '#FFC72C', '#87A96B', '#4B6F44'],
6: ['#DDA0DD', '#662d91', '#E6E6FA', '#EE82EE']}

plt.rcParams["figure.figsize"] = [10.00, 10.50]
plt.rcParams["figure.autolayout"] = True
df = pd.read_csv("answer_q02_1.csv", delimiter=';', header = 0)

print(df)

df['row_number_by_group']=df.groupby(['Platform']).ngroup() + 1
print(df)


colors1 = []
for value in df.row_number_by_group: 
    colors1.append(colors.get(value)[0])

plt.barh(df.Products, df.Sales, color  = colors1)
for i, v in enumerate(df.Sales):
    plt.text(v, i, " "+str(v), color='gray', va='center')
 

plt.show()

