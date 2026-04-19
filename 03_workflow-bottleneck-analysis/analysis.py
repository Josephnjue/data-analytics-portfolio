import pandas as pd

df = pd.read_csv("dataset.csv")

print(df.mean())

df["total_time"] = df.sum(axis=1)

print("\nLongest stage:")
print(df[["stage_1_time","stage_2_time","stage_3_time"]].mean())