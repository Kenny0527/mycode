"""
Author: Kramclam
This program renders an analytics dashboard with html and used Python \
    to help transform data from amazon advertising search term xlsx \
    reports. The Database class is used to load the xlsx into a \
    data frame. The Dataframe is then filtered and passed to either \
    advertising or analytics class.
"""
import os
import pandas as pd
# Class called Database
class Database:
    """Initialization method. Declares fields and calls setter methods."""
    def __init__(self):
        # directory with the advertising database
        self.directory = 'static/db'

# ----------------------- INIT DATA DICT -----------------------------
        # array used to store dictionaries
        self.data_frames = []
        # reads xlsx files into data_frames
        self.read_xlsx_to_dataframe()

    def read_xlsx_to_dataframe(self):
        """read xlsx files into a list of panda dataframes"""
        ads = []
        try:
            for filename in os.scandir(self.directory):
                if filename.is_file():
                    ads.append(pd.read_excel(filename))
            self.data_frames = ads
        except RuntimeError as err:
            print(err.__traceback__ + "Error with handling the files")

    def get_advertising_dataframe_list(self):
        """method that gets the consolidated advertising dataframe list"""
        ads_data_set = []
        try:
            for table in self.data_frames:
                ads_data_set \
                    .append(table[['Campaign Name', \
                        'Impressions', \
                            'Cost Per Click (CPC)', \
                                'Spend', \
                                    '7 Day Total Sales ']])
        except KeyError as err:
            print(err.__traceback__ + "Error with file column names")
        except RuntimeError as err:
            print(err.__traceback__ + "Error with handling the data")
        return ads_data_set

    def get_analytics_dataframe_list(self):
        """method that gets the consolidated analytics dataframe list"""
        ads_data_set = []
        try:
            for table in self.data_frames:
                ads_data_set \
                    .append(table[['Targeting', \
                        'Customer Search Term', \
                            'Cost Per Click (CPC)', \
                                'Spend', \
                                    '7 Day Total Sales ']])
        except KeyError as err:
            print(err.__traceback__ + "Error with file column names")
        except RuntimeError as err:
            print(err.__traceback__ + "Error with handling the data")
        return ads_data_set
