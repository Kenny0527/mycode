#!/usr/bin/env python3
from advertising import *
from flask import Flask, render_template

server = Flask(__name__)

@server.route("/")
def index():
    advertsing = Advertising()
    advertsing.readXlsx_to_dataFrame()
    
    return render_template("index.html")


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=2224)
