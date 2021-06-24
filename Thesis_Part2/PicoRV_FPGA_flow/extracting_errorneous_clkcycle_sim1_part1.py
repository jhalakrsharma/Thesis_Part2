import pandas as pd
import os
import csv
import subprocess
import random
import glob
from tqdm import tqdm

final_compare = pd.DataFrame()
#--------------------------------------------------------------------------------
# Extracting the line at which enable is 1
for faulty_csv in tqdm(glob.glob('./csv_results_sim1/*.csv')):
    print(faulty_csv) #prints the name of csv

    splitted = faulty_csv.split("_")
    # print(splitted)
    cpureg = splitted[3] + "_" + splitted[4]
    # print(cpureg)
    # print(cpureg)
    # identifier = faulty_csv.split("_", 1)[1].split(".")[0]
    # print(identifier)
    # rows = []

    sf = pd.read_csv(faulty_csv)
    sf = sf.loc[sf['enable'] == 1]
    # print(sf.head())
    # print("---")
    # Clock cycle at which error was enabled *
    time_en = sf.iloc[0,0]
    cf = pd.read_csv('golden_sim1.csv')
    #print(cf.head())
# #-----------------------------------------------------------------------------------
    #df = pd.read_csv(faulty_csv)
    for clock in range(0,100,10): #(start, end, step size)
        # print(clock)
        rows = pd.DataFrame()
        temp_df = pd.DataFrame()
        time_outf = time_en + clock
        df = pd.read_csv(faulty_csv)
        df = df.loc[df['clk'] == time_outf].reset_index(drop = True)
        # print("---")
        df = df.iloc[:,:]
        # print("###")
        #print(df.head())
        #---------------------------------------------------------------------------------
        # Reading the golden values

        #cf = golden.copy()
        gold = cf[cf["clk"] == time_outf].reset_index(drop = True)
        # print(gold)
        gold = gold.iloc[:,1:]

#     # ---------------------------------------------------------------------------------
#     # appending all values in order to form a row

        # rows.append(identifier)
        # rows.append(cpureg)
        # print(rows)
        #print(identifier, cpureg)
        # rows["identifier"] = [identifier]
        rows["cpuregs"] = [cpureg]
        temp_df = pd.concat([rows, df, gold], axis = 1)
        
        final_compare = final_compare.append(temp_df)
        # # #---------------------------------------------------------------------------------
final_compare = final_compare.reset_index(drop = True)
final_compare.to_csv("inter_sim1_2.csv", index =False)




