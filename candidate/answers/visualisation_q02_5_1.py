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

plt.rcParams["figure.figsize"] = [15.00, 15.50]
plt.rcParams["figure.autolayout"] = True
df = pd.read_csv("answer_q02_6.csv", delimiter=';', header = 0)
df2=df.groupby(['date_key']).size().reset_index(name='counts') 
final_df2 = df2.sort_values('date_key')
#df.groupby(['date_key']).count().reset_index(name='counts')
plt.plot(final_df2.date_key, final_df2.counts)
plt.xticks(rotation=90)
plt.title('All Listings Per day')
plt.xlabel('Date')
plt.ylabel('# Listings')
plt.show()

df3=df[df['status_id'] == 10].groupby(['date_key']).size().sort_values(ascending=True).reset_index(name='actives')  
#df.groupby(['date_key']).count().reset_index(name='counts')
final_df3 = df3.sort_values('date_key')
plt.plot(final_df3.date_key, final_df3.actives)
plt.xticks(rotation=90)
plt.title('Active Listings Per day')
plt.xlabel('Date')
plt.ylabel('# Listings')
plt.show()
