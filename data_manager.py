from tkinter import *
from datetime import date, datetime
from tkinter import messagebox
import json
BLACK = "#343a40"


class DataManager:
    def __init__(self):
        pass

    def save(self, input1, input2, var, var2):
        var_get = var.get()
        name_get = input1.get()
        value_get = input2.get()
        type_get = var2.get()
        now_str = str(datetime.now())
        try:
            value_get = float(value_get[:-1])
        except ValueError:
            messagebox.showwarning(title="Chyba", message="Zadajte správnu hodnotu.")
        else:
            if var_get == 2:
                value_get *= -1


            new_dict = {
                now_str: {
                    "Transaction": var_get,
                    "Name": name_get,
                    "Value": value_get,
                    "Type": type_get,
                }
            }

            try:
                with open("data.json", "r") as data_file:
                    # Reading old data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_dict, data_file, indent=4)
            else:
                # Updating old data with new data
                data.update(new_dict)

                with open("data.json", "w") as data_file:
                    # Saving updated data
                    json.dump(data, data_file, indent=4)
            finally:
                input1.delete(0, END)
                input2.delete(0, END)


