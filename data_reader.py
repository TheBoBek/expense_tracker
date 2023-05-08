import json
from datetime import datetime

class DataReader:
    def __init__(self):
        self.account_value = 0
        self.month_balance = [0, 0, 0, 0, 0, 0]
        self.monthly_tran = [0, 0, 0, 0, 0, 0]

    def update_value(self):
        try:
            self.account_value = 0
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
                for thisdict_key in data:
                    self.account_value += float(data[thisdict_key]["Value"])
        finally:
            pass

    def get_history(self):
        self.month_balance = [0, 0, 0, 0, 0, 0]
        self.monthly_tran = [0, 0, 0, 0, 0, 0]
        now_month = datetime.now().month
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
                for thisdict_key in data:
                    thisdict_key_object = datetime.strptime(thisdict_key, '%Y-%m-%d %H:%M:%S.%f')
                    for i in range(6):
                        if thisdict_key_object.month == (now_month - i + 11) % 12 + 1:
                            if thisdict_key_object.month == now_month:
                                for j in range(1, 7):
                                    if data[thisdict_key]["Type"] == j:
                                        self.monthly_tran[j - 1] += data[thisdict_key]["Value"]
                            self.month_balance[i] += (data[thisdict_key]["Value"])
        finally:
            print(self.month_balance, "      ", self.monthly_tran)

    def get_graph_data(self):
        return self.month_balance

    def get_chart_data(self):
        return self.monthly_tran

