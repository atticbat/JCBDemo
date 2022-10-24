# Static container program

#from dynamic import *
from flask import Flask, render_template

app = Flask(__name__)
@app.route("/", methods=['GET'])
def home():
    return render_template("home.html", x=generatedDataFrame)
#not sure how I get generatedDataFrame from dynamic main here

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
