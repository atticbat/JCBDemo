# Dynamic controls occur here

import configparser
import numpy as np
import pandas as pd

from flask import Flask, render_template
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, support_credentials=True)
generatedDataFrame = {}

@app.route("/data", methods=['GET'])
@cross_origin(supports_credentials=True)
def get_df():
    config = configparser.ConfigParser()
    config.sections()
    config.read('../config.ini')
    data = np.random.randint(0, 100, size=int(config['DataTotal']['JCBDemo']))
    df = pd.DataFrame(data, columns=['a'])
    df['b'] = df.mod(10)
    generatedDataFrame = df.to_json(orient='records')
    return generatedDataFrame

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
