from datetime import datetime, date

data = list(map(int, input().split()))

def what_day(date):
  days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
  day = date.weekday()
  print(days[day])

what_day(date(2007, data[0], data[1]))