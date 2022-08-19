#!/usr/bin/env python3
"""
Author: Kramclam
This program renders an analytics dashboard with html and used Python \
    to help transform data from amazon advertising search term xlsx \
    reports. The Server class is used to define the routes and related \
    html files. It also handles the packages needed to be rendered \
    with jinja
"""
from flask import Flask, render_template
from advertising import *
from analytics import *

app = Flask(__name__)
# Analytics and Advertising classes "has a" relationship with server.
# Both are declared here to handle their GET and POST routes
advertising = Advertising()
analytics = Analytics()

# ---------------------------------- APP GET ROUTES -------------------------------
@app.route("/")
@app.route("/dashboard", methods=['GET'])
def index():
    """method is used to build and render advertising data into index.html"""
    advertising_overview = []
    advertising_overview.append(round(float(advertising.get_total_spend()), 2))
    advertising_overview.append(round(float(advertising.get_total_sales()), 2))
    advertising_overview \
        .append(round(float(advertising.get_total_sales() - advertising.get_total_spend()), 2))
    return render_template('index.html', \
        index = advertising_overview, \
            tables = [advertising.get_head().to_html()], \
                titles=[''])

@app.route("/dashboard/<name>", methods=['GET'])
def campaign_search(name):
    """method is used to take in a name parameter. the name parameter is used to find \
        campaigns with its value as substrings. renders index.html with new campaign \
            data"""
    advertising_overview = []
    advertising_overview.append(round(float(advertising.get_total_spend()), 2))
    advertising_overview.append(round(float(advertising.get_total_sales()), 2))
    advertising_overview \
        .append(round(float(advertising.get_total_sales() - advertising.get_total_spend()), 2))
    return render_template('index.html', \
        index = advertising_overview, \
            tables = [advertising.get_head_search(name).to_html()], \
                titles=[''])

@app.route("/analytics", methods=['GET'])
def analytics_welcome():
    """method is used to build and render analytics data into analytics.html"""
    analytics_overview = []
    analytics_overview.append(round(float(analytics.get_kw_total_spend()), 2))
    analytics_overview.append(round(float(analytics.get_kw_total_sales()), 2))
    analytics_overview \
        .append(round(float(analytics.get_kw_total_sales() - analytics.get_kw_total_spend()), 2))
    return render_template('analytics.html', \
        index = analytics_overview, \
            tables = [analytics.get_kw_head().to_html()], \
                titles=[''])

@app.route("/analytics/<searchterm>", methods=['GET'])
def analytics_search(searchterm):
    """method is used to take in a searchterm parameter. the searchterm \
        parameter is used to find search terms with its value as substrings. \
        renders analytics.html with new search term data"""
    analytics_overview = []
    analytics_overview.append(round(float(analytics.get_kw_total_spend()), 2))
    analytics_overview.append(round(float(analytics.get_kw_total_sales()), 2))
    analytics_overview \
        .append(round(float(analytics.get_kw_total_sales() - analytics.get_kw_total_spend()), 2))
    return render_template('analytics.html', \
        index = analytics_overview, \
            tables = [analytics.get_kw_head_search(searchterm).to_html()], \
                titles=[''])

# ---------------------------------- APP POST ROUTES -------------------------------
@app.route("/analytics/searchterm", methods=['POST'])
def analytics_search_form(searchterm):
    """method is used to take in a searchterm parameter from form as POST. \
        the searchterm parameter is used to find search terms with its \
            value as substrings. renders analytics.html with new search \
                term data"""
    analytics_overview = []
    analytics_overview.append(round(float(analytics.get_kw_total_spend()), 2))
    analytics_overview.append(round(float(analytics.get_kw_total_sales()), 2))
    analytics_overview \
        .append(round(float(analytics.get_kw_total_sales() - analytics.get_kw_total_spend()), 2))
    return render_template('analytics.html', \
        index = analytics_overview, \
            tables = [analytics.get_kw_head_search(searchterm).to_html()], \
                titles=[''])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
