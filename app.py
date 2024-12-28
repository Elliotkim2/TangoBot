# import flast module
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# instance of flask application
app = Flask(__name__)

# home route that returns below text when root url is accessed
@app.route("/")
def hello_world():
    return render_template("index.html")

if __name__ == '__main__':  
   app.run(host="localhost", port=3000)