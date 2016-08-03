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
ax1 = plt.subplot2grid((12,2), (1,0), rowspan=4, colspan=1)
ax2 = plt.subplot2grid((12,2), (7,0), rowspan=4, colspan=1)
ax3 = plt.subplot2grid((12,2), (1,1), rowspan=4, colspan=1)
ax4 = plt.subplot2grid((12,2), (7,1), rowspan=4, colspan=1)

ax1.grid(True)
ax2.grid(True)
ax3.grid(True)
ax4.grid(True)

#Slanting the X-axis (dates)
for label in ax1.xaxis.get_ticklabels():
    label.set_rotation(45)
for label in ax2.xaxis.get_ticklabels():
    label.set_rotation(45)
for label in ax3.xaxis.get_ticklabels():
    label.set_rotation(45)
for label in ax4.xaxis.get_ticklabels():
    label.set_rotation(45)

#Just grabbing the dates (all are the same for each site, so I don't need ALL of the dates from each set. Kind of like a one size fits all situation)    
dates = [Data[1][1],Data[2][1],Data[3][1],Data[4][1],Data[5][1],Data[6][1],Data[7][1],Data[8][1],Data[9][1],Data[10][1],Data[11][1],Data[12][1]]

#Making the dates "plottable"
xs = [dt.datetime.strptime(d,'%Y-%m-%d').date() for d in dates[:12]]
#Grabbing each sets "Fecal Coliform" data and set them to variable
ys = [int(Data[1][2]),int(Data[2][2]),int(Data[3][2]),int(Data[4][2]),int(Data[5][2]),int(Data[6][2]),int(Data[7][2]),int(Data[8][2]),int(Data[9][2]),int(Data[10][2]),int(Data[11][2]),int(Data[12][2])]
ys2 = [int(Data2[1][2]),int(Data2[2][2]),int(Data2[3][2]),int(Data2[4][2]),int(Data2[5][2]),int(Data2[6][2]),int(Data2[7][2]),int(Data2[8][2]),int(Data2[9][2]),int(Data2[10][2]),int(Data2[11][2]),int(Data2[12][2])]
ys3 = [int(Data3[1][2]),int(Data3[2][2]),int(Data3[3][2]),int(Data3[4][2]),int(Data3[5][2]),int(Data3[6][2]),int(Data3[7][2]),int(Data3[8][2]),int(Data3[9][2]),int(Data3[10][2]),int(Data3[11][2]),int(Data3[12][2])]
ys4 = [int(Data4[1][2]),int(Data4[2][2]),int(Data4[3][2]),int(Data4[4][2]),int(Data4[5][2]),int(Data4[6][2]),int(Data4[7][2]),int(Data4[8][2]),int(Data4[9][2]),int(Data4[10][2]),int(Data4[11][2]),int(Data4[12][2])]



#Making titles and plotting them
x,y = xs,ys
ax1.set_title("Bronx River @ Westchester Ave")
ax1.plot(x,y)

x,y = xs,ys2
ax2.set_title("Bronx River @ 231st")
ax2.plot(x,y)

x,y = xs,ys3
ax3.set_title("Alley Creek @ CSO Outfall")
ax3.plot(x,y)

x,y = xs,ys4
ax4.set_title("Alley Creek @ Northern Blvd")
ax4.plot(x,y)


#Adjusting the subplots (Make the graph full screen)
plt.subplots_adjust(left=0.09, bottom=0.11, right=0.94, top=1.00, wspace=0.20, hspace=0.20)
plt.show()









