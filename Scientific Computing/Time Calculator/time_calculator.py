def add_time(start, duration, start_day=None):

  #Get start time, the start value = 11:06 PM
  start_time, period = start.split()
  #Example: start time 11:06
  #Example: period PM
  start_hour, start_minute = map(int, start_time.split(':'))
  #Example start_hour = 11
  #Example start_minute = 6

  #Get duration time, the duration value = 2:02
  duration_hour, duration_minute = map(int, duration.split(':'))
  #Example: duration_hour = 2
  #Example: duration_minute = 2

  #Calculate total minutes
  total_minutes = start_hour * 60 + start_minute + duration_hour * 60 + duration_minute
  #Example: total_minutes = (11 * 60) + 6 + (2 * 60) + 2 = 788

  #Calculate days and remaining minutes
  days = total_minutes // (24 * 60)
  remaining_minutes = total_minutes % (24 * 60)
  #Example: days = 788 // (24 * 60) = 0
  #Example: remaining_minutes = 788 % (24 * 60) = 788

  #Calculate new hours and minutes
  new_hour = remaining_minutes // 60
  new_minute = remaining_minutes % 60
  #Example: new_hour = 788 // 60 = 13
  #Example: new_minute = 788 % 60 = 8

  #Determine period (AM/PM)
  if new_hour >= 12:
    period = "PM" if period == "AM" else "AM"
    days += 1 if period == "AM" else 0
    new_hour = new_hour - 12 if new_hour > 12 else new_hour

  # Update day if start_day is provided
  if start_day:
    start_day = start_day.lower().capitalize()
    days_of_week = [
        "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",
        "Sunday"
    ]
    start_day_index = days_of_week.index(start_day)
    new_day_index = (start_day_index + days) % 7
    new_day = days_of_week[new_day_index]
    if days == 0:
      new_time = f"{new_hour}:{new_minute:02d} {period}, {new_day}"
    elif days == 1:
      new_time = f"{new_hour}:{new_minute:02d} {period}, {new_day} (next day)"
    else:
      new_time = f"{new_hour}:{new_minute:02d} {period}, {new_day} ({days} days later)"

  else:
    if days == 0:
      new_time = f"{new_hour}:{new_minute:02d} {period}"
    elif days == 1:
      new_time = f"{new_hour}:{new_minute:02d} {period} (next day)"
    else:
      new_time = f"{new_hour}:{new_minute:02d} {period} ({days} days later)"

  return new_time
