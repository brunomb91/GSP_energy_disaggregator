#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This implements GSP energy disaggregation method proposed in the paper "On a training-less solution for non-intrusive appliance load monitoring using graph signal processing"

Created on Thu Feb  1 15:42:41 2018

@author: haroonr
"""
from __future__ import division
import warnings
warnings.filterwarnings("ignore")
import pandas as pd
import gsp_support as gsp
import matplotlib.pyplot as plt
import numpy as np
import time
from collections import OrderedDict

print("1 of 6> reading data")

# Datasets files
# REDD House 1
#csvfileaggr = "../Data/REDD/house_1/house1_aggr.csv"
#csvfiledisaggr = "../Data/REDD/house_1/house1_disaggr.csv"

# REDD House 2
#csvfileaggr = "../Data/REDD/house_2/house2_aggr2.csv"
#csvfiledisaggr = "../Data/REDD/house_2/house2_disaggr.csv"

# REDD House 6
#csvfileaggr = "../Data/REDD/house_6/house6_aggr.csv"
#csvfiledisaggr = "../Data/REDD/house_6/house6_disaggr.csv"

#REFIT House 8
csvfileaggr = "../Data/REFIT/house8_aggr.csv"
csvfiledisaggr = "../Data/REFIT/house8_disaggr.csv"

# Demo files
#csvfileaggr = "./output_aggr.csv"
#csvfiledisaggr = "./output_disaggr.csv"

df = pd.read_csv(csvfileaggr, index_col = "Time") # read demo file with aggregated active power
df.index = pd.to_datetime(df.index)
dfd = pd.read_csv(csvfiledisaggr, index_col = "Time") # read file with ground truth disaggregated appliances
dfd.index = pd.to_datetime(dfd.index)

# REDD House 1
#dfd_house1 = pd.DataFrame()
# 
#dfd_house1['refrigerator'] = dfd['refrigerator']
#dfd_house1['dishwasher'] = dfd['dishwasher']
#dfd_house1['kitchen_outlets'] = dfd['kitchen_outlets']
#dfd_house1['lighting'] = dfd['lighting']
#dfd_house1['washer_dryer'] = dfd['washer_dryer']
#dfd_house1['bathroom_gfi'] = dfd['bathroom_gfi']
#dfd_house1['microwave'] = dfd['microwave']
#dfd_house1['oven'] = dfd['oven']
#
#dfd_house1.index = pd.to_datetime(dfd_house1.index)

# REDD House 2
#dfd_house2 = pd.DataFrame()
#
#dfd_house2['microwave'] = dfd['microwave']
#dfd_house2['kitchen_outlets'] = dfd['kitchen_outlets']
#dfd_house2['kitchen_outlets2'] = dfd['kitchen_outlets2']
#dfd_house2['stove'] = dfd['stove']
#dfd_house2['refrigerator'] = dfd['refrigerator']
#dfd_house2['dishwasher'] = dfd['dishwasher']
#dfd_house2['lighting'] = dfd['lighting']
#
#dfd_house2.index = pd.to_datetime(dfd_house2.index)

# REDD House 6
#dfd_house6 = pd.DataFrame()
#
##dfd_house6['microwave'] = dfd['microwave']
#dfd_house6['kitchen_outlets'] = dfd['kitchen_outlets']
#dfd_house6['stove'] = dfd['stove']
#dfd_house6['refrigerator'] = dfd['refrigerator']
#dfd_house6['electronics'] = dfd['kitchen_outlets2']
#dfd_house6['electric_heat'] = dfd['electric_heat']
#dfd_house6['air_conditioning'] = dfd['air_conditioning']
#dfd_house6['lighting'] = dfd['lighting']
#dfd_house6['outlets_unknown'] = dfd['outlets_unknown']
#
#dfd_house6.index = pd.to_datetime(dfd_house6.index)

## REFIT House 8
dfd_house8 = pd.DataFrame()

dfd_house8['microwave'] = dfd['microwave']
dfd_house8['toaster'] = dfd['toaster']
dfd_house8['kettle'] = dfd['kettle']
#dfd_house8['refrigerator'] = dfd['refrigerator']
dfd_house8['freezer'] = dfd['freezer']
dfd_house8['television_site'] = dfd['television_site']
dfd_house8['washing_machine'] = dfd['washing_machine']
dfd_house8['computer'] = dfd['computer']

dfd_house8.index = pd.to_datetime(dfd_house8.index)

# select date range
#start_date = '2011-04-23' # from 2011-04-23
#end_date = '2011-05-02' # to 2011-05-01

#start_date = '2011-04-23' # from 2011-04-23
#end_date = '2011-04-30' # to 2011-05-01

# REDD house 1 range
#start_date = '2011-05-01' # from 2011-04-23
#end_date = '2011-05-04' # to 2011-05-01

# REDD house 2 range
#start_date = '2011-04-18' # from 2011-04-23
#end_date = '2011-04-21' # to 2011-05-01

# REDD house 6 range
#start_date = '2011-05-22' # from 2011-04-23
#end_date = '2011-05-25' # to 2011-05-01

# REFIT range
start_date = '2013-12-01' # from 2011-04-23
end_date = '2013-12-04' # to 2011-05-01

mask = (df.index > start_date) & (df.index < end_date)
df = df.loc[mask]

# Demo files
#mask = (dfd.index > start_date) & (dfd.index < end_date)
#dfd = dfd.loc[mask]

# REDD House 1
#mask = (dfd_house1.index > start_date) & (dfd_house1.index < end_date)
#dfd_house1 = dfd_house1.loc[mask]

# REDD House 2
#mask = (dfd_house2.index > start_date) & (dfd_house2.index < end_date)
#dfd_house2 = dfd_house2.loc[mask]

# REDD House 6
#mask = (dfd_house6.index > start_date) & (dfd_house6.index < end_date)
#dfd_house6 = dfd_house6.loc[mask]

# REFIT House 8
mask = (dfd_house8.index > start_date) & (dfd_house8.index < end_date)
dfd_house8 = dfd_house8.loc[mask]


fig, axs = plt.subplots(3, 1, sharex=True)
axs[0].plot(df)
axs[0].set_title("Aggregated power", size=8)
#axs[0].set_title("Aggregated power of house 2 from April 23th to 30th 2011, downsampled to 1 minute", size=8)
#
#axs[1].stackplot(dfd.index, dfd.values.T, labels = list(dfd.columns.values))

# REDD House 1
#axs[1].stackplot(dfd_house1.index, dfd_house1.values.T, labels = list(dfd_house1.columns.values))

## REDD House 2
#axs[1].stackplot(dfd_house2.index, dfd_house2.values.T, labels = list(dfd_house2.columns.values))
#
## REDD House 6
#axs[1].stackplot(dfd_house6.index, dfd_house6.values.T, labels = list(dfd_house6.columns.values))
#
# REFIT House 8
axs[1].stackplot(dfd_house8.index, dfd_house8.values.T, labels = list(dfd_house8.columns.values))


axs[1].set_title("Disaggregated appliance power [Ground Truth]", size=8)
axs[1].legend(loc='upper left', fontsize=6)

#%%
#REDD parameters
# Please read the paper to undertand following parameters. Note initial values of these parameters depends on the appliances used and the frequency of usage.
sigma = 20;
ri = 2.25
T_Positive = 10;
T_Negative = -10;
#Following parameters alpha and beta are used in Equation 15 of the paper 
# alpha define weight given to magnitude and beta define weight given to time
alpha = 0.5
beta  = 0.5
# this defines the  minimum number of times an appliance is set ON in considered time duration
instancelimit = 5

#%%
# Please read the paper to undertand following parameters. Note initial values of these parameters depends on the appliances used and the frequency of usage.
sigma = 10;
ri = 0.1
T_Positive = 10;
T_Negative = -10;
#Following parameters alpha and beta are used in Equation 15 of the paper 
# alpha define weight given to magnitude and beta define weight given to time
alpha = 0.5
beta  = 0.5
# this defines the  minimum number of times an appliance is set ON in considered time duration
instancelimit = 3

#%%

t1 = time.time() 

main_val = df.values # get only readings
main_ind = df.index  # get only timestamp
data_vec =  main_val
signature_database = "signature_database_labelled.csv" #the signatures were extracted of power analysis from April 28th to 30th
#signature_database = "../Data/REDD/house_2/signatures/signature_house_2_main1.csv" #the signatures were extracted of power analysis from April 28th to 30th
#signature_database = "../Data/REFIT/signatures/signature_house_8_1.csv" #the signatures were extracted of power analysis from April 28th to 30th
#threshold = 10000 # threshold of DTW algorithm used for appliance power signature matching
threshold = 3000
#threshold = 70000 
#threshold_max = 200000 

#delta_p = [np.around(data_vec[i+1]  - data_vec[i], 2) for i in range(0, len(data_vec) - 1)]
delta_p = [round(data_vec[i+1] - data_vec[i], 2) for i in range(0, len(data_vec) - 1)]
event =  [i for i in range(0, len(delta_p)) if (delta_p[i] > T_Positive or delta_p[i] < T_Negative) ]

# initial and refined clustering block of Figure 1 in the paper
clusters = gsp.refined_clustering_block(event, delta_p, sigma, ri)

# Feature matching block of Figure 1 in the paper
finalclusters, pairs = gsp.pair_clusters_appliance_wise(clusters, data_vec, delta_p, instancelimit)
appliance_pairs = gsp.feature_matching_module(pairs, delta_p, finalclusters, alpha, beta)

# create appliance wise disaggregated series
power_series, appliance_signatures = gsp.generate_appliance_powerseries(appliance_pairs, delta_p)

#%%
# label the disaggregated appliance clusters by comparing with signature DB
labeled_appliances = gsp.label_appliances(appliance_signatures, signature_database, threshold)

# Correcting a bug with the labels
for index in range(len(power_series)):     
    verify = index in labeled_appliances.keys()
    # print(verify)
    
    if not verify:
        labeled_appliances[index] = 'Unknown'

#%%
# Manually labelling, due lack of memory
labeled_appliances = OrderedDict()
dfw = pd.concat(appliance_signatures, axis = 1, ignore_index=True)
dfw.drop(dfw.index[1], axis=1)

#dfr = pd.read_csv(signature_database, index_col=0)
#dfw.to_csv("../Data/REDD/house_1/signature_database_house_1_main1.csv")

# House 8 REFIT
labeled_appliances[0] = 'microwave'
labeled_appliances[1] = 'toaster'
labeled_appliances[2] = 'Unknown'
labeled_appliances[3] = 'freezer'
labeled_appliances[4] = 'television_site'
#labeled_appliances[5] = 'washing machine'
#labeled_appliances[6] = 'computer'
#labeled_appliances[7] = 'Unknown'
#labeled_appliances[8] = 'Unknown'
#labeled_appliances[9] = 'Unknown'
#labeled_appliances[10] = 'Unknown'
#labeled_appliances[11] = 'Unknown'
#labeled_appliances[12] = 'Unknown'
#labeled_appliances[13] = 'Unknown'
#labeled_appliances[14] = 'Unknown'
#labeled_appliances[15] = 'Unknown'
#labeled_appliances[16] = 'Unknown'
#labeled_appliances[17] = 'Unknown'
#labeled_appliances[18] = 'Unknown'
#labeled_appliances[19] = 'Unknown'
#labeled_appliances[20] = 'Unknown'
#labeled_appliances[21] = 'Unknown'
#labeled_appliances[22] = 'Unknown'
#labeled_appliances[23] = 'Unknown'
#labeled_appliances[24] = 'kettle'
#labeled_appliances[25] = 'Unknown'
#labeled_appliances[26] = 'Unknown'

#labeled_appliances[0] = 'fridge'
#labeled_appliances[1] = 'freezer'
#labeled_appliances[2] = 'washer_dryer'
#labeled_appliances[3] = 'washing machine'
#labeled_appliances[4] = 'toaster'
#labeled_appliances[5] = 'computer' 
#labeled_appliances[6] = 'television_site'
#labeled_appliances[7] = 'microwave'
#labeled_appliances[8] = 'kettle'
#labeled_appliances[9] = 'Unknown'
#labeled_appliances[10] = 'Unknown'
#labeled_appliances[11] = 'Unknown'
#labeled_appliances[12] = 'Unknown'
#labeled_appliances[13] = 'Unknown'
#labeled_appliances[14] = 'Unknown'
#labeled_appliances[15] = 'Unknown'
#labeled_appliances[16] = 'Unknown'
#labeled_appliances[17] = 'Unknown'
#labeled_appliances[18] = 'Unknown'
#labeled_appliances[19] = 'Unknown'
#labeled_appliances[20] = 'Unknown'
#labeled_appliances[21] = 'Unknown'
#labeled_appliances[22] = 'Unknown'
#labeled_appliances[23] = 'Unknown'
#labeled_appliances[24] = 'Unknown'
#labeled_appliances[25] = 'Unknown'
#labeled_appliances[26] = 'Unknown'
#labeled_appliances[27] = 'Unknown'
#labeled_appliances[28] = 'Unknown'
#labeled_appliances[29] = 'Unknown'
#labeled_appliances[30] = 'Unknown'
#labeled_appliances[31] = 'Unknown'
#labeled_appliances[32] = 'Unknown'
#labeled_appliances[33] = 'Unknown'
#labeled_appliances[34] = 'Unknown'
#labeled_appliances[35] = 'Unknown'
#labeled_appliances[36] = 'Unknown'
#labeled_appliances[37] = 'Unknown'
#labeled_appliances[38] = 'Unknown'
#labeled_appliances[39] = 'Unknown'
#labeled_appliances[40] = 'Unknown'
#labeled_appliances[41] = 'Unknown'
#labeled_appliances[42] = 'Unknown'
#labeled_appliances[43] = 'Unknown'
#labeled_appliances[44] = 'Unknown'
#labeled_appliances[45] = 'Unknown'
#labeled_appliances[46] = 'Unknown'
#labeled_appliances[47] = 'Unknown'

# House 6 REDD
#labeled_appliances[0] = 'kitchen_outlets'
#labeled_appliances[1] = 'stove'
#labeled_appliances[2] = 'refrigerator' 
#labeled_appliances[3] = 'electronics'
#labeled_appliances[4] = 'electric_heat'
#labeled_appliances[5] = 'air_conditioning'
#labeled_appliances[6] = 'lighting'
#labeled_appliances[7] = 'outlets_unknown'
#labeled_appliances[8] = 'Unknown'
#labeled_appliances[9] = 'Unknown'
#labeled_appliances[10] = 'Unknown'
#labeled_appliances[11] = 'Unknown'
#labeled_appliances[12] = 'Unknown'
#labeled_appliances[13] = 'Unknown'

#labeled_appliances[0] = 'kitchen_outlets'
#labeled_appliances[1] = 'washer_dryer'
#labeled_appliances[2] = 'stove'
#labeled_appliances[3] = 'electronics'
#labeled_appliances[4] = 'bathroom_gfi'
#labeled_appliances[5] = 'refrigerator' 
#labeled_appliances[6] = 'outlets_unknown'
#labeled_appliances[7] = 'outlets_unknown2'
#labeled_appliances[8] = 'electric_heat'
#labeled_appliances[9] = 'kitchen_outlets2'
#labeled_appliances[10] = 'lighting'
#labeled_appliances[11] = 'air_conditioning'
#labeled_appliances[12] = 'air_conditioning2'
#labeled_appliances[13] = 'air_conditioning3'
#labeled_appliances[14] = 'kitchen_outlets'
#labeled_appliances[15] = 'washer_dryer'
#labeled_appliances[16] = 'disposal'
#labeled_appliances[17] = 'stove'
#labeled_appliances[18] = 'microwave'
#labeled_appliances[19] = 'electronics'
#labeled_appliances[20] = 'bathroom_gfi'
#labeled_appliances[21] = 'refrigerator'

# House 2 REDD

#labeled_appliances[0] = 'microwave'
#labeled_appliances[1] = 'kitchen_outlets'
#labeled_appliances[2] = 'Unknown'
#labeled_appliances[3] = 'stove'
#labeled_appliances[4] = 'refrigerator'
#labeled_appliances[5] = 'dishwasher'
#labeled_appliances[6] = 'lighting' 
#labeled_appliances[7] = 'Unknown'
#labeled_appliances[8] = 'kitchen_outlets2'
#labeled_appliances[9] = 'Unknown'
#labeled_appliances[10] = 'Unknown'
#labeled_appliances[11] = 'Unknown'
#labeled_appliances[12] = 'Unknown'
#labeled_appliances[13] = 'Unknown'
#
#labeled_appliances[0] = 'kitchen_outlets'
#labeled_appliances[1] = 'lighting'
#labeled_appliances[2] = 'stove'
#labeled_appliances[3] = 'microwave'
#labeled_appliances[4] = 'washer_dryer'
#labeled_appliances[5] = 'kitchen_outlets2'
#labeled_appliances[6] = 'refrigerator' 
#labeled_appliances[7] = 'dishwasher'
#labeled_appliances[8] = 'disposal'
#labeled_appliances[9] = 'Unknown'
#labeled_appliances[10] = 'Unknown'
#labeled_appliances[11] = 'Unknown'
#labeled_appliances[12] = 'Unknown'
#labeled_appliances[13] = 'Unknown'
#labeled_appliances[14] = 'Unknown'
#labeled_appliances[15] = 'Unknown'
#labeled_appliances[16] = 'Unknown'
#labeled_appliances[17] = 'Unknown'
#labeled_appliances[18] = 'Unknown'
#labeled_appliances[19] = 'Unknown'
#labeled_appliances[20] = 'Unknown'
#labeled_appliances[21] = 'Unknown'
#labeled_appliances[22] = 'washer_dryer'
#labeled_appliances[23] = 'kitchen_outlets2'
#labeled_appliances[24] = 'refrigerator' 
#labeled_appliances[25] = 'dishwasher'
#labeled_appliances[26] = 'disposal'
#labeled_appliances[27] = 'kitchen_outlets'
#labeled_appliances[28] = 'lighting'
#labeled_appliances[29] = 'stove'
#labeled_appliances[30] = 'microwave'
#labeled_appliances[31] = 'washer_dryer'
#labeled_appliances[32] = 'kitchen_outlets2'


# House 1 REDD
#labeled_appliances[0] = dfr.iloc[:0,0].name

#labeled_appliances[0] = 'refrigerator' 
#labeled_appliances[1] = 'dishwasher' 
#labeled_appliances[2] = 'microwave'
#labeled_appliances[3] = 'lighting'
#labeled_appliances[4] = 'washer_dryer'
#labeled_appliances[5] = 'bathroom_gfi'
#labeled_appliances[6] = 'kitchen_outlets'
#labeled_appliances[7] = 'oven'
#labeled_appliances[8] = 'Unknown'
#labeled_appliances[9] = 'Unknown'
#labeled_appliances[10] = 'Unknown'
#labeled_appliances[11] = 'Unknown'
#labeled_appliances[12] = 'Unknown'
#labeled_appliances[13] = 'Unknown'
#labeled_appliances[14] = 'Unknown'
#labeled_appliances[15] = 'Unknown'
#labeled_appliances[16] = 'Unknown'
#labeled_appliances[17] = 'Unknown'
#labeled_appliances[18] = 'Unknown'

#labeled_appliances[0] = 'oven' #
#labeled_appliances[1] = 'oven2' #
#labeled_appliances[2] = 'refrigerator' 
#labeled_appliances[3] = 'dishwasher'
#labeled_appliances[4] = 'kitchen_outlets'
#labeled_appliances[5] = 'kitchen_outlets2'
#labeled_appliances[6] = 'lighting' #
#labeled_appliances[7] = 'washer_dryer'
#labeled_appliances[8] = 'microwave'
#labeled_appliances[9] = 'bathroom_gfi'
#labeled_appliances[10] = 'electric_heat'
#labeled_appliances[11] = 'stove' #
#labeled_appliances[12] = 'kitchen_outlets3'
#labeled_appliances[13] = 'kitchen_outlets4'
#labeled_appliances[14] = 'lighting2'
#labeled_appliances[15] = 'lighting3'
#labeled_appliances[16] = 'washer_dryer2'
#labeled_appliances[17] = 'washer_dryer3'
#labeled_appliances[18] = 'Unknown'
#labeled_appliances[19] = 'Unknown'
#labeled_appliances[20] = 'Unknown'
#labeled_appliances[21] = 'Unknown'
#labeled_appliances[22] = 'Unknown'
#labeled_appliances[23] = 'Unknown'
#labeled_appliances[24] = 'Unknown'
#labeled_appliances[25] = 'Unknown'
#labeled_appliances[26] = 'Unknown'
#labeled_appliances[27] = 'Unknown'
#labeled_appliances[28] = 'Unknown'
#labeled_appliances[29] = 'Unknown'
#labeled_appliances[30] = 'Unknown'
#labeled_appliances[31] = 'Unknown'
#labeled_appliances[32] = 'Unknown'
#labeled_appliances[33] = 'Unknown'
#labeled_appliances[34] = 'Unknown'
#labeled_appliances[35] = 'Unknown'
#labeled_appliances[36] = 'Unknown'
#labeled_appliances[37] = 'Unknown'
#labeled_appliances[38] = 'Unknown'
#labeled_appliances[39] = 'Unknown'

        
#%%
# Attach timestamps to generated series
power_timeseries = gsp.create_appliance_timeseries(power_series, main_ind)

# create pandas dataframe of all series
gsp_result = pd.concat(power_timeseries, axis = 1)

labels= [i[1] for i in list(labeled_appliances.items())]
gsp_result.columns = labels

#labels_useful = labels[0:5]
#gsp_result_useful = gsp_result.ix[:,0:5]

axs[2].stackplot(gsp_result.index, gsp_result.values.T, labels=labels)
#axs[2].stackplot(gsp_result_useful.index, gsp_result_useful.values.T, labels=labels_useful)
axs[2].set_title("Disaggregated appliance [Results]", size=8)
axs[2].legend(loc='upper left', fontsize=6)

#gsp_result.plot(kind='area', stacked=True, title='stacked appliances power', label=labeled_appliances)
#gsp_result.plot(subplots=True, layout=(2,1))
print("6 of 6> plotting the input and results :)")

plt.show()

#gsp.calculate_energy_pct(dfd, gsp_result)
#gsp.calculate_energy_pct(dfd_house1, gsp_result),
#gsp.calculate_energy_pct(dfd_house2, gsp_result)
#gsp.calculate_energy_pct(dfd_house6, gsp_result)
gsp.calculate_energy_pct(dfd_house8, gsp_result)
#gsp.calculate_energy_pct(dfd, gsp_result_useful)

t2 = time.time()

t = t2 - t1

s = t%60
m1 = t//60
m = m1%60
h = m1//60

print("Time elapsed: %d h %d min %d sec" %(h, m, s))

#%%
dfw = pd.concat(appliance_signatures, axis = 1, ignore_index=True)
dfw.drop(dfw.index[1], axis=1)

dfw.to_csv("../Data/REFIT/signatures/signature_house_8.csv")

#%%

#plt.plot(gsp_result.index, gsp_result.ix[:,24])
#plt.plot(dfd_house8.index, dfd_house8['microwave'])
#plt.plot(dfd_house8.index, dfd_house8['toaster'])
#plt.plot(dfd_house8.index, dfd_house8['kettle'])
#plt.plot(dfd_house8.index, dfd_house8['freezer'])
#plt.plot(dfd_house8.index, dfd_house8['television_site'])
#plt.plot(dfd_house8.index, dfd_house8['washing_machine'])

## Trocar
# kettle por freezer
# Unknown.3 por kettle
# Unknown por television_site
# Unknown.5: washing_machine ou toaster?
# freezer por microwave?
# gsp_result.ix[:,24].name = 'kettle'

#%%

#Demo encontrou 14 eletrodomésticos, com threshold = 3000

#True positives
#0 e 10, 'refrigerator', TP = 7032 (TP = 108) (0), TP = 4338 (TP = 0) (10)
#1, 'kitchen_outlets1', TP = 8137 (TP = 3417)
#2, 'kitchen_outlets2', TP = 9891 (TP = 47)
#3, 'microwave', TP = 9786 (TP = 0)
#4, 5, 6, 7, 8, 9 'lighting', TP = 8678 (TP = 0) (4), TP = 8704 (TP = 0) (5), TP = 9746 (TP = 2) (6), TP = 9038 (TP = 3) (7), TP = 8840 (TP = 0) (8), TP = 8539 (TP = 0) (9)

# df_result = dfd_house1.join(gsp_result, lsuffix='_dfd', rsuffix='_result')

#for l in range(4, 10):
TP = 0
for k in range(len(dfd['lighting'].values)):
    try:  
#            if abs(dfd['lighting'].values[k] - gsp_result.ix[:,l].values[k]) <= 10:
        if dfd['lighting'].values[k] == gsp_result.ix[:,l].values[k]:
            TP += 1
    except:
        break
print TP

#%%
# True Negatives
#0 e 10, 'refrigerator', TN = 14340 (TN = 43774) (0), TN = 16496 (TN = 43547) (10)     
#1, 'kitchen_outlets1', TN = 10634 (TN = 46029)
#2, 'kitchen_outlets2', TN = 16815 (TN = 42970)
#3, 'microwave', TN = 14050 (TN = 42747)
#4, 5, 6, 7, 8, 9, 'lighting', TN = 10689 (TN = 42580) (4), TN = 10521 (TN = 28213) (5), TN = 18193 (TN = 13121) (6), TN = 14520 (TN = 21836) (7), TP = 11882 (TN = 31419) (8), TP = 11018 (TN = 42640) (9)

for m in range(4, 10):
    TN = 0
    for l in dfd.columns:
        if l == 'lighting':
            continue
        for k in range(len(dfd[l].values)):
            try:  
#                if abs(dfd[l].values[k] - gsp_result.ix[:,m].values[k]) >= 10:
                if dfd[l].values[k] != gsp_result.ix[:,m].values[k]:    
                    TN += 1
            except:
                break
    print TN

#%%
# False Positives
#0 e 10, 'refrigerator', FP = 2302 (FP = 31773) (0), FP = 2529 (FP = 29833) (10)
#1, 'kitchen_outlets1', FP = 47 (FP = 35478)
#2, 'kitchen_outlets2', FP = 3106 (FP = 29346)
#3, 'microwave', FP = 3329 (FP = 32098)
#4, 5, 6, 7, 8, 9, 'lighting', FP = 3496 (FP = 29297) (4), FP = 3515 (FP = 29432) (5), FP = 2426 (FP = 22991) (6), FP = 2552 (FP = 26653) (7), FP = 3375 (FP = 28182) (8), FP = 3436 (FP = 29002) (9)

#for m in range(4, 10):
FP = 0
for l in dfd.columns:
    if l == 'microwave':
        continue
    for k in range(len(dfd[l].values)):
        try:  
            if abs(dfd[l].values[k] - gsp_result.ix[:,3].values[k]) <= 10:
#            if dfd[l].values[k] == gsp_result.ix[:,3].values[k]:    
                FP += 1
        except:
            break
print FP

#%%

#False Negatives

#'refrigerator', FN = 113, (FN = 2346) <=5 (FN = 76563) <=10
#'kitchen_outlets1', FN = 38962 (FN = 96407) <= 5 (FN = 97547) <=10
#'kitchen_outlets2', FN = 534 (FN = 124541) <=5 (FN = 127279) <=10
#'microwave', FN = 0 (FN = 113369) <=5 (FN = 120865) <=10
#'lighting', FN = 15 (FN = 4750) <=5 (FN = 112552) <=10

FN = 0
for l in range(len(gsp_result.columns)):
    if l == 0 and l == 10:
    #if l == 1:
    #if l == 2:
    #if l == 3:
    #if l == 4 and l == 5 and l == 6 and l == 7 and l == 8 and l == 9:
        continue
for k in range(len(dfd.values)):
    try:
    #if dfd['lighting'].values[k] == gsp_result.ix[:,l].values[k]:    
        if abs(dfd['lighting'].values[k] - gsp_result.ix[:,l].values[k]) <= 10:
            FN += 1
    except:
        break
print FN

#%%

# ==

TP = 108 #refrigerator
TP = 3417 #kitchen_outlets1
TP = 47 #kitchen_outlets2
TP = 0 #microwave
TP = 0 #lighting
TP = 0 #lighting
TP = 2 #lighting
TP = 3 #lighting
TP = 0 #lighting
TP = 0 #lighting
TP = 0 #refrigerator

TP = [108, 3417, 47, 0, 0, 0, 2, 3, 0, 0, 0]

TN = 43774 #refrigerator
TN = 46029 #kitchen_outlets1
TN = 16815 #kitchen_outlets2
TN = 42747 #microwave
TN = 42580 #lighting
TN = 28213 #lighting
TN = 13121 #lighting
TN = 21836 #lighting
TN = 31419 #lighting 
TN = 42640 #lighting 
TN = 43547 #refrigerator

TN = [43774, 46029, 16815, 42747, 42580, 28213, 13121, 21836, 31419, 42640, 43547]

FP = 31773 #refrigerator
FP = 35478 #kitchen_outlets1
FP = 29346 #kitchen_outlets2
FP = 32098 #microwave
FP = 29297 #lighting
FP = 29432 #lighting
FP = 22991 #lighting
FP = 26653 #lighting
FP = 28182 #lighting
FP = 29002 #lighting
FP = 29833 #refrigerator

FP = [31773, 35478, 29346, 32098, 29297, 29432, 22991, 26653, 28182, 29002, 29833]

FN = 113   #refrigerator
FN = 38962 #kitchen_outlets1
FN = 534   #kitchen_outlets2
FN = 0     #microwave
FN = 15    #lighting

FN = [113, 38962, 534, 0, 15, 15, 15, 15, 15, 15, 113]

# <=10

TP = 7032 #refrigerator
TP = 8137 #kitchen_outlets1
TP = 9891 #kitchen_outlets2
TP = 9786 #microwave
TP = 8678 #lighting
TP = 8704 #lighting
TP = 9746 #lighting
TP = 9038 #lighting
TP = 8840 #lighting
TP = 8539 #lighting
TP = 4338 #refrigerator

TP = [7032, 8137, 9891, 9786, 8678, 8704, 9746, 9038, 8840, 8539, 4338]

TN = 14340 #refrigerator
TN = 10634 #kitchen_outlets1
TN = 16815 #kitchen_outlets2
TN = 14050 #microwave
TN = 10689 #lighting
TN = 10521 #lighting
TN = 18193 #lighting
TN = 14520 #lighting
TN = 11882 #lighting
TN = 11018 #lighting
TN = 16496 #refrigerator

TN = [14340, 10634, 16815, 14050, 10689, 10521, 18193, 14520, 11882, 11018, 16496]

FP = 2302 #refrigerator
FP = 47   #kitchen_outlets1
FP = 3106 #kitchen_outlets2
FP = 3329 #microwave
FP = 3496 #lighting
FP = 3515 #lighting
FP = 2426 #lighting
FP = 2552 #lighting
FP = 3375 #lighting
FP = 3436 #lighting
FP = 2529 #refrigerator

FP = [2302, 47, 3106, 3329, 3496, 3515, 2426, 2552, 3375, 3436, 2529]

FN = 76563  #refrigerator
FN = 97547  #kitchen_outlets1
FN = 127279 #kitchen_outlets2
FN = 120865 #microwave
FN = 112552 #lighting

FN = [76563, 97547, 127279, 120865, 112552, 112552, 112552, 112552, 112552, 112552, 76563]

# <=5

FN = 2346   #refrigerator
FN = 96407  #kitchen_outlets1
FN = 124541 #kitchen_outlets2
FN = 113369 #microwave
FN = 4750   #lighting

FN = [2346, 96407, 124541, 113369, 4750, 4750, 4750, 4750, 4750, 4750, 2346]

#%%

# ==

#TP = [108, 3417, 47, 0, 0, 0, 2, 3, 0, 0, 0]
#TN = [43774, 46029, 16815, 42747, 42580, 28213, 13121, 21836, 31419, 42640, 43547]
#FP = [31773, 35478, 29346, 32098, 29297, 29432, 22991, 26653, 28182, 29002, 29833]
FN = [113, 38962, 534, 0, 15, 15, 15, 15, 15, 15, 113]

# <= 10

TP = [7032, 8137, 9891, 9786, 8678, 8704, 9746, 9038, 8840, 8539, 4338]
TN = [14340, 10634, 16815, 14050, 10689, 10521, 18193, 14520, 11882, 11018, 16496]
FP = [2302, 47, 3106, 3329, 3496, 3515, 2426, 2552, 3375, 3436, 2529]
#FN = [76563, 97547, 127279, 120865, 112552, 112552, 112552, 112552, 112552, 112552, 76563]

Precision = []
Recall = []
F1_score = []
Accuracy = []

for i in range(11):
    PR = float(TP[i])/float(TP[i] + FP[i])
    RE = float(TP[i])/float(TP[i] + FN[i])
    Precision.append(PR)
    Recall.append(RE)
    F1_score.append(2 * (PR * RE)/(PR + RE))
    Accuracy.append(float(TP[i] + TN[i])/float(TP[i] + TN[i] + FP[i] + FN[i]))
