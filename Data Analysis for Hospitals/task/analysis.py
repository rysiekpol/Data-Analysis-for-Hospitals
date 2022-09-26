import pandas as pd
import numpy as np

pd.set_option("display.max_columns", 8)
general = pd.read_csv("test/general.csv")
prenatal = pd.read_csv("test/prenatal.csv")
sports = pd.read_csv("test/sports.csv")
print(general.head(20), prenatal.head(20), sports.head(20))
