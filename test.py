import random
import datetime
import json



month_value = 0
month = 10
month2 = 11
year = 2022
year2 = 2022
for j in range(7):
    month_value += month_value
    if month + j > 12:
        month -= 12
        year += 1
    if month2 + j > 12:
        month2 -= 12
        year2 += 1
    start_date = datetime.date(year, month, 1)
    end_date = datetime.date(2023, 5, 1)
    delta = end_date - start_date
    random_date = start_date + datetime.timedelta(days=random.randint(0, delta.days))

    random_datetime = datetime.datetime.combine(random_date, datetime.time.min)

    print(random_datetime)

    for i in range(15):
        random_date = start_date + datetime.timedelta(days=random.randint(0, delta.days))
        random_datetime = str(datetime.datetime.combine(random_date, datetime.time.min) + datetime.timedelta(
            seconds=random.randint(0, 86400), microseconds=random.randint(0, 1000000)))
        random_money = random.randint(0, 1000)
        random_transaction = random.randint(1, 2)
        random_type = random.randint(1, 6)
        if random_transaction == 2:
            random_money *= -0.5
        if random_money + month_value >= 0:
            month_value += random_money

            new_dict = {
                random_datetime: {
                    "Transaction": random_transaction,
                    "Name": "Nepovinne",
                    "Value": random_money,
                    "Type": random_type,
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
        else:
            pass

