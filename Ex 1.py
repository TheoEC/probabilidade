import pandas as pd

import numpy as np

import matplotlib.pyplot as plt



y_axis = [20, 15, 31, 20]

x_axis = np.arange(1) 
plt
width_n = 0.5

bar_color = 'yellow'


plt.bar(x_axis,  y_axis[0], width = width_n, color =  'r', label = 'funcionarios sem acidentes')
plt.bar(x_axis+0.6,  y_axis[1], width = width_n, color =  'b', label = 'funcionarios  com mais de 4 acidentes')
plt.bar(x_axis+1.2,  y_axis[2], width = width_n, color =  'g', label = 'funcionarios com mais de 1 e ate 4 acidentes')
plt.bar(x_axis+1.8,  y_axis[3], width = width_n, color =  'y', label = 'funcionarios com mais de 2 e ate 5 acidentes')

plt.legend()