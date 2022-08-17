#!/usr/bin/env python3
from advertising import *
from flask import Flask, render_template, request, redirect
import jinja2
import math

app = Flask(__name__)
# app.config['DEBUG'] = True
advertising = Advertising()

@app.route("/", methods=['GET'])
def index():
    ads_overview = []
    ads_overview.append(float(advertising.getTotalSpend()).__round__())
    ads_overview.append(float(advertising.getTotalSales()).__round__())
    ads_overview.append(advertising.getHead())
    print(str(ads_overview[2]['Start Date'].name))
    return render_template('index.html', index = ads_overview)

@app.route("/analytics", methods=['GET'])
def analytics():
    return render_template('analytics.html', analytics = advertising)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
