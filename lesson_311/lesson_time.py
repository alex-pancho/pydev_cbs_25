import time

current_time = time.localtime()
print(current_time)
print("Рік:", current_time.tm_year)
print("Місяць:", current_time.tm_mon)
print(tuple(current_time))

moment_of_start_this_lesson = (2025, 12, 9, 19, 0, 1, 1, 343, 0)
print(time.asctime(moment_of_start_this_lesson))
unixtime = 1765300003.1234
print(time.ctime(unixtime))
print(time.ctime(0))
print(time.localtime(unixtime))

some_day = "Sep 20, 2022"
now_day = "2025, December, 09, 19:00:01"
print(time.strftime("%Y, %B, %d, %H:%M:%S", moment_of_start_this_lesson))

print(time.strptime(now_day, "%Y, %B, %d, %H:%M:%S"))

print(time.strptime(some_day, "%b %d, %Y"))

now = time.time()
print(now)
time.sleep(0.5)
now = time.time()
print(now)
