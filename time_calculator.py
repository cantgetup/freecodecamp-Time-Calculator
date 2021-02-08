def add_time(start, duration, day_input=-1):
    
    weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    # extract variable
    start_hour, start_min = tuple(start.split()[0].split(':'))
    AM_or_PM = start.split()[1]
    dur_hour, dur_min = tuple(duration.split()[0].split(':'))
    #dayofweek = ?
    
    # convert int
    start_hour = int(start_hour)
    start_min = int(start_min)
    
    dur_hour = int(dur_hour)
    dur_min = int(dur_min)

    if AM_or_PM == 'PM':
        start_hour += 12
    
    # add minutes
    add_hour = 0
    
    final_min = (start_min + dur_min)%60
    
    if (start_min + dur_min)//60 >= 1:
        add_hour = 1
    
    if final_min < 10:
        final_min = '0' + str(final_min)
    else:
        final_min = str(final_min)
        
    # add hours    
    final_hour_raw = start_hour + dur_hour + add_hour
    
    final_hour_24 = final_hour_raw%24
    
    final_hour_12 = 0
    final_AM_PM = ''
    
    if final_hour_24 > 12:
        final_AM_PM = ' PM'
        final_hour_12 = final_hour_24 - 12
    elif final_hour_24 == 12:
        final_AM_PM = ' PM'
        final_hour_12 = 12      
    elif final_hour_24 == 0:
        final_AM_PM = ' AM'
        final_hour_12 = 12 
    else:
        final_AM_PM = ' AM'
        final_hour_12 = final_hour_24   
    
    final_hour_12 = str(final_hour_12)
    
    # how many days?
    day_string = ''
    
    num_days = final_hour_raw//24
    
    if num_days == 0:
        day_string = ''
    elif num_days == 1:
        day_string = ' (next day)'
    elif num_days > 1:
        day_string = f' ({num_days} days later)'
        
    # which day of week ends at?
    day_output = ''
    
    if type(day_input) == str:    
        day_input_num = weekdays.index(day_input.lower())
        day_output = ', '+ weekdays[(day_input_num + num_days)%7].capitalize()    

    return final_hour_12 + ':' + final_min + final_AM_PM + day_output + day_string
