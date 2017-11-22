# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 11:02:27 2017

@author: IFPB
"""

import pandas as np
import numpy as np
import matplotlib.pyplot as plt

y = [100, 12, 44]
x = np.arange(1)
espacamento = 0.5
cor = 'red'

plt.bar(x, y[0], width = espacamento, color = 'y', label = 'total de pessoas')
plt.bar(x + 0.6, y[1], width = espacamento, color = 'r', label = '% de pessoas com mais de 5 acidentes(12%)')
plt.bar(x + 1.2, y[2], width = espacamento, color = 'b', label = '% de pessoas entre 2 e 4 acidentes(44%)')

plt.legend()