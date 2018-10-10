import os
import numpy as np
import pandas as pd
csv_file=pd.read_csv("C:\Users\Khushboo 13\Desktop\8th SEM\Elucidata\dataset.csv")
df=pd.read_csv("dataset.csv")
df['rounded_time']=abs(np.rint(df['Retention time (min)']))
dfsorted=df.sort_values('rounded_time')
#take avg of all cols using rounded time
avg = dfsorted.groupby('rounded_time').mean().reset_index()
avg['avg']=avg.mean(axis=1)
print avg
