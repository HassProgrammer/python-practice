import datetime

date = datetime.date(2024, 10, 10)
print(f"using date: {date}")

print("........................")

today = datetime.date.today()
print(f"Today's date: {today}")

print("........................")

time = datetime.time(12, 57, 59)
print(f"using time: {time}")

print("........................")

current_time = datetime.datetime.now()
print(f"Current time: {current_time}")

print("........................")

formatting_current_time = datetime.datetime.now().strftime("%H:%M:%S %m-%d-%Y")
print(formatting_current_time)
