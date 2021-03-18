import pandas as pd
from dash import Dash, dependencies
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.express as px
import quandl

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

quandl.ApiConfig.api_key = 'GN2Lh6r28oF_GXc1LXbj'

tickerlist = pd.read_csv('ticker_list.csv')
quandl_code = tickerlist.Quandl_Code.unique()

app.layout = html.Div([
    dcc.Dropdown(
        id="dropdown",
        options=[{"label": x, "value": x}
                 for x in quandl_code],
        value='EOD/MSFT'
    ),
    dcc.Graph(id="line-chart"),
])


@app.callback(
    Output("line-chart", "figure"),
    [Input("dropdown", "value")])
def update_line_chart(quandl_code):
    stockprices = quandl.get(quandl_code)
    print(stockprices, "for", quandl_code, )
    stockprices.reset_index(inplace=True)
    fig = px.line(stockprices,
                  x="Date", y="Close")
    return fig


app.run_server(debug=True)
