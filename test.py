import random
import datetime
import json

start_date = datetime.date(2022, 10, 1)
end_date = datetime.date(2023, 4, 7)

delta = end_date - start_date
random_date = start_date + datetime.timedelta(days=random.randint(0, delta.days))

random_datetime = datetime.datetime.combine(random_date, datetime.time.min)

print(random_datetime)

for i in range(50):
    random_date = start_date + datetime.timedelta(days=random.randint(0, delta.days))
    random_datetime = str(datetime.datetime.combine(random_date, datetime.time.min) + datetime.timedelta(
        seconds=random.randint(0, 86400), microseconds=random.randint(0, 1000000)))
    random_money = random.randint(0, 1000)
    random_transaction = random.randint(1, 2)
    random_type = random.randint(1, 6)
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

