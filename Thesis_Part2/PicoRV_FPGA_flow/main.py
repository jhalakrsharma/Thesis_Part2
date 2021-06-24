import random
import glob
import os
import pandas as pd

with open('picorv_python_FPGA_flow.v', 'r') as k:
    lines = k.readlines()

register = range(1, 8) #range(1, 8)
bits = range(0, 32) #range(0, 32)


#Uncomment from 15 to 31 to generate faulty files. 

for i in register:
    for j in bits:
        for k in range(1, 10): # This is for 10 instance of single reg bit combo.
            clock = random.randint(6, 100)
            with open('./faulty_files/fault_' + str(i) + "_" + str(j) + "_" + str(clock) + "_" + str(k) + '.v', 'w') as m:
                for line in lines:
                    if "Placeholder(2) Fault Injection" in line:        
                        line = "        cpuregs[" + str(i) + "][" + str(j) + "] = cpuregs[" + str(i) + "][" + str(j) + "] ^ enable; \n"
                        m.write(line)
                    elif "Placeholder(1) for random number" in line:        
                        change = "        if(counter_enable == 32'd" + str(clock) + ")\n"
                        m.write(change)
                    else:
                        m.write(line)

## This takes all faulty files and perform verilog. If run multiple time without generating
## new faulty files, the results will come same.

all_faulty_files = glob.glob("./faulty_files/*.v")

# for file in all_faulty_files:
#     os.system("iverilog -o ./vcd/"+ file.split("\\")[1].split(".")[0] + " " + file)
#     os.system("vvp ./vcd/" + file.split("\\")[1].split(".")[0] + " > ./results/" + file.split("\\")[1].split(".")[0] + ".csv")

# all_result_file = glob.glob("./results/*.csv")

# # print(len(all_result_file))
# # print(all_result_file)

# for file in all_result_file:

#     splitted = file.split("_")
#     cpureg = "cpuregs[" + splitted[1] + "][" + splitted[2] + "]"

#     header_names = ["clk","cpuregs[1]","cpuregs[2]","cpuregs[3]","cpuregs[4]","cpuregs[5]","cpuregs[6]","cpuregs[7]","memory[0]","memory[1]","memory[2]","memory[3]","memory[4]","memory[5]","memory[6]","memory[7]","memory[8]","memory[9]","memory[10]","memory[11]","memory[12]","memory[13]","memory[14]","memory[15]","memory[16]","memory[17]","memory[18]","memory[19]","memory[20]","memory[21]","memory[22]","memory[23]","memory[24]","memory[25]","memory[26]","memory[27]","memory[28]","memory[29]","memory[30]","memory[31]","memory[32]","memory[33]","memory[34]","memory[35]","memory[36]","memory[37]","memory[38]","memory[39]","memory[40]","memory[41]","memory[42]","memory[43]","memory[44]","memory[45]","memory[46]","memory[47]","memory[48]","memory[49]","memory[50]","memory[51]","memory[52]","memory[53]","memory[54]","memory[55]","memory[56]","memory[57]","memory[58]","memory[59]","memory[60]","memory[61]","memory[62]","memory[63]","memory[64]","memory[65]","memory[66]","memory[67]","memory[68]","memory[69]","memory[70]","memory[71]","memory[72]","memory[73]","memory[74]","memory[75]","memory[76]","memory[77]","memory[78]","memory[79]","memory[80]","memory[81]","memory[82]","memory[83]","memory[84]","memory[85]","memory[86]","memory[87]","memory[88]","memory[89]","memory[90]","memory[91]","memory[92]","memory[93]","memory[94]","memory[95]","memory[96]","memory[97]","memory[98]","memory[99]","memory[100]","memory[101]","memory[102]","memory[103]","memory[104]","memory[105]","memory[106]","memory[107]","memory[108]","memory[109]","memory[110]","memory[111]","memory[112]","memory[113]","memory[114]","memory[115]","memory[116]","memory[117]","memory[118]","memory[119]","memory[120]","memory[121]","memory[122]","memory[123]","memory[124]","memory[125]","memory[126]","memory[127]","memory[128]","memory[129]","memory[130]","memory[131]","memory[132]","memory[133]","memory[134]","memory[135]","memory[136]","memory[137]","memory[138]","memory[139]","memory[140]","memory[141]","memory[142]","memory[143]","memory[144]","memory[145]","memory[146]","memory[147]","memory[148]","memory[149]","memory[150]","memory[151]","memory[152]","memory[153]","memory[154]","memory[155]","memory[156]","memory[157]","memory[158]","memory[159]","memory[160]","memory[161]","memory[162]","memory[163]","memory[164]","memory[165]","memory[166]","memory[167]","memory[168]","memory[169]","memory[170]","memory[171]","memory[172]","memory[173]","memory[174]","memory[175]","memory[176]","memory[177]","memory[178]","memory[179]","memory[180]","memory[181]","memory[182]","memory[183]","memory[184]","memory[185]","memory[186]","memory[187]","memory[188]","memory[189]","memory[190]","memory[191]","memory[192]","memory[193]","memory[194]","memory[195]","memory[196]","memory[197]","memory[198]","memory[199]","memory[200]","memory[201]","memory[202]","memory[203]","memory[204]","memory[205]","memory[206]","memory[207]","memory[208]","memory[209]","memory[210]","memory[211]","memory[212]","memory[213]","memory[214]","memory[215]","memory[216]","memory[217]","memory[218]","memory[219]","memory[220]","memory[221]","memory[222]","memory[223]","memory[224]","memory[225]","memory[226]","memory[227]","memory[228]","memory[229]","memory[230]","memory[231]","memory[232]","memory[233]","memory[234]","memory[235]","memory[236]","memory[237]","memory[238]","memory[239]","memory[240]","memory[241]","memory[242]","memory[243]","memory[244]","memory[245]","memory[246]","memory[247]","memory[248]","memory[249]","memory[250]","memory[251]","memory[252]","memory[253]","memory[254]","memory[255]","enable"]

#     temp = pd.read_csv(file, sep = ",", header=None)
 
#     temp.columns = header_names

#     temp.to_csv(file, sep = ",", index = False)