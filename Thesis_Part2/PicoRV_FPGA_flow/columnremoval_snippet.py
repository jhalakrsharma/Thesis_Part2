import pandas as pd
import glob

print(len(glob.glob("./csv_results_sim1/*.csv")))

for faulty_csv in glob.glob("./csv_results_sim1/*.csv"):
    temp = pd.read_csv(faulty_csv)
    temp = temp.iloc[:, 3:].copy()
    # print(temp.head())
    column_list = [*temp.columns]
    for i in range(2, len(column_list)):
        #print(column_list[i])
        column_list[i] = column_list[i].split("]", 2)[0] + "]"
    #print(column_list)
    temp.columns = column_list
    # temp["clk"] = [*range(0, len(temp), 1)]
    temp.insert(0, 'clk', [*range(0, len(temp), 1)])
    temp1 = temp.iloc[::10,:]

    temp1.to_csv(faulty_csv, index = False)
    

