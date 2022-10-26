# Static container program

from flask import Flask, render_template

app = Flask(__name__)
@app.route("/", methods=['GET'])
def home():
    return render_template("home.html") #, x=generatedDataFrame)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
