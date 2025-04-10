import pandas as pd
import numpy as np

df = pd.read_csv("/Users/aayansayed/Documents/CSCI - 420/HW_07_Sayed_DIR/Two_D_Data_For_Students_To_Check.csv")

# Assuming your CSV file has two columns.  Adjust if needed.
print("this is the data")
data = df.to_numpy().T
print(data)
print("\n")
covTest = np.cov(data)
print("this is the covariance matrix")
print(covTest)

