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
 

      
#%%

def true_positives(dfd, labels):
    TP_dict = {}
    for appliance in labels:
        TP = 0
        if appliance == 'Unknown':
            continue
        try:
            for k in range(len(df_result[appliance+'_dfd'].values)):
            #        if abs(dfd['lighting'].values[k] - gsp_result.ix[:,l].values[k]) <= 10:
            #        if dfd['lighting'].values[k] == df_result.ix[:,l].values[k]:
                if df_result[appliance+'_dfd'].values[k] == df_result[appliance+'_result'].values[k]:
                    TP += 1
            TP_dict[appliance] = TP
        except:
            continue
    return TP_dict

def true_negatives(dfd, labels):
    TN_dict = {}
    for appliance in labels:
        TN = 0
        if appliance == 'Unknown':
            continue
        for appliance2 in labels:
            if appliance == 'Unknown':
                continue
            if appliance == appliance2:
                    continue
            try:
                for k in range(len(df_result[appliance+'_dfd'].values)):
                    #        if abs(dfd['lighting'].values[k] - gsp_result.ix[:,l].values[k]) <= 10:
                    #        if dfd['lighting'].values[k] == df_result.ix[:,l].values[k]:
                        if df_result[appliance+'_dfd'].values[k] != df_result[appliance2+'_result'].values[k]:
                            TN += 1
                TN_dict[appliance] = TN
            except:
                continue
    return TN_dict
            
def false_negatives(dfd, labels):
    FN_dict = {}
    for appliance in labels:
        FN = 0
        if appliance == 'Unknown':
            continue
        for appliance2 in labels:
            if appliance == 'Unknown':
                continue
            if appliance == appliance2:
                    continue
            try:
                for k in range(len(df_result[appliance+'_dfd'].values)):
                    #        if abs(dfd['lighting'].values[k] - gsp_result.ix[:,l].values[k]) <= 10:
                    #        if dfd['lighting'].values[k] == df_result.ix[:,l].values[k]:
                        if df_result[appliance+'_dfd'].values[k] == df_result[appliance2+'_result'].values[k]:
                            FN += 1
                FN_dict[appliance] = FN
            except:
                continue
    return FN_dict

def false_positives(dfd, labels):
    FP_dict = {}
    for appliance in labels:
        FP = 0
        if appliance == 'Unknown':
            continue
        try:
            for k in range(len(df_result[appliance+'_dfd'].values)):
                #        if abs(dfd['lighting'].values[k] - gsp_result.ix[:,l].values[k]) <= 10:
                #        if dfd['lighting'].values[k] == df_result.ix[:,l].values[k]:
                    if df_result[appliance+'_dfd'].values[k] != df_result[appliance+'_result'].values[k]:
                        FP += 1
            FP_dict[appliance] = FP
        except:
            continue
    return FP_dict

# REDD House 1
#df_result = dfd_house1.join(gsp_result, lsuffix='_dfd', rsuffix='_result')
#
#print("Calculating True Positives...")
#TP = true_positives(df_result, dfd_house1.columns)
#print("Calculating False Negatives...")
#FN = false_negatives(df_result, dfd_house1.columns)
#print("Calculating True Negatives...")
#TN = true_negatives(df_result, dfd_house1.columns)
#print("Calculating False Positives...")
#FP = false_positives(df_result, dfd_house1.columns)

# REDD House 2
#df_result = dfd_house2.join(gsp_result, lsuffix='_dfd', rsuffix='_result')
#
#print("Calculating True Positives...")
#TP = true_positives(df_result, dfd_house2.columns)
#print("Calculating False Positives...")
#FN = false_negatives(df_result, dfd_house2.columns)
#print("Calculating True Negatives...")
#TN = true_negatives(df_result, dfd_house2.columns)
#print("Calculating False Positives...")
#FP = false_positives(df_result, dfd_house2.columns)

# REDD House 6
#df_result = dfd_house6.join(gsp_result, lsuffix='_dfd', rsuffix='_result')
#
#print("Calculating True Positives...")
#TP = true_positives(df_result, dfd_house6.columns)
#print("Calculating False Positives...")
#FN = false_negatives(df_result, dfd_house6.columns)
#print("Calculating True Negatives...")
#TN = true_negatives(df_result, dfd_house6.columns)
#print("Calculating False Positives...")
#FP = false_positives(df_result, dfd_house6.columns)

# REFIT House 8
df_result = dfd_house8.join(gsp_result, lsuffix='_dfd', rsuffix='_result')

print("Calculating True Positives...")
TP = true_positives(df_result, dfd_house8.columns)
print("Calculating False Positives...")
FN = false_negatives(df_result, dfd_house8.columns)
print("Calculating True Negatives...")
TN = true_negatives(df_result, dfd_house8.columns)
print("Calculating False Positives...")
FP = false_positives(df_result, dfd_house8.columns)

#Demo Files
#df_result = dfd.join(gsp_result, lsuffix='_dfd', rsuffix='_result')
#
#print("Calculating True Positives...")
#TP = true_positives(df_result, dfd.columns)
#print("Calculating False Positives...")
#FN = false_negatives(df_result, dfd.columns)
#print("Calculating True Negatives...")
#TN = true_negatives(df_result, dfd.columns)
#print("Calculating False Positives...")
#FP = false_positives(df_result, dfd.columns)

#print "True positives", TP; print "\n"; 
#print "True negatives", TN; print "\n"; 
#print "False positives", FP; print "\n"; 
#print "False positives", FN; print "\n";

#%%

#REDD House 1 Main 1 metrics with the article parameters

#True positives
#'bathroom_gfi' = 3656
#'dishwasher' = 52481
#'kitchen_outlets' = 0
#'lighting' = 17866
#'microwave' = 0
#'oven' = 42502
#'refrigerator' = 4
#'washer_dryer' = 44956

#TP = [3656, 52481, 0, 17866, 0, 42502, 4, 44956]

#True negatives
#'bathroom_gfi' = 411786
#'dishwasher' = 136645
#'kitchen_outlets' = 434443
#'lighting' = 316359
#'microwave' = 434511
#'oven' = 92359
#'refrigerator' = 434511
#'washer_dryer' = 104460   

#TN = [411786, 136645, 434443, 316359, 434511, 92359, 434511, 104460]

#False positives
#'bathroom_gfi' = 58417
#'dishwasher' = 9592
#'kitchen_outlets' = 62073
#'lighting' = 44207
#'microwave' = 62073
#'oven' = 19571
#'refrigerator' = 62069
#'washer_dryer' = 17117   

#FP = [58417, 9592, 62073, 44207, 62073, 19571, 62069, 17117]

#False Negatives
#'bathroom_gfi' = 22725
#'dishwasher' = 297866
#'kitchen_outlets' = 89
#'lighting' = 118152
#'microwave' = 0
#'oven' = 342152
#'refrigerator' = 0
#'washer_dryer' = 330051

#FN = [22725, 297866, 89, 118152, 0, 342152, 0, 330051]

#REDD House 1 Main 2 metrics with the article parameters
#True positives
# 'bathroom_gfi': 3298,
# 'dishwasher': 42369,
# 'kitchen_outlets': 0,
# 'lighting': 19492,
# 'microwave': 0,
# 'refrigerator': 0,
# 'washer_dryer': 57239

#TP = [3298, 42369, 0, 19492, 0, 0, 57239]

#False negatives
# 'bathroom_gfi': 17507,
# 'dishwasher': 293674,
# 'kitchen_outlets': 69,
# 'lighting': 99291,
# 'microwave': 0,
# 'refrigerator': 42,
# 'washer_dryer': 299990

#FN = [17507, 293674, 69, 99291, 0, 42, 299990]

#True negatives
# 'bathroom_gfi': 354931,
# 'dishwasher': 78764,
# 'kitchen_outlets': 372369,
# 'lighting': 273147,
# 'microwave': 372438,
# 'refrigerator': 372396,
# 'washer_dryer': 72448

#TN = [354931, 78764, 372369, 273147, 372438, 372396, 72448]

#False positives
# 'bathroom_gfi': 58775,
# 'dishwasher': 19704,
# 'kitchen_outlets': 62073,
# 'lighting': 42581,
# 'microwave': 62073,
# 'refrigerator': 62073,
# 'washer_dryer': 4834

#FP = [58775, 19704, 62073, 42581, 62073, 62073, 4834]

#REDD House 2 Main 1 metrics with the article parameters

#True Positives
# 'dishwasher': 37942,
# 'kitchen_outlets': 20095,
# 'kitchen_outlets2': 1916,
# 'lighting': 0,
# 'microwave': 0,
# 'refrigerator': 0,
# 'stove': 34872

#TP = [37942, 20095, 1916, 0, 0, 0, 34872]

#True Negatives
# 'dishwasher': 86335,
# 'kitchen_outlets': 250543,
# 'kitchen_outlets2': 377505,
# 'lighting': 389019,
# 'microwave': 389022,
# 'refrigerator': 388987,
# 'stove': 215593

#TN = [86335, 250543, 377505, 389019, 389022, 388987, 215593]

#False Positives
# 'dishwasher': 26895,
# 'kitchen_outlets': 44742,
# 'kitchen_outlets2': 62921,
# 'lighting': 64837,
# 'microwave': 64837,
# 'refrigerator': 64837,
# 'stove': 29965

#FP = [26895, 44742, 62921, 64837, 64837, 64837, 29965]

#False Negatives
# 'dishwasher': 302687,
# 'kitchen_outlets': 138479,
# 'kitchen_outlets2': 11517,
# 'lighting': 3,
# 'microwave': 0,
# 'refrigerator': 35,
# 'stove': 173429

#FN = [302687, 138479, 11517, 3, 0, 35, 173429]

#REDD House 2 Main 2 metrics with the article parameters

#True Positives
# 'dishwasher': 55239,
# 'kitchen_outlets': 27521,
# 'kitchen_outlets2': 2236,
# 'lighting': 3,
# 'microwave': 5,
# 'refrigerator': 0,
# 'stove': 34452

#TP = [55239, 27521, 2236, 3, 5, 0, 34452]

#True Negatives
# 'dishwasher': 63414,
# 'kitchen_outlets': 234519,
# 'kitchen_outlets2': 377317,
# 'lighting': 388970,
# 'microwave': 389022,
# 'refrigerator': 389017,
# 'stove': 194199

#TN = [63414, 234519, 377317, 388970, 389022, 389017, 194199]

#False Positives
# 'dishwasher': 9598,
# 'kitchen_outlets': 37316,
# 'kitchen_outlets2': 62601,
# 'lighting': 64834,
# 'microwave': 64832,
# 'refrigerator': 64837,
# 'stove': 30385

#FP = [9598, 37316, 62601, 64834, 64832, 64837, 30385]

#False Negatives
# 'dishwasher': 325608,
# 'kitchen_outlets': 154503,
# 'kitchen_outlets2': 11705,
# 'lighting': 52,
# 'microwave': 0,
# 'refrigerator': 5,
# 'stove': 194823

#FN = [325608, 154503, 11705, 52, 0, 5, 194823]

#REDD House 6 Main 1 metrics with the article parameters
#True Positives
#'stove': 0, 
#'outlets_unknown': 5558, 
#'electric_heat': 0, 
#'lighting': 0, 
#'air_conditioning': 2, 
#'kitchen_outlets': 0, 
#'electronics': 228, 
#'refrigerator': 2882

#TP = [0, 5558, 0, 0, 2, 0, 228, 2882]

#True Negatives
#'stove': 154259, 
#'outlets_unknown': 101122, 
#'electric_heat': 154245, 
#'lighting': 154241, 
#'air_conditioning': 154248, 
#'kitchen_outlets': 154259, 
#'electronics': 152791, 
#'refrigerator': 129178

#TN = [154259, 101122, 154245, 154241, 154248, 154259, 152791, 129178]

#False Positives
#'stove': 22037, 
#'outlets_unknown': 16479, 
#'electric_heat': 22037, 
#'lighting': 22037, 
#'air_conditioning': 22035, 
#'kitchen_outlets': 22037, 
#'electronics': 21809, 
#'refrigerator': 19155

#FP = [22037, 16479, 22037, 22037, 22035, 22037,21809, 19155]

#False Negatives
#'stove': 0, 
#'outlets_unknown': 53137, 
#'electric_heat': 14, 
#'lighting': 18, 
#'air_conditioning': 11, 
#'kitchen_outlets': 0, 
#'electronics': 1468, 
#'refrigerator': 25081

#FN = [0, 53137, 14, 18, 11, 0, 1468, 25081]

#REDD House 6 Main 2 metrics with the article parameters
#True Positives
#'stove': 0, 
#'outlets_unknown': 9526, 
#'electric_heat': 0, 
#'lighting': 0, 
#'air_conditioning': 1, 
#'kitchen_outlets': 0, 
#'electronics': 224, 
#'refrigerator': 4369

#TP = [0, 9526, 0, 0, 1, 0, 224, 4369]

#True Negatives
#'stove': 154259, 
#'outlets_unknown': 95623, 
#'electric_heat': 154252, 
#'lighting': 154182, 
#'air_conditioning': 154246, 
#'kitchen_outlets': 154259, 
#'electronics': 152740, 
#'refrigerator': 125895

#TN = [154259, 95623, 154252, 154182, 154246, 154259, 152740, 125895]

#False Positives
#'stove': 22037, 
#'outlets_unknown': 12511, 
#'electric_heat': 22037, 
#'lighting': 22037, 
#'air_conditioning': 22036, 
#'kitchen_outlets': 22037, 
#'electronics': 21813, 
#'refrigerator': 17668

#FP = [22037, 12511, 22037, 22037, 22036, 22037, 21813, 17668]

#False Negatives
#'stove': 0, 
#'outlets_unknown': 58636, 
#'electric_heat': 7, 
#'lighting': 77, 
#'air_conditioning': 13, 
#'kitchen_outlets': 0, 
#'electronics': 1519, 
#'refrigerator': 28364

#FN = [0, 58636, 7, 77, 13, 0, 1519, 28364]

#REFIT House 8 metrics with the article parameters
#True Positives
#'toaster': 26572, 
#'computer': 0, 
#'freezer': 21024, 
#'microwave': 0, 
#'television_site': 2

#TP = [26572, 0, 21024, 0, 2]

#True Negatives
#'toaster': 24685, 
#'computer': 141308, 
#'freezer': 47101, 
#'microwave': 141308, 
#'television_site': 141060

#TN = [24685, 141308, 47101, 141308, 141060]

#False Positives
#'toaster': 8755, 
#'computer': 35327, 
#'freezer': 14303, 
#'microwave': 35327, 
#'television_site': 35325

#FP = [8755, 35327, 14303, 35327, 35325]

#False Negatives
#'toaster': 116623, 
#'computer': 0, 
#'freezer': 94207, 
#'microwave': 0, 
#'television_site': 248

#FN = [116623, 0, 94207, 0, 248]

#Demo Files
#True Positives
#'kitchen_outlets1': 3421, 
#'kitchen_outlets2': 47, 
#'microwave': 0

#True Negatives
# 'kitchen_outlets1': 16560,
# 'kitchen_outlets2': 22942,
# 'lighting': 34557,
# 'microwave': 23038,
# 'refrigerator': 34557

#False Positives
#'kitchen_outlets1': 8098, 
#'kitchen_outlets2': 11472, 
#'microwave': 11519

#False Negatives
# 'kitchen_outlets1': 6478,
# 'kitchen_outlets2': 96,
# 'lighting': 0,
# 'microwave': 0,
# 'refrigerator': 0
    
#%%
    
#REDD House 1 Main 1 metrics with the other parameters
#True positives
#'bathroom_gfi': 3565,
# 'dishwasher': 48076,
# 'lighting': 12893,
# 'microwave': 0,
# 'refrigerator': 7,
# 'washer_dryer': 56030

#TP = [3565, 48076, 12893, 0, 7, 56030]

#True negatives
# 'bathroom_gfi': 294967,
# 'dishwasher': 63614,
# 'lighting': 223147,
# 'microwave': 310364,
# 'refrigerator': 310365,
# 'washer_dryer': 52460

#TN = [294967, 63614, 223147, 310364, 310365, 52460]

#False positives
# 'bathroom_gfi': 58508,
# 'dishwasher': 13997,
# 'lighting': 49180,
# 'microwave': 62073,
# 'refrigerator': 62066,
# 'washer_dryer': 6043

#FP = [58508, 13997, 49180, 62073, 62066, 6043]

#False negatives
# 'bathroom_gfi': 15398,
# 'dishwasher': 246751,
# 'lighting': 87218,
# 'microwave': 1,
# 'refrigerator': 0,
# 'washer_dryer': 257905

#FN = [15398, 246751, 87218, 1, 0, 257905]

#REDD House 1 Main 2 metrics with the other parameters
#True positives
# 'bathroom_gfi': 3500,
# 'dishwasher': 53724,
# 'lighting': 16229,
# 'microwave': 0,
# 'refrigerator': 0,
# 'washer_dryer': 56700

#TP = [3500, 53724, 16229, 0, 0, 56700]

#True negatives
# 'bathroom_gfi': 295929,
# 'dishwasher': 105637,
# 'lighting': 232386,
# 'microwave': 310363,
# 'refrigerator': 310365,
# 'washer_dryer': 89907

#TN = [295929, 105637, 232386, 310363, 310365, 89907]

#False positives
# 'bathroom_gfi': 58573,
# 'dishwasher': 8349,
# 'lighting': 45844,
# 'microwave': 62073,
# 'refrigerator': 62073,
# 'washer_dryer': 5373

#FP = [58573, 8349, 45844, 62073, 62073, 5373]

#False negatives
# 'bathroom_gfi': 14436,
# 'dishwasher': 204728,
# 'lighting': 77979,
# 'microwave': 2,
# 'refrigerator': 0,
# 'washer_dryer': 220458

#FN = [14436, 204728, 77979, 2, 0, 220458]

#REDD House 2 Main 1 metrics with the other parameters
#True positives
# 'dishwasher': 60091,
# 'kitchen_outlets': 12909,
# 'lighting': 0,
# 'microwave': 7,
# 'refrigerator': 0,
# 'stove': 28537

#TP = [60091, 12909, 0, 7, 0, 28537]

#True negatives
# 'dishwasher': 90936,
# 'kitchen_outlets': 201571,
# 'lighting': 324179,
# 'microwave': 324185,
# 'refrigerator': 324113,
# 'stove': 173735

#TN = [90936, 201571, 324179, 324185, 324113, 173735]

#False positives
# 'dishwasher': 4746,
# 'kitchen_outlets': 51928,
# 'lighting': 64837,
# 'microwave': 64830,
# 'refrigerator': 64837,
# 'stove': 36300

#FP = [4746, 51928, 64837, 64830, 64837, 36300]

#False negatives
# 'dishwasher': 233249,
# 'kitchen_outlets': 122614,
# 'lighting': 6,
# 'microwave': 0,
# 'refrigerator': 72,
# 'stove': 150450

#FN = [233249, 122614, 6, 0, 72, 150450]

#REDD House 2 Main 2 metrics with the other parameters
#True positives
# 'dishwasher': 58278,
# 'kitchen_outlets': 25249,
# 'lighting': 3,
# 'microwave': 0,
# 'refrigerator': 0,
# 'stove': 29737

#TP = [58278, 25249, 3, 0, 0, 29737]

#True negatives
# 'dishwasher': 78836,
# 'kitchen_outlets': 201935,
# 'lighting': 324156,
# 'microwave': 324177,
# 'refrigerator': 324176,
# 'stove': 171777

#TN = [78836, 201935, 324156, 324177, 324176, 171777]

#False positives
# 'dishwasher': 6559,
# 'kitchen_outlets': 39588,
# 'lighting': 64834,
# 'microwave': 64837,
# 'refrigerator': 64837,
# 'stove': 35100

#FP = [6559, 39588, 64834, 64837, 64837, 35100]

#False negatives
# 'dishwasher': 245349,
# 'kitchen_outlets': 122250,
# 'lighting': 29,
# 'microwave': 8,
# 'refrigerator': 9,
# 'stove': 152408

#FN = [245349, 122250, 29, 8, 9, 152408]

#REDD House 6 Main 1 metrics with the other parameters
#True positives
#'electronics': 233, 
#'kitchen_outlets': 0, 
#'refrigerator': 4447, 
#'stove': 0

#TP = [65414, 66111, 53020, 66111]

#True negatives
# 'electronics': 65414,
# 'kitchen_outlets': 66111,
# 'refrigerator': 53020,
# 'stove': 66111

#TN = [65414, 66111, 53020, 66111]

#False positives
# 'electronics': 21804,
# 'kitchen_outlets': 22037,
# 'refrigerator': 17590,
# 'stove': 22037

#FP = [21804, 22037, 17590, 22037]

#False negatives
#'electronics': 697, 
#'kitchen_outlets': 0, 
#'refrigerator': 13091, 
#'stove': 0

#FN = [697, 0, 13091, 0]

#REDD House 6 Main 2 metrics with the other parameters
#True positives
# 'air_conditioning': 2,
# 'electric_heat': 0,
# 'electronics': 231,
# 'kitchen_outlets': 0,
# 'refrigerator': 3656,
# 'stove': 0

#TP = [2, 0, 231, 0, 3656, 0]

#True negatives
# 'air_conditioning': 110179,
# 'electric_heat': 110162,
# 'electronics': 109177,
# 'kitchen_outlets': 110185,
# 'refrigerator': 92555,
# 'stove': 110185

#TN = [110179, 110162, 109177, 110185, 92555, 110185]

#False positives
# 'air_conditioning': 22035,
# 'electric_heat': 22037,
# 'electronics': 21806,
# 'kitchen_outlets': 22037,
# 'refrigerator': 18381,
# 'stove': 22037

#FP = [22035, 22037, 21806, 22037, 18381, 22037]

#False negatives
# 'air_conditioning': 6,
# 'electric_heat': 23,
# 'electronics': 1008,
# 'kitchen_outlets': 0,
# 'refrigerator': 17630,
# 'stove': 0

#FN = [6, 23, 1008, 0, 17630, 0]

#REDD House 8 metrics with the other parameters
#True positives
#'freezer': 26533, 
#'microwave': 0, 
#'television_site': 85, 
#'toaster': 18257

#TP = [26533, 0, 85, 18257]

#True negatives
# 'freezer': 47741,
# 'microwave': 105981,
# 'television_site': 105977,
# 'toaster': 20218

#TN = [47741, 105981, 105977, 20218]

#False positives
# 'freezer': 8794,
# 'microwave': 35327,
# 'television_site': 35242,
# 'toaster': 17070

#FP = [8794, 35327, 35242, 17070]

#False negatives
#'freezer': 58240, 
#'microwave': 0, 
#'television_site': 4, 
#'toaster': 85763

#FN = [58240, 0, 4, 85763]
