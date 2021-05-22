import pandas as pd
import matplotlib.pyplot as plt

Workbook1 = "higado.xlsx"

df = pd.read_excel(Workbook1)
print(df.head())
valores = df[["Title","Year"]]
print(valores)
ax=valores.plot.bar(x="Title", y="Year", rot=0, color="green" )

plt.show()
