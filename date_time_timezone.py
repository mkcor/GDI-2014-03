# Module containing functions to get date/time in other timezones

import datetime
from pytz import timezone


def get_date(hoursago, othertz):
    """
    Returns the date and time it was 'hoursago' in 'othertz'
    """
    # This is our timezone
    eastern = timezone('US/Eastern')
    # This is the other timezone
    othertz = timezone(othertz)
    # This is the time right now in our timezone
    now_here = datetime.datetime.now(eastern)
    # Subtract given number of hours
    then_here = now_here - datetime.timedelta(0, 0, 0, 0, 0, hoursago)
    then_there = then_here.astimezone(othertz)
    datetime_there = then_there.strftime('%m-%d-%Y %H:%M:%S')
    return(datetime_there)

# Now write a function which returns the date it will be in Vancouver x hours
# into the future (date should be displayed in Canadian notation)
