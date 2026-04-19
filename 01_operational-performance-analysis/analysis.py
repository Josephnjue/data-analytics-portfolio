import pandas as pd

df = pd.read_csv("dataset.csv")

print("Summary Statistics:")
print(df.describe())

print("\nAccuracy by Worker:")
print(df.groupby("worker_id")["accuracy"].mean())

print("\nErrors by Task Type:")
print(df[df["status"]=="error"].groupby("task_type").size())