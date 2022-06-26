# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 18:03:09 2022

@author: adity
"""

#%%

# Create a 2d array in tensorflow

import tensorflow as tf

a = tf.constant([[1., 2., 3.],
                 [4., 5., 6.]])

print(a)
print(a.shape)
print(a.dtype)

#%%
# Find max per row

for i in a:
	print(max(i))

#%%

# Arthemetic with tensors

x1 = [1, 2, 3, 4]
y1 = [1]
print("Normal concatenattion: ", x1 + y1)
print("Tensor addition: ", tf.add(x1, y1))

#%%
# Adding tensor with a list
x2 = tf.constant([1, 2, 3, 4])
y2 = [1, 2, 3, 4]
print(x2 + y2)
y2 = tf.constant([1, 2, 3, 4])
print(x2 + y2)

#%%
