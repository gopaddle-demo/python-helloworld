import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    # return "Hello World!"
    return "Welcome to Kube4All...!"

@app.route('/heartBeat')
def hello():
    return 'Alive!'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
