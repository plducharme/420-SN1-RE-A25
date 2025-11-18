import pandas as pd

# importe le csv
dataframe = pd.read_csv("Water-Qual-Eau-Sites-National.csv", sep=",")

print(dataframe["PROV_TERR"])

print(dataframe.info())
