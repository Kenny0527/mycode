import pyexcel
import os
from database import *
import pandas as pd
# Class called Analytics
class Analytics:
    def __init__(self):
        # directory with the advertising database
        self.directory = 'static/db'

# ----------------------- INIT DATA DICT -----------------------------
        # array of dictionaries from database data
        self.db = Database()

# ----------------- INIT KW W/ Most Sales Total ----------------------------
        # total spend for all "Honey" related keywords
        self.kwTotalSpend = 0
        self.setKwTotalSpend()

        self.kwTotalSales = 0
        self.setKwTotalSales()
    
    # calculate the total value of the key with highest spend
    def setKwTotalSpend(self):
        seriesspend = 0
        for data_frame in (self.db.getAnalyticsDataFramesList()):
            seriesspend += float(data_frame['Spend'] \
                .where(data_frame['Customer Search Term'] \
                    .str.contains('honey')) \
                        .sum())
            # seriesspend += float(data_frame['Spend'].sum(axis=0, skipna=True))

        self.kwTotalSpend = seriesspend
        return None

    # method that gets total spend
    def getKwTotalSpend(self):
        return self.kwTotalSpend


    # calculate the total spend at init from dataFrame
    def setKwTotalSales(self):
        seriessales = 0
        for data_frame in (self.db.getAnalyticsDataFramesList()):
            seriessales += float(data_frame['7 Day Total Sales '] \
                .where(data_frame['Customer Search Term'] \
                    .str.contains('honey')) \
                        .sum())
        self.kwTotalSales = seriessales
        return None

    # method that gets total sales
    def getKwTotalSales(self):
        return self.kwTotalSales

    # method to get the head of the dictonary
    def getKwHead(self):
        return self.db.getAnalyticsDataFramesList()[0] \
            .where(self.db.getAnalyticsDataFramesList()[0]['Customer Search Term'] \
                .str.contains('honey')) \
                    .sort_values(by="7 Day Total Sales ", ascending=False) \
                        .head(10)

    # method to get the head of the dictionary with requested search pattern
    def getKwHeadSearch(self, searchterm):
        return self.db.getAnalyticsDataFramesList()[0] \
            .where(self.db.getAnalyticsDataFramesList()[0]['Customer Search Term'] \
                .str.contains(searchterm)) \
                    .sort_values(by="7 Day Total Sales ", ascending=False) \
                        .head(10)