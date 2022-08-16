import pyexcel
import os
import pandas as pd
# Class called advertising
class Advertising:
    def __init__(self):
        self.directory = 'static/db'
        self.advertising_data = []
    # read xlsx files into container, xls to dictionary conversion
    def readXlsx_to_dataFrame(self):
        for filename in os.scandir(self.directory):
            if filename.is_file():
                self.advertising_data.append(pd.read_excel(filename))
                print(self.advertising_data)
        return None

    def getAdvertising_data(self):
        return self.advertising_data
        
    # method that adds total spend

# method that adds total sales
# method that initializes spend, sales, acos, campaign insights