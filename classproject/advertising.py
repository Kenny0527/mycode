"""
Author: Kramclam
This program renders an analytics dashboard with html and used Python \
    to help transform data from amazon advertising search term xlsx \
    reports. The Advertising class is used for manipulating \
    the data frame and rendering it to index.html file. \
"""
from database import *
class Advertising:
    """Initialization method. Declares fields and calls setter methods."""
    def __init__(self):
# ----------------------- INIT DATABASE CLASS -------------------------
        # array of dictionaries from database data
        self.data_base = Database()

# ----------------------- INIT TOTAL SPEND ----------------------------
        # total spend for all keywords
        self.total_spend = 0
        # initialize totalSpend with all spend from dataFrame
        self.set_total_spend()

# ----------------------- INIT TOTAL SALES ----------------------------
        # total sales for all keywords
        self.total_sales = 0
        # initialize totalSales with all sales from dataFrame
        self.set_total_sales()

    def set_total_spend(self):
        """This method call is to calculate and set the total spend."""
        seriesspend = 0
        try:
            for data_frame in (self.data_base.get_advertising_dataframe_list()):
                seriesspend += float(data_frame['Spend'].sum(axis=0, skipna=True))
            self.total_spend = seriesspend
        except KeyError as err:
            print(err.__traceback__ + "Error with file column names")
        except RuntimeError as err:
            print(err.__traceback__ + "Error with handling the data")

    def get_total_spend(self):
        """method that gets total spend"""
        return self.total_spend

    def set_total_sales(self):
        """method calculate the total sales and sets at init from dataFrame"""
        seriessales = 0
        try:
            for data_frame in (self.data_base.get_advertising_dataframe_list()):
                seriessales += float(data_frame['7 Day Total Sales '].sum(axis=0, skipna=True))
            self.total_sales = seriessales
        except KeyError as err:
            print(err.__traceback__ + "Error with file column names")
        except RuntimeError as err:
            print(err.__traceback__ + "Error with handling the data")

    def get_total_sales(self):
        """method that gets total sales"""
        return self.total_sales

    def get_head(self):
        """method to get the sorted head of the data frame"""
        try:
            return self.data_base.get_advertising_dataframe_list()[0] \
                .sort_values(by="7 Day Total Sales ", ascending=False) \
                    .head(10)
        except KeyError as err:
            print(err.__traceback__ + "Error with file column names")
        except RuntimeError as err:
            print(err.__traceback__ + "Error with handling the data")
        return None

    def get_head_search(self, name):
        """method to get the head of the dictionary with requested search pattern"""
        try:
            return self.data_base.get_advertising_dataframe_list()[0] \
                .where(self.data_base.get_advertising_dataframe_list()[0]['Campaign Name'] \
                    .str.contains(name)) \
                        .sort_values(by="7 Day Total Sales ", ascending=False) \
                            .head(10)
        except KeyError as err:
            print(err.__traceback__ + "Error with file column names")
        except RuntimeError as err:
            print(err.__traceback__ + "Error with handling the data")
        return None
