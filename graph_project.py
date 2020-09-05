import csv
import  line_graph
import  bar_graph
import  pie_graph
from tkinter.filedialog import askopenfile
import tkinter

from tkinter import filedialog

import pandas as pd
from tkinter import *
#csv_file_name='line_graph.csv'
st_row=[]
csv_file_path='aro'



def heading_extraction_from_csv(csv_file_path):
    data=pd.read_csv(csv_file_path,nrows=0)
    for i in data:
        st_row.append(i)


#heading_extraction_from_csv()







def pie_function(root):
    root.destroy()
    win = Tk()
    win.geometry('800x650')
    win.config(bg='black')
    Label(win, text='Enter Pie Graph Name', font=('Verdana', 13), fg='black', bg='SeaGreen1',padx=10,pady=10,relief=RAISED).place(x=50,y=100)
    graph_name_entry=Entry(win, font=('Verdana', 13), fg='black', bg='WHITE', relief=RAISED)
    graph_name_entry.place(x=300, y=110)

    Button(win, text='Show Graph', height=1, width=10, padx=10, pady=10, bg='coral1', fg='black',
           command=lambda : pie_graph.pie_graph(graph_name_entry.get(),st_row,csv_file_path)).place(x=350, y=250)


    win.mainloop()

def bar_function(root):
    root.destroy()
    win = Tk()
    win.geometry('800x650')
    win.config(bg='black')
    Label(win, text='Enter Pie Graph Name', font=('Verdana', 13), fg='black', bg='SeaGreen1',padx=10,pady=10,relief=RAISED).place(x=50,y=100)
    graph_name_entry=Entry(win, font=('Verdana', 13), fg='black', bg='WHITE', relief=RAISED)
    graph_name_entry.place(x=300, y=110)

    Label(win, text='Enter X Axis Name', font=('Verdana', 13), fg='black', bg='SeaGreen1', padx=10, pady=10,
          relief=RAISED).place(x=50, y=250)
    graph_x_axis_name_entry = Entry(win, font=('Verdana', 13), fg='black', bg='WHITE', relief=RAISED)
    graph_x_axis_name_entry.place(x=300, y=260)

    Label(win, text='Enter Y Axis Name', font=('Verdana', 13), fg='black', bg='SeaGreen1', padx=10, pady=10,
          relief=RAISED).place(x=50, y=400)
    graph_y_axis_name_entry = Entry(win, font=('Verdana', 13), fg='black', bg='WHITE', relief=RAISED)
    graph_y_axis_name_entry.place(x=300, y=410)


    Button(win, text='Show Graph', height=1, width=10, padx=10, pady=10, bg='coral1', fg='black',
           command=lambda : bar_graph.bar_graph(graph_x_axis_name_entry.get(),graph_y_axis_name_entry.get(),graph_name_entry.get(),st_row,csv_file_path)).place(x=350, y=500)


    win.mainloop()

def line_function(root):
    root.destroy()
    win = Tk()
    win.geometry('800x650')
    win.config(bg='black')
    Label(win, text='Enter Line Graph Name', font=('Verdana', 13), fg='black', bg='SeaGreen1',padx=10,pady=10,relief=RAISED).place(x=50,y=100)
    graph_name_entry=Entry(win, font=('Verdana', 13), fg='black', bg='WHITE', relief=RAISED)
    graph_name_entry.place(x=300, y=110)

    Label(win, text='Enter X Axis Name', font=('Verdana', 13), fg='black', bg='SeaGreen1', padx=10, pady=10,
          relief=RAISED).place(x=50, y=250)
    graph_x_axis_name_entry = Entry(win, font=('Verdana', 13), fg='black', bg='WHITE', relief=RAISED)
    graph_x_axis_name_entry.place(x=300, y=260)

    Label(win, text='Enter Y Axis Name', font=('Verdana', 13), fg='black', bg='SeaGreen1', padx=10, pady=10,
          relief=RAISED).place(x=50, y=400)
    graph_y_axis_name_entry = Entry(win, font=('Verdana', 13), fg='black', bg='WHITE', relief=RAISED)
    graph_y_axis_name_entry.place(x=300, y=410)


    Button(win, text='Show Graph', height=1, width=10, padx=10, pady=10, bg='coral1', fg='black',
           command=lambda : line_graph.line_graph(graph_x_axis_name_entry.get(),graph_y_axis_name_entry.get(),graph_name_entry.get(),st_row,csv_file_path)).place(x=350, y=500)

    win.mainloop()







def upload_data_function():
    global csv_file_path
    tkinter.Tk().withdraw()
    in_path = filedialog.askopenfile()
    csv_file_path= in_path.name
    heading_extraction_from_csv(csv_file_path)



def main_menu():

    root = Tk()
    root.geometry('800x650')
    root.config(bg='black')
    Label(root, text='Graph', font=('Verdana', 30), fg='white', bg='black').pack(side=TOP, pady=10)
    logo = PhotoImage(file='images/logo.gif')
    bar = PhotoImage(file='images/bar.gif')
    pie = PhotoImage(file='images/pie.gif')
    line = PhotoImage(file='images/line.gif')
    # Button(root,text='i need this plz',image=logo).pack(side=TOP)
    Label(root, text='Snake n Ladder', font=('Andalus', 20, 'bold'), bg='black', fg='light blue', pady=50,
                    image=logo).pack(side=TOP)

    # Label(text=' '*30,fg='black',bg='black').pack(side=LEFT)
    Button(root, text='i need this plz', image=pie, command=lambda: pie_function(root)).place(x=70, y=400)
    # Label(text=' '*30,fg='black',bg='black').pack(side=LEFT)
    Button(root, text='i need this plz', image=bar,command=lambda : bar_function(root)).place(x=330, y=400)
    # Label(text=' '*30,fg='black',bg='black').pack(side=LEFT)
    Button(root, text='i need this plz', image=line,command=lambda :line_function(root)).place(x=590, y=400)
    # Label(text=' '*30,fg='black',bg='BLACK').pack(side=LEFT)

    Button(root, text='Upload Data ', font=('verdana', 15),command=lambda :upload_data_function()).place(x=320, y=300)

    root.mainloop()



if __name__=='__main__':

    st_row=[]
    csv_file_path='aro'


    main_menu()




















