import pandas as pd

data = pd.read_csv("compare_with_regs_paper2.csv")
# data["clk"] = [*range(0, len(data), 1)]
#data.insert(0, 'clk', [*range(0, len(data), 1)])
# print(data.head())
# print(data.tail())

data1 = data.iloc[::10,:]
# print(type(data1))
# print(data1)
# print(data1.tail())
data1.to_csv("compare_with_regs_paper2_removed_duplicate.csv", index = False)