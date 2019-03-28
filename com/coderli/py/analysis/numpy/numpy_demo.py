# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 09:13:20 2019

@author: lihongzhe
"""
#%%
import numpy as np
np_arr = np.array([[1,2,3],[4,5.6,7],[9,8,3]])
int_arr = np_arr.astype(np.int32)
#%%
np_arr.shape
#%%
np_arr.dtype
#%%
np_empty = np.empty((2,3,4))
np_empty
#%%
float_arr = np.arange(5,dtype = "float64")
float_arr
#%%
#astype 一定会创建新的数组而不是改变原有数组
float_arr.astype(np.int64)
#%%
int_arr + int_arr
#%%
int_arr * int_arr
#%%
int_arr * 2
#%%
int_arr[0,1]
#%%
int_arr[0,0] = 2
int_arr
#%%
arr = np.arange(32).reshape((8,4))
arr[[1,2,3,0],[3,1,2,0]]
#%%
arr
#%%
arr[[1,2,3,0]][:,[1,2,0,3]]
#%%
arr[np.ix_([0,1],[1,0])]
#%%
np.dot(arr.T,arr)
np.meshgrid(np.array([1,2]),np.array([3,4]))
