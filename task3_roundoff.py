import os
import numpy as np
import pandas as pd
#import csv file
csv_file=pd.read_csv("C:\Users\Khushboo 13\Desktop\8th SEM\Elucidata\dataset.csv")
df=pd.read_csv("dataset.csv")
#round off
df['rounded_time']=np.rint(df['Retention time (min)'])
df['rounded_time']
