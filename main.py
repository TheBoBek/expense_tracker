from tkinter import *
from mainwindow import MainWindow, DataManagerWindow
from datetime import date, datetime
from tkinter import messagebox
from data_manager import DataManager
from data_reader import DataReader
import json


today_str = date.today().strftime('%Y-%m-%d')
data_read = DataReader()
timer = ""

# -------------- Data Management -------------------#


def pridaj():
    global value
    global timer
    data_manager_window = DataManagerWindow(gui)
    data_manager = DataManager()
    data_manager_window.pridaj_button.config(command=lambda: [data_manager.save(data_manager_window.input1,
                                                                                data_manager_window.input2,
                                                                                data_manager_window.var,
                                                                                data_manager_window.var2),
                                                              data_manager_window.pridaj_win.destroy(),
                                                              data_read.get_history(),
                                                              gui.update_graph(data_read.get_graph_data()),
                                                              gui.update_chart(data_read.get_chart_data()),
                                                              gui.value_label.config(text=f"{value_count()}€")])


def value_count():
    try:
        data_read.update_value()
        value = data_read.account_value
    except FileNotFoundError:
        value = 0
    return int(value)

def month_count():
    try:
        month_balance = data_read.get_graph_data()
        spending_report = data_read.get_chart_data()
    except FileNotFoundError:
        month_balance = [0, 0, 0, 0, 0, 0]
        spending_report = [1, 1, 1, 1, 1, 1]
    return month_balance, spending_report

data_read.get_history()
value = value_count()
month_balance, spending_report = month_count()

print(value, month_balance)






# -------------- GUI -------------------#


#if __name__ == "__main__":
#    gui = Gui()
#    v = Scrollbar(gui)
#    v.pack()
#    gui.mainloop()

gui = MainWindow(month_balance, spending_report)
gui.pridaj_button.config(command=pridaj)
gui.value_label.config(text=f"{value}€")

# VYKRESLOVANIE GRAFU

gui.mainloop()


