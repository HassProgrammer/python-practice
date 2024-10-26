import datetime

target_date_time = datetime.datetime(2050, 1, 2, 12, 31, 1)
current_date_time = datetime.datetime.now()

if current_date_time > target_date_time:
    print("Target date has pass")
else:
    print("Target date has not pass")
