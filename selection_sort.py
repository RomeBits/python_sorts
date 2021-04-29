# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 19:13:51 2021

@author: benja
"""
import matplotlib.pyplot as plt
import random

N = 10000
X = list(range(N))
to_sort = list(X)

random.shuffle(to_sort)
unsorted = list(to_sort)