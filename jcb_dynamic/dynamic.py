# Dynamic controls occur here

import configparser
import numpy as np
import pandas as pd

generatedDataFrame = {}

def get_df():
    config = configparser.ConfigParser()
    config.sections()
    config.read('../config.ini')
    while 1:
        data = np.random.randint(0, 100, size=int(config['DataTotal']['JCBDemo']))
        df = pd.DataFrame(data, columns=['a'])
        df['b'] = df.mod(10)
        generatedDataFrame = df.to_json(orient='records')
        time.sleep(0.5)
    return generatedDataFrame
