# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 13:40:25 2021

@author: benja
"""
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random
import matplotlib as mp

N = 50
X = list(range(N))
to_sort = list(X)

random.shuffle(to_sort)
unsorted = list(to_sort)

"""
Check if the array is sorted
var: array, the array to check
"""
def check(array):
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            return False
    return True



def bubble(array):
    for j in range(len(array) - 1):
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]: 
                array[i], array[i + 1] = array[i + 1], array[i]
            yield array

"""
CODE CREDIT:  https://www.geeksforgeeks.org/insertion-sort-visualization-using-matplotlib-in-python/
The visualization of the sorting was taken from this link, as the goal for
    this project was to build working sorts, not data visualization
"""
generator = bubble(to_sort) 
data_normalizer = mp.colors.Normalize()
color_map = mp.colors.LinearSegmentedColormap(
    "my_map",
    {
        "red": [(0, 1.0, 1.0),
                (1.0, .5, .5)],
        "green": [(0, 0.5, 0.5),
                  (1.0, 0, 0)],
        "blue": [(0, 0.50, 0.5),
                  (1.0, 0, 0)]
    }
)

fig, ax = plt.subplots()
rects = ax.bar(range(len(to_sort)), to_sort, align="edge", 
                color = color_map(data_normalizer(range(N))))

ax.set_xlim(0, N)
ax.set_ylim(0, int(1.1*N))
text = ax.text(0.01, 0.95, "", transform=ax.transAxes)
iteration = [0]

def animate(to_sort, rects, it):
    for rect, val in zip(rects, to_sort):
        rect.set_height(val)
        
    iteration[0] += 1
    text.set_text("iterations : {}".format(iteration[0]))
    
anim = FuncAnimation(fig, func=animate,
                      fargs=(rects, iteration), frames=generator, interval=50,
                      repeat=True, save_count=N*N)

plt.show()
anim.save("50_points.mp4")
