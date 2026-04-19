import pandas as pd

df = pd.read_csv("dataset.csv")

sample = df.sample(frac=0.5, random_state=42)

print("Sample Data:")
print(sample)