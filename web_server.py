from flask_api import FlaskAPI
import get_data
import json
from flask import Flask, render_template, abort, request

app = FlaskAPI(__name__)

with open('./configuration.json') as con_file:
    config_file = json.load(con_file)
    allow_addr = config_file['allowlist']

@app.before_request
def limit_remote_addr():
    if request.remote_addr != allow_addr:
        abort(403)

@app.route("/<person>")
def main(person):
    result = get_data.main(person, config_file)
    result_json = json.loads(result)
    return render_template("index.html", person=person, result=result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
