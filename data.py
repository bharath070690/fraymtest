import pandas as pd
import plotly.graph_objs as go
import quandl



def eod_stock_price_by_ticker(code):
    stockprices = quandl.get(code)
    stockprices.reset_index(inplace=True)
    stockprices_dict = stockprices.to_dict(orient='records')