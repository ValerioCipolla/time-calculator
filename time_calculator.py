def add_time(start, duration, day = None):

    hours_dict = {
        "12AM": 0,
        "1AM": 1,
        "2AM": 2,
        "3AM": 3,
        "4AM": 4,
        "5AM": 5,
        "6AM": 6,
        "7AM": 7,
        "8AM": 8,
        "9AM": 9,
        "10AM": 10,
        "11AM": 11,
        "12PM": 12,
        "1PM": 13,
        "2PM": 14,
        "3PM": 15,
        "4PM": 16,
        "5PM": 17,
        "6PM": 18,
        "7PM": 19,
        "8PM": 20,
        "9PM": 21,
        "10PM": 22,
        "11PM": 23,
    }

    days_dict = {
        "monday": 1,
        "tuesday": 2,
        "wednesday": 3,
        "thursday": 4,
        "friday": 5,
        "saturday": 6,
        "sunday": 7
    }

    reverse_days_dict = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }

    # figure out what hour of the day is 
    start_hours = start.split(":")[0] + start.split(" ")[1]
    start_hours = hours_dict[start_hours]
    start_minutes = int(start.split(":")[1].split(" ")[0])

    # get values to add
    duration_hours = int(duration.split(":")[0])
    duration_minutes = int(duration.split(":")[1])

    # figure out hours and minutes after adding values
    final_hours = int(start_hours + duration_hours)
    final_minutes = int(start_minutes + duration_minutes)
    final_days = 0

    # if minutes are > 60, get right minutes and add to hours
    while final_minutes > 59:
        final_hours = final_hours + 1
        final_minutes = final_minutes - 60
    
    #if hours are > 23, get right hours and add to days
    while final_hours > 23:
        final_days = final_days + 1
        final_hours = final_hours - 24
    
    # get correct hour of the day for the result hour
    result = ""
    if final_hours == 0 or final_hours == 12:
        result = result + "12:"
    elif final_hours < 12:
        result = result + str(final_hours) + ":"
    elif final_hours > 12:
        result = result + str(final_hours - 12) + ":"

    # check if final_minutes needs zero in front or not and add to result
    if len(str(final_minutes)) == 2:
        result = result + str(final_minutes)
    else:
        result = result + "0" + str(final_minutes)
    
    # check if it's AM or PM and add to result
    if final_hours >= 12:
        result = result + " PM"
    else: 
        result = result + " AM"

    # check if day of the week is needed and add to result
    if day is not None:
        day_value = days_dict[day.lower()]
        final_week_day = day_value + final_days
        if final_week_day <= 7:
            result = result + ", " + reverse_days_dict[final_week_day]
        else:
            while final_week_day > 7:
                final_week_day = final_week_day - 7
            result = result + ", " + reverse_days_dict[final_week_day]
    
    #check days and add to result
    if final_days == 1:
        result = result + " (next day)"
    elif final_days > 1:
        result = result + f" ({final_days} days later)"
    
    return result

    