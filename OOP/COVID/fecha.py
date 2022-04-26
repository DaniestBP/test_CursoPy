import datetime as dt

today = dt.datetime.now()
# today = today.isoformat()  # .isoformat() convierte el formato fecha a formato string

# dt_today = dt.datetime.fromisoformat(today)
# print(type(dt_today))
idate = "2021/12/10"
idate = idate.replace("/", "-")
dt_idate = dt.datetime.fromisoformat(idate)

days_in_between = today - dt_idate
print(type(days_in_between))