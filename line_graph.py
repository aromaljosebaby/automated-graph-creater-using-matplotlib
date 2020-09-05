from matplotlib import pyplot as plt
import  numpy as np
import pandas as pd
def line_graph(x_axis_name,y_axis_name,graph_title,st_row,csv_file_path):
    data=pd.read_csv(csv_file_path)
    x_axis_data=data[st_row[0]]
    y_axis_data=data[st_row[1]]
    plt.plot(x_axis_data,y_axis_data)
    plt.style.use('fivethirtyeight')
    plt.title(graph_title)
    plt.xlabel(x_axis_name)
    plt.ylabel(y_axis_name)
    plt.tight_layout()
    plt.grid()
    plt.show()


#line_graph('Animals','Number','Bar Graph')

