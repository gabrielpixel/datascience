import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 10)
y = x ^ 2

#labeling
plt.title("Graph Drawing") #Graphic
plt.xlabel("Time")         #Time Graphic
plt.ylabel("Distance")     #Distance Graphic

plt.plot(x,y,'r') #formatting the line colors "r=red"
plt.plot(x,y,'>') #formattion the line type ">"
