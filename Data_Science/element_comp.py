import pandas as pd
import matplotlib.pyplot as plt
org_df=pd.read_csv('periodic_table.csv')
df=org_df.dropna()
print(df)
plt.figure(figsize=(12, 8))
plt.scatter(data=df,x='AtomicNumber',y='Electronegativity',c='AtomicNumber', cmap='viridis')
plt.title("Atomic Number versus Electronegativity.",loc='center')
plt.xlabel('Atomic Number')
plt.ylabel('Electronegativity')
for index,row in df.iterrows():
    plt.annotate(row['Symbol'],(row['AtomicNumber'],row['Electronegativity']),xytext=(5,5),textcoords='offset points')

plt.show()