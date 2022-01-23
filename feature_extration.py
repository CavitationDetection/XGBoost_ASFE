import os 
import scipy.io as scio
import math
from scipy import stats
import numpy as np
import pandas as  pd
import matplotlib.pyplot as plt
import math
import csv
import warnings
warnings.filterwarnings("ignore")
'''
1. Central Trend Statistics:
   --- mean 
   --- median
   --- low quartile
   --- upper quartile
2. Dispersion Degree Statistics:
   --- minimum
   --- maximum
   --- inter quartile range
   --- standard deviation
   --- root mean square
   --- square root amplitude
3. Distribution Shape Statistics
   --- kurtosis
   --- skewness
   --- shape factor
   --- clearance shape
   --- crest factor
'''

path = "/TestSplitFFT"
file_name = os.listdir(path)
file_name.sort(key=lambda x:int(x.split('.')[0]))

feature_list = []
for info in file_name:
   domain = os.path.abspath(path)
   info = os.path.join(domain,info)
   data = pd.read_csv(info,header=None)

   # central trend statistics
   data_mean = np.mean(data)
   data_median = data.median()
   data_quartile_025 = data.quantile(0.25)
   data_quartile_075 = data.quantile(0.75)

   # dispersion degree statistics
   data_Minimum = np.min(data)
   data_Maximum = np.max(data)
   data_quartile = data_quartile_075 - data_quartile_025
   data_std = np.std(data)
   data_rms = np.sqrt((np.mean(data**2)))
   data_sra = (np.sum(np.sqrt(np.abs(data)))/len(data))**2

   # distribution shape statistics
   data_kurtosis = data.kurt()
   data_skew = data.skew()

   data_avg = np.mean(np.abs(data))
   data_ff = data_rms / data_avg

   data_clf = np.max(np.abs(data)) / data_sra
   data_cf = np.max(np.abs(data)) / data_rms
   
   feature_list = [data_mean, data_median, data_quartile_025, data_quartile_075, data_Maximum, data_Minimum, data_quartile, data_std, data_rms, data_sra, data_kurtosis, data_skew, data_ff, data_clf, data_cf]
   feature_list = pd.DataFrame(data=feature_list).T
   feature_list.to_csv("./test_features.csv",sep=',',mode='a',index=False,encoding='utf-8',header=None)
print("Work Done")
      


































