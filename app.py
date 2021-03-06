import os
from flask import Flask, request

app = Flask(__name__)
cloudName = os.getenv('CLOUD_LOCATION')
__version__ = '0.1.5'

@app.route("/", methods=["GET"])
def homepage():
    if request.method == "GET":
        return "Hello World from {0} \n Version: {1} \n\n".format(cloudName, __version__)

#PORT = int(os.environ.get("PORT", 8080))
PORT = 8080
if __name__ == '__main__':
    app.run(threaded=True,host='0.0.0.0',port=PORT)