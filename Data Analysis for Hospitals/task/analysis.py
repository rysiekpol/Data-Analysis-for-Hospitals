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
print("Data shape:",merged_data.shape)
print(merged_data.sample(n=20, random_state=30))