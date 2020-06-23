#import the pandas library and aliasing as pd
import pandas as pd
import numpy as np
			#0     #1     #2      #3
data_array = np.array(['car1','car2','car3','car4'])

#split datas with pd.Series(parameter data)
#pd.Series(data_array) structure data for split output
#this is case array data for pd.Series(parameter data)

split_data_series = pd.Series(data_array)
print(split_data_series)
