import csv
import numpy as np
import pandas as pd
from SalesReader import run


'''
This function calculate min,max,avg of sales and appends into existing file.
'''
def write_data_to_csv():

    total, minSales,min_month, maxSales,max_month, avg = run()

    with open('sales_v1.csv', 'a+') as abc:
        csv_output = csv.writer(abc)
        csv_output.writerow([
            "A total {}".format(total), ",min {min_sales} sales in {month} month,".format(min_sales=min_month,month=minSales),
     ",max {max_key} sales in {month} month,".format(max_key=max_month,month=maxSales), 'Avg {}'.format(avg)])


'''
This function plot chart
'''
def plt_chart():
    import matplotlib.pyplot as plt
    df = pd.read_csv("sales.csv")
    xaxis = np.array(df.month)
    yaxis = np.array(df.sales)
    plt.plot(xaxis, yaxis)
    plt.show()


'''
This function reads from sales.csv and calculates pecentage changes and write to sales_v1.csv.
'''
def cal_pecentage_change():
    df = pd.read_csv("sales.csv")
    df["PecentageChange"] = (df.sales.pct_change()*100)
    df.to_csv('sales_v1.csv')
    print(df)
