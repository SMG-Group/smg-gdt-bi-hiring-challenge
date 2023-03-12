import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import colors as mcolors
import numpy as np 

colors = {0: ['#7CB9E8'],
1: [ '#00308F'],
2: ['#72A0C1'],
3: ['#1CAC78'],
4: ['#fd5c63'],
5: ['#FBCEB1'],
6: ['#A52A2A'],
7: ['#FF7F50'],
8: ['#F0E68C'],
9: ['#FFC72C'],
10: ['#87A96B'],
11: ['#4B6F44'],
12: ['#DDA0DD'],
13: ['#662d91'],
14: ['#E6E6FA'],
15: [ '#EE82EE'],
16: [ '#00308F'],
17: ['#72A0C1'],
18: ['#1CAC78'],
19: ['#fd5c63'],
20: ['#FBCEB1'],
21: ['#A52A2A'],
22: ['#FF7F50'],
23: ['#F0E68C'],
24: ['#FFC72C'],
25: ['#87A96B'],
26: ['#4B6F44'],
27: ['#DDA0DD'],
28: ['#662d91'],
29: ['#E6E6FA'],
30: [ '#EE82EE']
}

plt.rcParams["figure.figsize"] = [10.00, 10.50]
plt.rcParams["figure.autolayout"] = True
df = pd.read_csv("answer_q02_4.csv", delimiter=';', header = 0)

print(df)

df['row_number_by_group']=df.groupby(['Products']).ngroup() + 1
print(df)


colors1 = []
for value in df.row_number_by_group: 
    colors1.append(colors.get(value)[0])

plt.barh(df.Products, df.Sold, color  = colors1)
#plt.barh(df.Products, df.Number_Of_Working_Days, color  = colors1)
for i, v in enumerate(df.Sold):
    plt.text(v, i, " "+str(v), color='gray', va='center')
 

plt.show()