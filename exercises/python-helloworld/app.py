from flask import Flask
from flask import json
import logging
app = Flask(__name__)

@app.route("/status")
def healthcheck():
    response = app.response_class(
	response = json.dumps({"result" : "Ok - healthy"}),
	status = 200,
	mimetype = 'application/json'
	)
    app.logger.info("Status Request Successful")
    return response
@app.route("/metrics")
def metrics():
    response = app.response_class(
	response = json.dumps({"status" : "success","code" : 200, "data": {"UserCount": 140,"UserCountActive" : 23}}),
	status = 200,
	mimetype = 'application/json'
	)
    app.logger.info("Metrics Request Successful")
    return response

@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    logging.basicConfig(filename='app.log', level=logging.DEBUG)
    app.run(host='0.0.0.0')
	
