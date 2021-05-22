import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_excel("Sala6.xlsx", index_col="CONCEPTO")

df1=df.groupby("DIAS").agg({"SEMANAL":"sum"})

print(df1.head(5))

grouped=df1

grouped["SEMANAL"].plot.pie()

plt.title("Gastos Diarios")


plt.show()






