import pandas as pd
path = 'C:\\Users\\reny_\\Downloads\\test.csv'
df = pd.read_csv(path)
print(df)
# print(df["Name"])
print(df.nlargest(n = 2, columns = "M1 Score"))