import pyexcel
import os
import pandas as pd
# Class called Database
class Database:
    def __init__(self):

        self.directory = 'static/db'

        self.data_frames = []

        self.readXlsx_to_DataFrame()
        
    # read xlsx files into container, xls to dictionary conversion
    def readXlsx_to_DataFrame(self):
        ads = []
        for filename in os.scandir(self.directory):
            if filename.is_file():
                ads.append(pd.read_excel(filename))
        self.data_frames = ads
        return None

    def getAdvertisingDataFramesList(self):
        ads_data_set = []
        for table in self.data_frames:
            ads_data_set.append(table[['Campaign Name', 'Impressions', 'Cost Per Click (CPC)', 'Spend', '7 Day Total Sales ']])
        return ads_data_set

    def getAnalyticsDataFramesList(self):
        ads_data_set = []
        for table in self.data_frames:
            ads_data_set.append(table[['Targeting', 'Customer Search Term', 'Cost Per Click (CPC)', 'Spend', '7 Day Total Sales ']])
        return ads_data_set