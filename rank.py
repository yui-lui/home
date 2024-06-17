from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

rank=pd.read_csv('rank.csv')

x=rank['Character']
y=rank['Votes']
barcol=['lightblue','#fae678','#bfb5eb','#65a673','firebrick','lightpink','#a8e6db','wheat','steelblue','black']
font = {'family' : 'monospace',
        'weight' : 50}

plt.rc('font', **font)
plt.show()
plt.xlabel('Character',size=18)
plt.ylabel('Votes(millions)',size=18)
plt.bar(x,y,color=barcol)
plt.ylim([0,4500000])
plt.title('Sanrio Character Ranking 2023',size=24)
plt.show()


