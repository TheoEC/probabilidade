import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

y_axis = [40, 80, 10, 50]
x_axis = range(len(y_axis)) 
width_n = 0.5
bar_color = 'yellow'

plt.bar(x_axis,  y_axis, width = width_n, color =  'r')