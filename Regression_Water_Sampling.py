#I tried using pandas, but this was before I did some tutorials. I do like the 'csv' library though
#import pandas as pd
import csv
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
import datetime as dt

#Changes the plot style to a similar style from the R language
plt.style.use('ggplot')


Data = []
Data2 = []
Data3 = []
Data4 = []
dataList = [Data, Data2, Data3, Data4]

#Opens the csv file I created from the .xls (Pandas was able to help me there)
with open('HarborSAMP.csv', 'rb') as csvfile:
    content = csv.reader(csvfile)
    for row in content:
        #Changing one of the headers, and adding Percent Change (basically the percent the levels changed from each marked date)
        if row[0] == 'Site':
            row[2] = "Fecal Coliform #/mL"
            row.append("% Change")
            for data in dataList:
                data.append(row)
        #The Hard coded sites, I already told you(Jarmaine) what I'm going to do with it
        if row[0] == 'BR3':
            row[1] = row[1][:10]
            Data.append(row)
        if row[0] == 'BR1':
            row[1] = row[1][:10]
            Data2.append(row)
        if row[0] == 'AC2':
            row[1] = row[1][:10]
            Data3.append(row)
        if row[0] == 'AC1':
            row[1] = row[1][:10]
            Data4.append(row)
#This is simply just obtaining the percent change for each date
for data in dataList:
    new = 1
    old = 2
    n = len(data)

    while n >= 0:
        try:
            pct_change =(float(data[new][2])-float(data[old][2]))/float(data[old][2])*100.0
            data[new].append(pct_change)
            print data[new]
            new +=1
            old +=1
            n -= 1
            
            
        except:
            break


#Plotting all 4 on 1 grid 
ax1 = plt.subplot2grid((12,2), (0,0), rowspan=12, colspan=2)


#Just grabbing the dates (all are the same for each site, so I don't need ALL of the dates from each set. Kind of like a one size fits all situation)    
dates = [Data[1][1],Data[2][1],Data[3][1],Data[4][1],Data[5][1],Data[6][1],Data[7][1],Data[8][1],Data[9][1],Data[10][1],Data[11][1],Data[12][1]]

#Making the dates "plottable"
xs = [dt.datetime.strptime(d,'%Y-%m-%d').date() for d in dates[:12]]
#Grabbing each sets "Fecal Coliform" data and set them to variable
ys = [int(Data[1][2]),int(Data[2][2]),int(Data[3][2]),int(Data[4][2]),int(Data[5][2]),int(Data[6][2]),int(Data[7][2]),int(Data[8][2]),int(Data[9][2]),int(Data[10][2]),int(Data[11][2]),int(Data[12][2])]
ys2 = [int(Data2[1][2]),int(Data2[2][2]),int(Data2[3][2]),int(Data2[4][2]),int(Data2[5][2]),int(Data2[6][2]),int(Data2[7][2]),int(Data2[8][2]),int(Data2[9][2]),int(Data2[10][2]),int(Data2[11][2]),int(Data2[12][2])]
ys3 = [int(Data3[1][2]),int(Data3[2][2]),int(Data3[3][2]),int(Data3[4][2]),int(Data3[5][2]),int(Data3[6][2]),int(Data3[7][2]),int(Data3[8][2]),int(Data3[9][2]),int(Data3[10][2]),int(Data3[11][2]),int(Data3[12][2])]
ys4 = [int(Data4[1][2]),int(Data4[2][2]),int(Data4[3][2]),int(Data4[4][2]),int(Data4[5][2]),int(Data4[6][2]),int(Data4[7][2]),int(Data4[8][2]),int(Data4[9][2]),int(Data4[10][2]),int(Data4[11][2]),int(Data4[12][2])]


#Setting variables for each line.
line1 = ax1.plot(xs, ys)#, xs, ys2, xs, ys3, xs, ys4)
line2 = ax1.plot(xs, ys2)
line3 = ax1.plot(xs, ys3)
line4 = ax1.plot(xs, ys4)

#Setting colors for each line
plt.setp(line1, color = 'g', linewidth = 1.3)
plt.setp(line2, color = 'r', linewidth = 1.3)
plt.setp(line3, color = 'b', linewidth = 1.3)
plt.setp(line4, color = 'c', linewidth = 1.3)

#Slanting the Date(X-axis)
for label in ax1.xaxis.get_ticklabels():
    label.set_rotation(45)
#Adjusting the plot
plt.subplots_adjust(left=0.12, bottom=0.19, right=0.90, top=0.93, wspace=0.20, hspace=0.20)
plt.show()









