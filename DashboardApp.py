import dash
from dash import dash_table
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
import seaborn as sns

import pandas as pd

data = pd.read_table('bank.csv',delimiter=";")
#data.head()

app =  dash.Dash(__name__)

fig1 = px.scatter(data, x = 'age', y = 'balance', color = 'job',)
vals = data['marital'].value_counts().tolist()
labels  = ['married', 'divorced', 'single']
fig2 = px.bar(x = labels, y= vals)
fig3 = px.pie(data , 'loan' , color = 'loan')
fig4 = px.imshow(data.corr())
fig5 = px.histogram(data,x = 'age' ,y = 'duration', color = 'loan', marginal = 'box')

app.layout = html.Div([
                       dcc.Graph(id = 'bubble', figure = fig1), 
                       dcc.Graph(id = 'bar', figure = fig2),
                       dcc.Graph(id = 'pie', figure = fig3),
                       dcc.Graph(id = 'correlation_matrix', figure= fig4),
                       dcc.Graph(id = 'histogram', figure = fig5),
                       dash_table.DataTable(id = 'table', columns = [{'name':i, 'id':i}
                                                                      for i in data.columns],
                                            data = data.head(20).to_dict('records'),)
])
if __name__ == '__main__':
  app.run_server( debug = True, port=3222)