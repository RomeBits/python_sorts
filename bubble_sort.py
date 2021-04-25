# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 13:40:25 2021

@author: benja
"""
import matplotlib.pyplot as plt
import random

N = 10
X = list(range(N))
to_sort = list(X)

random.shuffle(to_sort)
unsorted = list(to_sort)


"""
Loop through the array and swap elements in the wrong spot
var: array, the array to loop through and sort 
"""
def bubble(array):
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]: 
            array[i], array[i + 1] = array[i + 1], array[i]


"""
Check if the array is sorted
var: array, the array to check
"""
def check(array):
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            return False
    return True

while(not check(to_sort)):
    bubble(to_sort)
    
plt.subplot(211)
plt.bar(X, unsorted)
plt.subplot(212)
plt.bar(X, to_sort)
plt.show()
