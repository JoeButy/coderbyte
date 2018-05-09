import calendar
from datetime import datetime
from datetime import timedelta

# print calendar.isleap(1900)
def recurringTask(firstDate, k, daysOfTheWeek, n):
	dt = datetime.strptime(firstDate, '%d/%m/%Y')
	weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
	week = dt.isocalendar()[1]
	wk_idx = dt.weekday()
	day = weekdays[wk_idx]
	weekdays = weekdays[wk_idx:] + weekdays[:wk_idx]
	splits = []
	for day in daysOfTheWeek:
		indx = weekdays.index(str(day))
		splits.append(indx)
	splits.sort()
	print splits
	dates = []
	for i in range(0,n):
		for s in splits:
			event_date = dt + timedelta(days=s+(7*i*k))
			dates.append(event_date.date().strftime('%d/%m/%Y'))
	return dates[:n]

firstDate = "01/01/2015"
k = 2
daysOfTheWeek = ["Monday", "Thursday"]
n = 4
recurringTask(firstDate, k, daysOfTheWeek, n)