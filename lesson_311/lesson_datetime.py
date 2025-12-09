from datetime import datetime, timedelta, timezone

day_now = datetime.today()
print(day_now)
day_now_utc = datetime.now(timezone.utc)
print(day_now_utc)

day_number = datetime.today().toordinal()
print(f'Порядковий номер сьогоднішнього дня: {day_number}')
unixtime = float("1765300003.123")
dt = datetime.fromtimestamp(unixtime)
print(dt)

pattern = "%Y, %B, %d, %H:%M:%S"
now_day = "2025, December, 09, 19:00:01"

dt2 = datetime.strptime(now_day, pattern)
print(dt2)

dt3 = datetime.strftime(day_now_utc, pattern)
print(dt3)
print(day_now_utc.isoformat())
print(day_now_utc.ctime())

point_1 = "11:22:10"
point_2 = "12:23:10"

pattern_for_point = "%H:%M:%S"

point_1_dt = datetime.strptime(point_1, pattern_for_point)
point_2_dt = datetime.strptime(point_2, pattern_for_point)

print(point_1_dt, point_2_dt)

print(type(point_2_dt - point_1_dt))

td1 = timedelta(hours=1)
print(point_2_dt - td1 - point_1_dt)
td1 = timedelta(hours=1)

if point_2_dt - td1 - point_1_dt < timedelta(minutes=3):
    print("pass")

# print(point_1_dt - point_2_dt)
print((point_2_dt - td1 - point_1_dt).total_seconds())

ystday = day_now_utc - timedelta(days=1)
print(ystday)
