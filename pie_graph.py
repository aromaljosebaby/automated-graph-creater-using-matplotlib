from matplotlib import pyplot as plt
import  numpy as np
import pandas as pd
from tkinter import *
from tkinter.filedialog import asksaveasfile
import os

def pie_graph(graph_title,st_row,csv_file_path):
        data=pd.read_csv(csv_file_path)
        x_axis_data=data[st_row[0]]
        y_axis_data=data[st_row[1]]
        plt.pie(y_axis_data,labels=x_axis_data,shadow=True,wedgeprops={'edgecolor':'white','linewidth':3},autopct='%0.01f')
        plt.style.use('fivethirtyeight')
        plt.title(graph_title)
        plt.legend()
        plt.tight_layout()
        plt.grid()
        plt.show()


#pie_graph('Animals','Number','Bar Graph')
