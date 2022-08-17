import pyexcel
import os
import pandas as pd
# Class called advertising
class Advertising:
    def __init__(self):
        # directory with the advertising database
        self.directory = 'static/db'
# ----------------------- INIT DATA DICT -----------------------------
        # array of dictionaries, advertising data
        self.advertising_data = []
        # initialize advertising_data from the xlsx files
        self.readXlsx_to_dataFrame()

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

    # read xlsx files into container, xls to dictionary conversion
    def readXlsx_to_dataFrame(self):
        ads = []
        for filename in os.scandir(self.directory):
            if filename.is_file():
                ads.append(pd.read_excel(filename))
        self.advertising_data = ads
        return None
    
    # calculate the total spend at init from dataFrame
    def setTotalSpend(self):
        sumspend = 0
        for data_set in self.advertising_data:
            seriesspend = data_set.sum(axis=0, skipna=True)
            sumspend += float(seriesspend['Spend'])
        self.totalSpend = sumspend
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
        return self.advertising_data[0].head()