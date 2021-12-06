import os
from flask import Flask, request

app = Flask(__name__)
cloudName = os.getenv('CLOUD_LOCATION')
__version__ = '0.1.1'

@app.route("/", methods=["GET"])
def homepage():
    if request.method == "GET":
        return "Hello World from {0} \n\n Version: {1}".format(cloudName, __version__)

#PORT = int(os.environ.get("PORT", 8080))
PORT = 8080
if __name__ == '__main__':
    app.run(threaded=True,host='0.0.0.0',port=PORT)