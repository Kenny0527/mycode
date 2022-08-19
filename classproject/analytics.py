"""
Author: Kramclam
This program renders an analytics dashboard with html and used Python \
    to help transform data from amazon advertising search term xlsx \
    reports. The Analytics class is used for manipulating \
    the data frame and rendering it to analytics.html file. \
"""
from database import *
# Class called Analytics
class Analytics:
    """Initialization method. Declares fields and calls setter methods."""
    def __init__(self):
# ----------------------- INIT DATABASE CLASS -----------------------------
        # array of dictionaries from database data
        self.data_base = Database()

# ----------------- INIT KW HIGHEST TOTAL SPEND ----------------------------
        # total spend for all "Honey" related keywords
        self.kw_total_spend = 0
        # initialize totalSpend with all spend from dataFrame
        self.set_kw_total_spend()

# ----------------- INIT KW HIGHEST TOTAL SPEND ----------------------------
        # total spend for all "Honey" related keywords
        self.kw_total_sales = 0
        # initialize totalSales with all sales from dataFrame
        self.set_kw_total_sales()

    def set_kw_total_spend(self):
        """Method calculates the total value of the keyword with highest spend"""
        seriesspend = 0
        try:
            for data_frame in (self.data_base.get_analytics_dataframe_list()):
                seriesspend += float(data_frame['Spend'] \
                    .where(data_frame['Customer Search Term'] \
                        .str.contains('honey')) \
                            .sum())
            self.kw_total_spend = seriesspend
        except KeyError as err:
            print(err.__traceback__ + "Error with file column names")
        except RuntimeError as err:
            print(err.__traceback__ + "Error with handling the data")

    # method that gets total spend
    def get_kw_total_spend(self):
        """Method gets the highest keyword total spend"""
        return self.kw_total_spend

    def set_kw_total_sales(self):
        """Method calculate the total value of the keyword with higest sales"""
        seriessales = 0
        try:
            for data_frame in (self.data_base.get_analytics_dataframe_list()):
                seriessales += float(data_frame['7 Day Total Sales '] \
                    .where(data_frame['Customer Search Term'] \
                        .str.contains('honey')) \
                            .sum())
            self.kw_total_sales = seriessales
        except KeyError as err:
            print(err.__traceback__ + "Error with file column names")
        except RuntimeError as err:
            print(err.__traceback__ + "Error with handling the data")

    def get_kw_total_sales(self):
        """Method gets the highest keyword total sales"""
        return self.kw_total_sales

    def get_kw_head(self):
        """Method gets the head of the dataframe based on the search pattern 'honey'"""
        try:
            return self.data_base.get_analytics_dataframe_list()[0] \
                .where(self.data_base.get_analytics_dataframe_list()[0]['Customer Search Term'] \
                    .str.contains('honey')) \
                        .sort_values(by="7 Day Total Sales ", ascending=False) \
                            .head(10)
        except KeyError as err:
            print(err.__traceback__ + "Error with file column names")
        except RuntimeError as err:
            print(err.__traceback__ + "Error with handling the data")
        return None

    def get_kw_head_search(self, searchterm):
        """Method gets the head of the dataframe based on the search param"""
        try:
            return self.data_base.get_analytics_dataframe_list()[0] \
                .where(self.data_base.get_analytics_dataframe_list()[0]['Customer Search Term'] \
                    .str.contains(searchterm.lower())) \
                        .sort_values(by="7 Day Total Sales ", ascending=False) \
                            .head(10)
        except KeyError as err:
            print(err.__traceback__ + "Error with file column names")
        except RuntimeError as err:
            print(err.__traceback__ + "Error with handling the data")
        return None
