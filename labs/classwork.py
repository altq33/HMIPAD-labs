import time


def parse_date(time):
	total_seconds = int(time)
	micro_seconds = int((time - total_seconds) * 1000000)
	minutes, seconds = divmod(total_seconds, 60)
	hours, minutes = divmod(minutes, 60)
	days, hours = divmod(hours, 24)
	year = 1970
	month = 1
	day = 1
	while True:
		days_in_year = 365
		if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
			days_in_year = 366
		if days >= days_in_year:
			year += 1
			days -= days_in_year
		else:
			break
	while True:
		days_in_month = 31
		if month in [4, 6, 9, 11]:
			days_in_month = 30
		elif month == 2:
			days_in_month = 29 if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else 28
		if days >= days_in_month:
			month += 1
			days -= days_in_month
		else:
			break
	day += days
	# Return the parsed date and time as a tuple
	return year, month, day, hours, minutes, seconds, micro_seconds


if __name__ == "__main__":
	current_time = time.time()
	print(current_time)
	parsed_time = parse_date(current_time)
	print("-".join(map(str, list(parsed_time[:3]))), ":".join(map(str, list(parsed_time[3:]))), "UTC", sep=" ")
	data = [34832, 43432, 32049, 438473, 43848374, 4378493274, 4378432, 43242, 43243]
	print(f'min {min(data)}')  # O(n)
