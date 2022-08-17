import pyexcel
import os
import pandas as pd
# Class called Analytics
class Analytics:
    def __init__(self):
        # directory with the advertising database
        self.directory = 'static/db'
# ----------------------- INIT DATA DICT -----------------------------
        # array of dictionaries, advertising data
        self.advertising_data = []
        # initialize advertising_data from the xlsx files
        self.readXlsx_to_dataFrame()
        print(self.advertising_data)

# ----------------- INIT KW W/ Most Sales Total ----------------------------
        # total spend for all keywords
        self.totalSpend = 0
        # initialize totalSpend with all spend from dataFrame
        self.setTotalSpend()

# ----------------- INIT KW W/ Most Spend Total ----------------------------
        # total sales for all keywords
        self.totalSales = 0
        # initialize totalSales with all sales from dataFrame
        self.setTotalSales()

    # read xlsx files into container, xls to dictionary conversion
    def readXlsx_to_dataFrame(self):
        ads = []
        for filename in os.scandir(self.directory):
            if filename.is_file():
                ads.append(pd.read_excel(filename)[['Campaign Name', 'Impressions', 'Cost Per Click (CPC)', 'Spend', '7 Day Total Sales ']])
        self.advertising_data = ads
        return None
    
    # calculate the total value of the key with highest spend
    def setKwTotalSpend(self):
        for table in self.advertising_data:
            table.str.find('honey', start)
        return None

    # method that gets total spend
    def getTotalSpend(self):
        return self.totalSpend


    # calculate the total spend at init from dataFrame
    def setTotalSales(self):
        sumsales = 0
        for data_set in self.advertising_data:
            seriessales = data_set.sum(axis=0, skipna=True)
            sumsales += float(seriessales['7 Day Total Sales '])
        self.totalSales = sumsales
        return None

    # method that gets total sales
    def getTotalSales(self):
        return self.totalSales

    # method to get the head of the dictonary
    def getHead(self):
        return self.advertising_data[0].sort_values(by="7 Day Total Sales ", ascending=False).head(6)