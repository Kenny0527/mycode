import pyexcel
import os
from database import *
import pandas as pd
# Class called advertising
class Advertising:
    def __init__(self):
        # directory with the advertising database
        self.directory = 'static/db'

# ----------------------- INIT DATA DICT -----------------------------
        # array of dictionaries from database data
        self.db = Database()

# ----------------------- INIT TOTAL SPEND ----------------------------
        # total spend for all keywords
        self.totalSpend = 0
        # initialize totalSpend with all spend from dataFrame
        self.setTotalSpend()

# ----------------------- INIT TOTAL SALES ----------------------------
        # total sales for all keywords
        self.totalSales = 0
        # initialize totalSales with all sales from dataFrame
        self.setTotalSales()
    
    # calculate the total spend at init from dataFrame
    def setTotalSpend(self):
        seriesspend = 0
        for data_frame in (self.db.getAdvertisingDataFramesList()):
            seriesspend += float(data_frame['Spend'].sum(axis=0, skipna=True))
        self.totalSpend = seriesspend
        return None

    # method that gets total spend
    def getTotalSpend(self):
        return self.totalSpend


    # calculate the total spend at init from dataFrame
    def setTotalSales(self):
        seriessales = 0
        for data_frame in (self.db.getAdvertisingDataFramesList()):
            seriessales += float(data_frame['7 Day Total Sales '].sum(axis=0, skipna=True))
        self.totalSales = seriessales
        return None

    # method that gets total sales
    def getTotalSales(self):
        return self.totalSales

    # method to get the head of the dictonary
    def getHead(self):
        return self.db.getAdvertisingDataFramesList()[0] \
            .sort_values(by="7 Day Total Sales ", ascending=False) \
                .head(10)
