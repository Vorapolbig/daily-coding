"""
Given a date, return the corresponding day of the week for that date.

The input is given as three integers representing the day, month and year respectively.

Return the answer as one of the following values {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.
"""

import datetime

def solution(day, month, year):
    days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday","Sunday")
    
    return days[datetime.date(year,month,day).weekday()]

print(solution(26,3,2020))