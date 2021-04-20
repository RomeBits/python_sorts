# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 13:40:25 2021

@author: benja
"""

import matplotlib.pyplot as plt

numbers = list(range(10))
to_sort = [1,7,5,2,8,3,6,9,4,0]
plt.bar(numbers, to_sort)

plt.show()