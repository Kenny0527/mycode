#!/usr/bin/env python3
from advertising import *
from analytics import *
from flask import Flask, render_template, request, redirect
import jinja2
import math

app = Flask(__name__)
# app.config['DEBUG'] = True

# Analytics and Advertising classes "has a" relationship with server. 
advertising = Advertising()
analytics = Analytics()

@app.route("/", methods=['GET'])
def index():
    advertising_overview = []
    advertising_overview.append(float(advertising.getTotalSpend()).__round__())
    advertising_overview.append(float(advertising.getTotalSales()).__round__())
    return render_template('index.html', \
        index = advertising_overview, \
            tables = [advertising.getHead().to_html()], \
                titles=[''])

@app.route("/analytics", methods=['GET'])
def analytics_welcome():
    analytics_overview = []
    analytics_overview.append(float(analytics.getKwTotalSpend()).__round__())
    analytics_overview.append(float(analytics.getKwTotalSales()).__round__())
    return render_template('analytics.html', \
        index = analytics_overview, \
            tables = [analytics.getKwHead().to_html()], \
                titles=[''])

@app.route("/analytics/<searchterm>", methods=['GET'])
def analytics_search():
    analytics_overview = []
    analytics_overview.append(float(analytics.getKwTotalSpend()).__round__())
    analytics_overview.append(float(analytics.getKwTotalSales()).__round__())
    return render_template('analytics.html', \
        index = analytics_overview, \
            tables = [analytics.getKwHeadSearch(searchterm).to_html()], \
                titles=[''])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
