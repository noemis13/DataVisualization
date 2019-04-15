#pip install plotly
#pip install openpyxl
import plotly.plotly as py
import plotly.graph_objs as go

# Create random data with numpy
import numpy as np

py.sign_in('xaaaandao','xENHTp6A3hsh1ZPm1FDo')

from pyexcel_xlsx import get_data
#pip install pyexcel-xlsx
import json 

data = get_data("/home/todos/alunos/cm/a1510762/Downloads/db.xlsx")
print(json.dumps(data))

'''N = 1000
random_x = np.random.randn(N)
random_y = np.random.randn(N)

# Create a trace
trace = go.Scatter(
    x = random_x,
    y = random_y,
    mode = 'markers'
)

data = [trace]

# Plot and embed in ipython notebook!
py.iplot(data, filename='basic-scatter')'''
'''
a = (1, 2, 3, 4 ,5)
b = (2, 3, 5, 6, 1)

py.iplot(a,b)'''
