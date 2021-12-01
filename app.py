import os
from flask import Flask, request

app = Flask(__name__)
cloudName = os.getenv('CLOUD_LOCATION')

@app.route("/", methods=["GET"])
def homepage():
    if request.method == "GET":
        return "Hello World from {0}".format(cloudName)

#PORT = int(os.environ.get("PORT", 8080))
PORT = 8080
if __name__ == '__main__':
    app.run(threaded=True,host='0.0.0.0',port=PORT)