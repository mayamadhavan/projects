from flask import Flask, abort, render_template, jsonify, request
from api import prediction

app = Flask('CollegeApp')

def fill_in_dict(data, response, key):
    if data.get(key, ''):
        response[key] = prediction(data[key])
    else:
        response[key] = ''

@app.route('/myapp', methods=['POST'])
def do_prediction():
    if not request.json:
        abort(400)
    data = request.json

    response = {}
    fill_in_dict(data, response, 'reach_schools')
    fill_in_dict(data, response, 'target_schools')
    fill_in_dict(data, response, 'safety_schools')
    return jsonify(response)

@app.route('/')
def index():
    return render_template('index.html')

app.run(debug=True)
