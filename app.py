import sys
import numpy as np
import pandas as pd


np.linspace(0, 100, 10)

z = 0
if z < 1:
    msg = "blep"
else:
    msg = "blup"

print(msg)

d = pd.DataFrame({"col1": [0, 1, 2, 3], "col2": [4, 5, 6, 7]})

d2 = pd.DataFrame({"col1": [0, 1, 2, 3], "col2": ["A", "B", "C", "D"]})
