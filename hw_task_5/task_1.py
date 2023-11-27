"""
1.	Создайте DataFrame с рандомными целыми числами от 1 до 10, размером 10х10.
"""

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(0,10,size=(10,10)))
print(df)