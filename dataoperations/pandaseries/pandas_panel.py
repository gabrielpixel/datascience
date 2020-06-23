import pandas as pd
import numpy as np
                               #random datas
data = {"Item1" : pd.DataFrame(np.random.randn(4,3)),
	"Item2" : pd.DataFrame(np.random.randn(4,2))}
panel = pd.Panel(data)
print(panel)
