"""_summary_
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv("data.txt", sep="\t")

df = df.drop(
    columns=[
        "Mixture",
        "P-value",
        "Correlation",
        "RMSE",
    ]
)

# print(df.head())
numbeer_of_patients = len(df)

# EXAMPLE
# print(df['malignant_cell'].sum() / numbeer_of_patients)

df = df.apply(lambda x: x.sum() / numbeer_of_patients)
print(df)

plt.figure(figsize=(12, 6))
# ax = df.plot.bar(
#     rot=90
#     )
plt.subplots_adjust(bottom=0.5)
sns.barplot(x=df.index, y=df.values)
plt.xticks(rotation=90)
# plt.show()
plt.savefig("barplot.png")
