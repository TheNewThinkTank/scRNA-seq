"""Generate barplot of average cell type presence,
for all patients in data file.
Shown in descending order.
"""

import matplotlib.pyplot as plt  # type: ignore
import pandas as pd  # type: ignore
import seaborn as sns  # type: ignore

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
number_of_patients = len(df)

# EXAMPLE
# print(df['malignant_cell'].sum() / number_of_patients)

ser = df.apply(lambda x: x.sum() / number_of_patients)

ser = ser.sort_values(ascending=False)

print(ser)
# print(type(ser))  # <class 'pandas.core.series.Series'>
# print(ser.index)

plt.figure(figsize=(12, 6))
# sum of values (V) for given cell type divided by the number of patients (N)
y_label = r"$(\sum V) / N $"
plt.subplots_adjust(bottom=0.5)
ax = sns.barplot(x=ser.index, y=ser.values)
ax.set(xlabel="Cell Type", ylabel=y_label)
plt.xticks(rotation=90)
plt.ylabel(y_label, rotation=0)
ax.yaxis.set_label_coords(-0.1, 0.5)  # 1.02
# plt.show()
plt.savefig("barplot.png")
