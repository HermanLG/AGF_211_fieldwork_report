import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


file = pd.read_csv("Core6.txt", delimiter="	")
print(file.keys())
print(file["End depth rate from top [cm]"])
sal = file["Salinity [g/kg]"][0]
val1 = file["Thickness val 1"][0]
val2 = file["Thickness val 2"][0]
val3 = file["Thickness val 3"][0]
val4 = file["Thickness val 4"][0]
print(np.mean([int(val1), int(val2), int(val3), int(val4)]))



