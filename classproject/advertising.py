import pyexcel
import os
import pandas as pd
# Class called advertising
class Advertising:
    def __init__(self):
        self.directory = '~/mycode/classproject/static/db'

    # read xlsx files into container, xls to dictionary conversion
    def readXlsx_to_json(self):
        for filename in os.scandir(self.directory):
            if filename.is_file():
                advertising_data.append(pd.read_excel(filename))
        return advertising_data
        
    # method that adds total spend

# method that adds total sales
# method that initializes spend, sales, acos, campaign insights
# method that sorts campaigns by greatest sales