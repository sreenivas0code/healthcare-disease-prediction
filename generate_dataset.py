import pandas as pd
import random

data = []

for _ in range(1200):
    age = random.randint(20, 80)
    glucose = random.randint(70, 200)
    bp = random.randint(60, 120)
    bmi = round(random.uniform(18, 40), 1)
    insulin = random.randint(50, 200)

    disease = 1 if (glucose > 140 or bmi > 30 or age > 50) else 0

    data.append([age, glucose, bp, bmi, insulin, disease])

df = pd.DataFrame(
    data,
    columns=["age", "glucose", "bp", "bmi", "insulin", "disease"]
)

df.to_csv("dataset.csv", index=False)

print("Dataset created with rows:", len(df))
