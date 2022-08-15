#!/usr/bin/python3

import pandas as pd

def json_to_csv():
    df = pd.read_json("5movies.json")
    df.to_csv("5movies-translated-from-json.csv")
    return None

def json_to_excel():
    df = pd.read_json("5movies.json")
    df.to_excel("5movies-translated-from-json.xlsx")
    return None

def csv_to_json():
    df = pd.read_csv("5movies.csv")
    df.to_json("5movies-translated-from-csv.json")
    return None


def main():
    # create a dataframe ciscocsv
    ciscocsv = pd.read_csv("ciscodata.csv")
    # create a dataframe ciscojson
    ciscojson = pd.read_json("ciscodata2.json")

    # The line below concats and reapplies the index value
    ciscodf = pd.concat([ciscocsv, ciscojson], ignore_index=True, sort=False)
    
    ## export to json
    ## do not include index number
    ciscodf.to_json("combined_ciscodata.json", orient="records")

    ## export to csv
    ## do not include index number
    ciscodf.to_csv("combined_ciscodata.csv", index=False)
    
    ## export to Excel
    ## do not include index number to xls
    ciscodf.to_excel("combined_ciscodata.xls", index=False)
    ## do not include index number to xlsx
    ciscodf.to_excel("combined_ciscodata.xlsx", index=False)
    
    ## create a python dictionary
    ## do not include index number
    x = ciscodf.to_dict(orient='records')
    print(x)
    
if __name__ == "__main__":
    main()

