import pandas as pd
import numpy as np

pd.set_option("display.max_columns", 8)
general = pd.read_csv("test/general.csv")
prenatal = pd.read_csv("test/prenatal.csv")
sports = pd.read_csv("test/sports.csv")

prenatal.rename(columns={"HOSPITAL": "hospital", "Sex":"gender"}, inplace=True)
sports.rename(columns={"Hospital": "hospital", "Male/female":"gender"}, inplace=True)
merged_data = pd.concat([general, prenatal, sports], ignore_index=True)
merged_data.drop(columns="Unnamed: 0", inplace=True)
merged_data.dropna(axis = 0, how='all', inplace=True)
merged_data.replace({"female": "f", "woman": "f", "male": "m", "man": "m"}, inplace=True)
merged_data["gender"].fillna("f", inplace=True)
merged_data.fillna(0, inplace=True)

number_of_patients = merged_data.hospital.value_counts().sort_values(ascending=False)
stomach_share = merged_data[merged_data.hospital == "general"].diagnosis.value_counts().loc["stomach"]/merged_data[merged_data.hospital == "general"].shape[0]
dislocation_share = merged_data[merged_data.hospital == "sports"].diagnosis.value_counts().loc["dislocation"]/merged_data[merged_data.hospital == "sports"].shape[0]
median_difference = merged_data[merged_data.hospital == "general"].age.median() - merged_data[merged_data.hospital == "sports"].age.median()
blood_rate = merged_data.pivot_table(index="hospital", columns="blood_test", values="age", aggfunc="count")["t"].sort_values(ascending=False)

print("The answer to the 1st question is", number_of_patients.index[0])
print("The answer to the 2nd question is", round(stomach_share,3))
print("The answer to the 3rd question is", round(dislocation_share,3))
print("The answer to the 4th question is", int(median_difference))
print(f"The answer to the 5th question is {blood_rate.index[0]}, {int(blood_rate[0])} blood tests")


