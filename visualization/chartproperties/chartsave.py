import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,10)
y = x ^ 2

#Label Configure
plt.title("Graph Drawing") #Drawing Graph
plt.xlabel("Time")         #Time Graph
plt.ylabel("Distance")     #Distance Graph

#Plot Graph
plt.plot(x,y,"r")          #Line and Collor
plt.plot(x,y,">")	   #Line Type

#Save in pdf format
plt.savefig("Timevsdist.pdf", format="pdf")
