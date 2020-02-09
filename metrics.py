# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 16:27:43 2020

@author: bruno
"""

df_result = dfd_house1.join(gsp_result, lsuffix='_dfd', rsuffix='_result')

#%%

#True Positives

TP_dict = {}
for appliance in dfd_house1.columns:
    TP = 0
    if appliance == 'Unknown':
        continue
    
    for k in range(len(df_result[appliance+'_dfd'].values)):
        #        if abs(dfd['lighting'].values[k] - gsp_result.ix[:,l].values[k]) <= 10:
        #        if dfd['lighting'].values[k] == df_result.ix[:,l].values[k]:
            if df_result[appliance+'_dfd'].values[k] == df_result[appliance+'_result'].values[k]:
                TP += 1
    TP_dict[appliance] = TP

#'bathroom_gfi' = 3656
#'dishwasher' = 52481
#'kitchen_outlets' = 0
#'lighting' = 17866
#'microwave' = 0
#'oven' = 42502
#'refrigerator' = 4
#'washer_dryer' = 44956

#%%
for appliance in dfd_house1.columns:
    for l in range(16, 20):
        TP = 0
        for k in range(len(df_result[appliance+'_dfd'].values)):
            try:
                if df_result[appliance+'_dfd'] == df_result.ix[:,l].values[k]:           
                    TP += 1
            except:
                continue
        print ("Resultados de "+appliance+" em comparação com %d: %d" %(l,TP))

#%%
        
# True Negatives

TN_dict = {}
for appliance in dfd_house1.columns:
    TN = 0
    if appliance == 'Unknown':
        continue
    for appliance2 in dfd_house1.columns:
        if appliance == 'Unknown':
            continue
        if appliance == appliance2:
                continue
        for k in range(len(df_result[appliance+'_dfd'].values)):
            #        if abs(dfd['lighting'].values[k] - gsp_result.ix[:,l].values[k]) <= 10:
            #        if dfd['lighting'].values[k] == df_result.ix[:,l].values[k]:
                if df_result[appliance+'_dfd'].values[k] != df_result[appliance2+'_result'].values[k]:
                    TN += 1
        TN_dict[appliance] = TN   
    
#'bathroom_gfi' = 411786
#'dishwasher' = 136645
#'kitchen_outlets' = 434443
#'lighting' = 316359
#'microwave' = 434511
#'oven' = 92359
#'refrigerator' = 434511
#'washer_dryer' = 104460   

#%%
        
# False Negatives
        
FN_dict = {}
for appliance in dfd_house1.columns:
    FN = 0
    if appliance == 'Unknown':
        continue
    for appliance2 in dfd_house1.columns:
        if appliance == 'Unknown':
            continue
        if appliance == appliance2:
                continue
        for k in range(len(df_result[appliance+'_dfd'].values)):
            #        if abs(dfd['lighting'].values[k] - gsp_result.ix[:,l].values[k]) <= 10:
            #        if dfd['lighting'].values[k] == df_result.ix[:,l].values[k]:
                if df_result[appliance+'_dfd'].values[k] == df_result[appliance2+'_result'].values[k]:
                    FN += 1
        FN_dict[appliance] = FN     
        
#'bathroom_gfi' = 22725
#'dishwasher' = 297866
#'kitchen_outlets' = 89
#'lighting' = 118152
#'microwave' = 0
#'oven' = 342152
#'refrigerator' = 330051
#'washer_dryer' = 

#%%
        
#False Positives
        
FP_dict = {}
for appliance in dfd_house1.columns:
    FP = 0
    if appliance == 'Unknown':
        continue
    
    for k in range(len(df_result[appliance+'_dfd'].values)):
        #        if abs(dfd['lighting'].values[k] - gsp_result.ix[:,l].values[k]) <= 10:
        #        if dfd['lighting'].values[k] == df_result.ix[:,l].values[k]:
            if df_result[appliance+'_dfd'].values[k] != df_result[appliance+'_result'].values[k]:
                FP += 1
    FP_dict[appliance] = FP    
 
#'bathroom_gfi' = 58417
#'dishwasher' = 9592
#'kitchen_outlets' = 62073
#'lighting' = 44207
#'microwave' = 62073
#'oven' = 19571
#'refrigerator' = 62069
#'washer_dryer' = 17117   
      
#%%

#df_result = dfd_house1.join(gsp_result, lsuffix='_dfd', rsuffix='_result')
#df_result = dfd_house2.join(gsp_result, lsuffix='_dfd', rsuffix='_result')
#df_result = dfd_house6.join(gsp_result, lsuffix='_dfd', rsuffix='_result')
#df_result = dfd_house8.join(gsp_result, lsuffix='_dfd', rsuffix='_result')
#df_result = dfd.join(gsp_result, lsuffix='_dfd', rsuffix='_result')
    
def true_positives(dfd):
    TP_dict = {}
    for appliance in dfd.columns:
        TP = 0
        if appliance == 'Unknown':
            continue
    
        for k in range(len(df_result[appliance+'_dfd'].values)):
        #        if abs(dfd['lighting'].values[k] - gsp_result.ix[:,l].values[k]) <= 10:
        #        if dfd['lighting'].values[k] == df_result.ix[:,l].values[k]:
            if df_result[appliance+'_dfd'].values[k] == df_result[appliance+'_result'].values[k]:
                TP += 1
        TP_dict[appliance] = TP
    return TP_dict

def true_negatives(dfd):
    TN_dict = {}
    for appliance in dfd.columns:
        TN = 0
        if appliance == 'Unknown':
            continue
        for appliance2 in dfd.columns:
            if appliance == 'Unknown':
                continue
            if appliance == appliance2:
                    continue
            for k in range(len(df_result[appliance+'_dfd'].values)):
                #        if abs(dfd['lighting'].values[k] - gsp_result.ix[:,l].values[k]) <= 10:
                #        if dfd['lighting'].values[k] == df_result.ix[:,l].values[k]:
                    if df_result[appliance+'_dfd'].values[k] != df_result[appliance2+'_result'].values[k]:
                        TN += 1
            TN_dict[appliance] = TN
    return TN_dict
            
def false_negatives(dfd):
    FN_dict = {}
    for appliance in dfd.columns:
        FN = 0
        if appliance == 'Unknown':
            continue
        for appliance2 in dfd.columns:
            if appliance == 'Unknown':
                continue
            if appliance == appliance2:
                    continue
            for k in range(len(df_result[appliance+'_dfd'].values)):
                #        if abs(dfd['lighting'].values[k] - gsp_result.ix[:,l].values[k]) <= 10:
                #        if dfd['lighting'].values[k] == df_result.ix[:,l].values[k]:
                    if df_result[appliance+'_dfd'].values[k] == df_result[appliance2+'_result'].values[k]:
                        FN += 1
            FN_dict[appliance] = FN
    return FN_dict

def false_positives(dfd):
    FP_dict = {}
    for appliance in dfd.columns:
        FP = 0
        if appliance == 'Unknown':
            continue
        
        for k in range(len(df_result[appliance+'_dfd'].values)):
            #        if abs(dfd['lighting'].values[k] - gsp_result.ix[:,l].values[k]) <= 10:
            #        if dfd['lighting'].values[k] == df_result.ix[:,l].values[k]:
                if df_result[appliance+'_dfd'].values[k] != df_result[appliance+'_result'].values[k]:
                    FP += 1
        FP_dict[appliance] = FP 
    return TP_dict