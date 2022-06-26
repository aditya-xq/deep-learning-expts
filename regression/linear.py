# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 18:34:01 2022

@author: adity
"""
# Linear regression in Keras

#%%

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Make NumPy printouts easier to read.
np.set_printoptions(precision=3, suppress=True)

#%%

import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers

print(tf.__version__)

#%%

