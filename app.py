from flask import Flask, make_response, jsonify, request
from flask_cors import CORS, cross_origin
import quandl
import pandas as pd

app = Flask(__name__)
app.config['SECRET_KEY'] = "my secret key for testing environment"
CORS(app, resources={r"/api/*": {"origins": "*"}})
# app.config["CORS_HEADERS"]='Content-Type'

quandl.ApiConfig.api_key = 'GN2Lh6r28oF_GXc1LXbj'


@app.route('/api/tickerlist', methods=['GET'])
def get_tickerlist():
    tickers = pd.read_csv("ticker_list.csv")
    # ticker_dict = tickers[tickers['Quandl_Code'] == 'EOD/MSFT'].to_dict(orient='records')
    ticker_dict = tickers.to_dict(orient='records')
    response = make_response(jsonify({"data":ticker_dict}))
    # response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route('/api/eodstock', methods=['POST'])
def eod_stockprices():
    data = request.get_json()
    quandl_code = data.get('quandl_code', None)
    if quandl_code is not None:
        stockprices = quandl.get(quandl_code)
        stockprices.reset_index(inplace=True)
        stockprices_dict = stockprices.to_dict(orient='records')
        return make_response(jsonify({"data": stockprices_dict}), 200)
    else:
        return make_response(jsonify({"data": []}, 404))


if __name__ == '__main__':
    app.run(debug=True)
