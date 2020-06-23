import pandas as pd

base_data  = {"Name":['Marie', 'Carlos', 'José', 'Jhon'], 'Age':[15,24,67,42]}

#data  frame is a two dimensional data scructure, line and columns
#cread data frame following constructor pandas.DataFrame(data,index,columns,dtype,copy)
data_frame = pd.DataFrame(base_data, index=['1', '2', '3', '4'])
print(data_frame)
