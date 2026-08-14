import pandas as pd
from ucimlrepo import fetch_ucirepo

# fetch dataset
iris = fetch_ucirepo(id=53)

# data (as pandas dataframes)
X = iris.data.features
y = iris.data.targets
print("total number of records",len(X))
print()

df=pd.DataFrame(iris.data.targets)
print("total number of different flower available",len(df.groupby(df["class"]).mean()))
df1=df.groupby(df["class"]).sum()
print(df1)
