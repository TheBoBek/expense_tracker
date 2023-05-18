from tkinter import *
from mainwindow import MainWindow, DataManagerWindow
from datetime import date, datetime
from tkinter import messagebox
from data_manager import DataManager
from data_reader import DataReader
import json

today_str = date.today().strftime('%Y-%m-%d')
data_read = DataReader()


# -------------- Data Management -------------------#


def pridaj():
    global value
    data_manager_window = DataManagerWindow(gui)  # Creates second window for data management
    data_manager = DataManager()
    data_manager_window.pridaj_button.config(command=lambda: [data_manager.save(data_manager_window.input1,  # Saving data from mainwindow
                                                                                data_manager_window.input2,
                                                                                data_manager_window.var,
                                                                                data_manager_window.var2,
                                                                                data_read.account_value),
                                                              data_manager_window.pridaj_win.destroy(),  # Destroys second window
                                                              data_read.get_history(),  # Updates attributes in data_reader
                                                              gui.update_graph(data_read.get_graph_data()), # Updates graph with new data
                                                              gui.update_chart(data_read.get_chart_data()), # Updates chart with new data
                                                              gui.value_label.config(
                                                                  text=f"{data_read.account_value}€")])  # Updates value label in mainwindow


def month_count():
    try:
        value = data_read.account_value
        month_balance = data_read.get_graph_data()
        spending_report = data_read.get_chart_data()
    except FileNotFoundError:  # Initializes default values
        value = 0
        month_balance = [0, 0, 0, 0, 0, 0]
        spending_report = [1, 1, 1, 1, 1, 1]
    return month_balance, spending_report, value


data_read.get_history()
month_balance, spending_report, value = month_count()

# Initializing gui
gui = MainWindow(month_balance, spending_report)
gui.pridaj_button.config(command=pridaj)
gui.value_label.config(text=f"{value}€")

gui.mainloop()
