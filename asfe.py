import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from tqdm import tqdm
import warnings
warnings.filterwarnings("ignore")

# load train and test features
train_df = pd.read_csv("./train_features.csv")
test_df = pd.read_csv("./test_features.csv")

data_df = pd.concat([train_df,test_df],axis=0,ignore_index=True)

group_feats = []

# top-k features
features = ['median','xr','mean','Quartile_75','std','form_factor','Quartile_25','Quartile','Skewness','par']

# adaptive feature aggregation and crosses
for f in tqdm(features):
    data_df['cavitation_{}_median'.format(f)] = data_df.groupby(['valve_opening','upstream_pressure'])[f].transform('median')
    data_df['cavitation_{}_mean'.format(f)] = data_df.groupby(['valve_opening','upstream_pressure'])[f].transform('mean')
    data_df['cavitation_{}_max'.format(f)] = data_df.groupby(['valve_opening','upstream_pressure'])[f].transform('max')
    data_df['cavitation_{}_min'.format(f)] = data_df.groupby(['valve_opening','upstream_pressure'])[f].transform('min')

    group_feats.append('cavitation_{}_median'.format(f))
    group_feats.append('cavitation_{}_mean'.format(f))
    group_feats.append('cavitation_{}_max'.format(f))
    group_feats.append('cavitation_{}_min'.format(f))

for f1 in tqdm(features + group_feats):
    for f2 in features + group_feats:
        if f1 != f2:
            colname1 = '{}_{}_ratio'.format(f1,f2)
            data_df[colname1] = data_df[f1].values/data_df[f2].values
            colname2 = '{}_{}_subtraction'.format(f1,f2)
            data_df[colname2] = data_df[f1].values-data_df[f2].values
data_df = data_df.fillna(method='bfill')

del data_df['valve_opening']
del data_df['upstream_pressure']
train_count = train_df.shape[0]
train_df = data_df[:train_count].copy().reset_index(drop=True)
test_df = data_df[train_count:].copy().reset_index(drop=True)

train_df.to_csv("./train_feature_transform.csv",index=False)
test_df.to_csv("./test_feature_transform.csv",index=False)









