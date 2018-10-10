import os
import numpy as np
import pandas as pd
csv_file=pd.read_csv("C:\Users\Khushboo 13\Desktop\8th SEM\Elucidata\dataset.csv")
df=pd.read_csv("dataset.csv")
#fill nan values with 0
df.fillna(0)
#separate datasets
df3=df[df['Accepted Compound ID'].str.contains('plasmalogen',na=False)]
df2=df[df['Accepted Compound ID'].str.contains('LPC',na=False)]
df1=df[df['Accepted Compound ID'].str.contains('PC',na=False)]

plasmalogen=df3
#remove any intersections
lpc=df2[~df2.isin(plasmalogen)].dropna()
df4=df1[~df1.isin(lpc)].dropna()
pc=df4[~df4.isin(df3)].dropna()

print("Plasmalogen")
print(plasmalogen)
print("---------------------------------***--------------------------------")
print("LPC")
print(lpc)
print("---------------------------------***--------------------------------")
print("PC")
print(pc)
print("---------------------------------***--------------------------------")

