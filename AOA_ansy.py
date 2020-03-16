import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

QAR_df=pd.read_csv('D:\\400-DataAnalys\\QAR_DATA\\B-602A_20200316_052027.csv',
                   usecols=['UTC','AOA1','AOA2','ALT_STD','ALT_STD2','LATG_L',
                            'LATG_R','CK_LDG_WOW','WOWL1','WOWL2','WOWN1','WOWN2',
                            'WOWR1','WOWR2','STICK_SHAKER','STICK_SHK_L','STICK_SHK_R'],
                   low_memory=False)
QAR_df['delta_AOA']=np.abs(QAR_df['AOA1']-QAR_df['AOA2'])
#QAR_df.to_csv('B-602A_0316_0753_done.csv',index=False)
sel_ALT=QAR_df.loc[QAR_df['ALT_STD']>=25000]
print('250高度下左右机身迎角平均差值为%f'%np.mean(sel_ALT['delta_AOA']))

plt.rcParams['xtick.direction']='in'
plt.rcParams['ytick.direction']='in'
plt.figure(figsize=(15,5),dpi=100)
plt.xlabel('Time')
plt.ylabel('delta_AOA')
plt.plot(sel_ALT['delta_AOA'],label='delta_AOA')
plt.axhline(0.365,c='r',label='Threshold Value')
plt.legend()
plt.show()

plt.rcParams['xtick.direction']='in'
plt.rcParams['ytick.direction']='in'
plt.figure(figsize=(15,5),dpi=100)
plt.xlabel('Time')
plt.ylabel('delta_AOA')
plt.plot(sel_ALT['ALT_STD'],label='Altitude')
plt.legend()
plt.show()
