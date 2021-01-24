import datetime
# print(dir(datetime))

# note date


# note datetime
now = datetime.datetime.now()
# print(now, now.day, now.year, now.month)
# print(now.hour, now.minute, now.second)
# print(now.timestamp())
# print(f'{day}/{month}/{year}, {hour}:{minute}')

# from datetime import datetime
# # current date and time
# now = datetime.now()
# t = now.strftime("%H:%M:%S")
# print("time:", t)
# time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
# # mm/dd/YY H:M:S format
# print("time one:", time_one)
# time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
# # dd/mm/YY H:M:S format
# print("time two:", time_two)

# from datetime import datetime
# date_string = "5 December, 2019"
# print("date_string =", date_string)
# date_object = datetime.strptime(date_string, "%d %B, %Y")
# print("date_object =", date_object)

# from datetime import date
# d = date(2020, 1, 1)
# print(d)
# print('Current date:', d.today())    # 2019-12-05
# # date object of today's date
# today = date.today()
# print("Current year:", today.year)   # 2019
# print("Current month:", today.month) # 12
# print("Current day:", today.day)     # 5

# note time
# from datetime import time
# # time(hour = 0, minute = 0, second = 0)
# a = time()
# print("a =", a)
# # time(hour, minute and second)
# b = time(10, 30, 50)
# print("b =", b)
# # time(hour, minute and second)
# c = time(hour=10, minute=30, second=50)
# print("c =", c)
# # time(hour, minute, second, microsecond)
# d = time(10, 30, 50, 200555)
# print("d =", d)

# note timedelta

# from datetime import timedelta
# t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
# t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
# t3 = t1 - t2
# print("t3 =", t3)