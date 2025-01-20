import pandas as pd
import numpy as np

my_data = np.array([[0, 3], [10, 7], [20, 9], [30, 14], [40, 15]])
mycol = ['Temperature', 'Activity'] 

df = pd.DataFrame(data=my_data, columns=mycol)

df['adjusted'] = df['Activity'] + 2

print(df)
print("Rows #0, #1, and #2:")
print(df.head(3), '\n')
