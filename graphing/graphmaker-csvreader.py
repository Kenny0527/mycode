#!/usr/bin/python3

# from python std library
import csv

# python3 -m pip install np
import numpy as np
# python3 -m pip install matplotlib
import matplotlib
matplotlib.use('Agg')
# sudo apt install python3-tk
import matplotlib.pyplot as plt

# ----------------------- PARSE CSV DATA ------------------------

def parsecsvdata():
    """returns a list. [0] is LAN and [1] WAN data"""
    summary = [] # list that will contain [(LAN), (WAN)]

    # open csv data
    with open("/home/student/mycode/graphing/2018summary.csv",\
     "r") as downtime:
        # parse csv data with csv.reader
        downdata = csv.reader(downtime, delimiter=",")
        for row in downdata:
            rowdat = (int(row[0]), int(row[1]), int(row[2]), int(row[3]))
            summary.append(rowdat) # add dict to list
    return summary

# ------------------------- PLOT GRAPHS --------------------------

def plotgraphs(summary):
    N = 4
    localnetMeans = summary[0] # LAN data
    wanMeans = summary[1] # WAN data

    ind = np.arange(N)    # the x locations for the groups
    # the width of the bars: can also be len(x) sequence
    width = 0.35

    # describe where to display p1
    p1 = plt.bar(ind, localnetMeans, width)
    # stack p2 on top of p1
    p2 = plt.bar(ind, wanMeans, width, bottom=localnetMeans)

    # Describe the table metadata
    plt.ylabel("Tima after Lightning Strike (sec)")
    plt.title("2022 Florida Lightning Summary")
    plt.xticks(ind, ("L1", "L2", "L3", "L4"))
    plt.yticks(np.arange(0, 81, 10))
    plt.legend((p1[0], p2[0]), ("DANGER ZONE", "SAFE ZONE"))
    return plt

# ------------------------- MAIN -------------------------------

def main():
    ## grab our data
    summary = parsecsvdata() # grab our data
    plt = plotgraphs(summary)
    # SAVE the graph locally
    plt.savefig("/home/student/mycode/graphing/2018summaryv2.png")
    # Save to "~/static"
    plt.savefig("/home/student/static/2018summaryv2.png")       
    print("Graph created.")

# ------------------- RUN MAIN FUNCTION -------------------------

if __name__ == "__main__":
    main()

