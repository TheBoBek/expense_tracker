import json
from datetime import datetime

class DataReader:
    def __init__(self):
        self.account_value = 0
        self.starting_value = 0
        self.month_balance = [0, 0, 0, 0, 0, 0]
        self.monthly_tran = [0, 0, 0, 0, 0, 0]

    def get_history(self):
        self.month_balance = [0, 0, 0, 0, 0, 0]
        self.monthly_tran = [0, 0, 0, 0, 0, 0]
        self.account_value = 0
        self.starting_value = 0


        now_month = datetime.now().month
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
                # Iterating through json data
                for thisdict_key in data:
                    is_halfyear = False
                    self.account_value += float(data[thisdict_key]["Value"])
                    thisdict_key_object = datetime.strptime(thisdict_key, '%Y-%m-%d %H:%M:%S.%f')
                    # Checking data date
                    for i in range(6):
                        if thisdict_key_object.month == (now_month - i + 11) % 12 + 1:
                            self.month_balance[i] += float(data[thisdict_key]["Value"])
                            is_halfyear = True
                            if thisdict_key_object.month == now_month:
                                # Checking transaction type
                                for j in range(1, 7):
                                    if data[thisdict_key]["Type"] == j:
                                        self.monthly_tran[j - 1] += data[thisdict_key]["Value"]
                    if not is_halfyear:
                        self.starting_value += float(data[thisdict_key]["Value"])
                        print(self.starting_value)
        except FileNotFoundError:
            pass
        finally:
            print(self.month_balance, "      ", self.monthly_tran)

    def get_graph_data(self):
        temp = self.starting_value
        month_value = []
        for i in self.month_balance[::-1]:
            temp = temp + i
            month_value.append(temp)
        return month_value

    def get_chart_data(self):
        return self.monthly_tran

