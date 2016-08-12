import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib.ticker as ticker
import datetime as dt
plt.style.use('ggplot')

def normalizeDataOld(filename):
    df = pd.read_excel(filename, ignore_index=True, parse_cols=[1,2,3,5,7], skiprows=range(0,7), names=['Site','Date',
                                                                                        'DO mg/L(Top)',
                                                                                        'FC #/mL(Top)',
                                                                                        'Enterococcus #/100mL(Top)'])
    dfBR1 = df[df['Site']=='BR1']
    dfBR3 = df[df['Site']=='BR3']
    dfBR5 = df[df['Site']=='BR5']

    return  dfBR1, dfBR3, dfBR5
    


dfBR1 = normalizeDataOld('harbor_sampling_ytd_2014.xls')[0]
dfBR3 = normalizeDataOld('harbor_sampling_ytd_2014.xls')[1]
dfBR5 = normalizeDataOld('harbor_sampling_ytd_2014.xls')[2]

dfBR1 = dfBR1.reset_index()
dfBR3 = dfBR3.reset_index()
dfBR5 = dfBR5.reset_index()

x = dfBR1['Date']
x = [dt.datetime.strptime(str(d)[:10],'%Y-%m-%d').date() for d in x]


#================Fecal Coliform================
ax1 = plt.subplot2grid((22,3), (7,0), rowspan=9, colspan=3)
y = dfBR1['FC #/mL(Top)']
y2 = dfBR3['FC #/mL(Top)']
#y3 = dfBR5['FC #/mL(Top)']
BR1line = ax1.plot(x, y, label = "Bronx River @ 231st", color = '#6dcff6', linewidth = 1.3, alpha=0.6)
BR3line = ax1.plot(x, y2, label = "Bronx River @ Westchester Ave", color = '#54b678', linewidth = 1.3, alpha=0.6)
#BR5line = ax1.plot(x, y3, label = "FC #/mL(Top)", color = 'g')
ax1.legend(ncol=1,prop={'size':8}).get_frame().set_alpha(0.4)
ax1.set_title('Fecal Coliform', fontsize=10)
ax1.set_ylabel('#/mL', fontsize=8)


#================Enterococcus====================
ax2 = plt.subplot2grid((22,3), (0,0), rowspan=5, colspan=3)
y = dfBR1['Enterococcus #/100mL(Top)']
y2 = dfBR3['Enterococcus #/100mL(Top)']
BR1line = ax2.plot(x, y, color = '#6dcff6', linewidth = 1.3, alpha=0.6)
BR3line = ax2.plot(x, y2, color = '#54b678', linewidth = 1.3, alpha=0.6)
#ax2.legend(ncol=1,prop={'size':8}).get_frame().set_alpha(0.4)
ax2.set_title('Enterococcus', fontsize=10)
ax2.set_ylabel('#/100mL', fontsize=8)


#================Dissolved Oxygen================
ax3 = plt.subplot2grid((22,3), (18,0), rowspan=4, colspan=3)
y = dfBR1['DO mg/L(Top)']
y2 = dfBR3['DO mg/L(Top)']
BR1line = ax3.plot(x, y, color = '#6dcff6', linewidth = 1.3, alpha=0.6)
BR3line = ax3.plot(x, y2, color = '#54b678', linewidth = 1.3, alpha=0.6)
ax3.yaxis.set_major_locator(ticker.MultipleLocator(2))
#ax3.legend(ncol=1,prop={'size':8}).get_frame().set_alpha(0.4)
ax3.set_title("Dissolved Oxygen", fontsize=10)
ax3.set_ylabel('mg/L', fontsize=8)




plt.show()










