from flask import Flask, abort, render_template, jsonify, request
from api import prediction

app = Flask('VisaApp')

@app.route('/myvisa', methods=['POST'])
def do_prediction():
    if not request.json:
        abort(400)
    data = request.json

    response = prediction(data)

    return jsonify(response)

@app.route('/')
def index():
    return render_template('index.html')

app.run(debug=True)
