from flask import Flask, jsonify, render_template
import json
import looker_sdk
from looker_sdk.sdk.api40.methods import Looker40SDK 

app = Flask(__name__)

sdk: Looker40SDK = looker_sdk.init40()

@app.route('/data')
def get_data():
    result_str = sdk.run_look(
        look_id="172",
        result_format="json")
    result = json.loads(result_str)
    return jsonify(result)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
