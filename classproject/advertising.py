import pyexcel
import os
import pandas as pd
# Class called advertising
class Advertising:
    def __init__(self):
        self.directory = 'static/db'
        self.advertising_data = readXlsx_to_dataFrame()
        self.totalSpend = 0
        self.totalSales = 0
        self.overallAcos = 0

    # read xlsx files into container, xls to dictionary conversion
    def readXlsx_to_dataFrame(self):
        ads = []
        for filename in os.scandir(self.directory):
            if filename.is_file():
                ads.append(pd.read_excel(filename))
                print(ads)
        return ads
    
        
    # method that gets total spend
    def getTotalSpend(self):
        return self.totalSpend

    # method that gets total sales
    def getTotalSales(self):
        return self.totalSales