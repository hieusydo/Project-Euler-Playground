#Project Euler 19 -
#How many Sundays fell on the first of the month 1/1/1901 -> 31/12/2000

#def isLeap(year):
#    if year % 100 == 0:
#        return year % 400 == 0
#    return year % 4 == 0

#25 leap year in the 21 century
#General rule: shift day of the week one unit to the right
#Exception: shift 2 units on months after Feb on leap years

#1/1/1900 was a Monday -> 1901: Tues
#2/1 Thu
#3/1 Thu
#4/1 Sun
#5/1 Tue
#6/1 Fri
#7/1 Sun
#8/1 Wed
#9/1 Sat
#10/1 Mon
#11/1 Thu
#12/1 Sat

import calendar

baseYr = 1901
count = 0

#array keeping track: month (index 0->12 (one empty value)) :: day of week (code: Mon: 2,...Sun: 8)
#the day of week of 1900 
yr = [0, 2, 5, 5, 8, 3, 6, 8, 4, 7, 2, 5, 7]

while baseYr < 2001:
    if calendar.isleap(baseYr) == True:
        for i in range(3, 13):
            yr[i] += 1
            if yr[i] > 8:
                yr[i] -= 7
    for i in range(1, 13):
            yr[i] += 1
            if yr[i] > 8:
                yr[i] -= 7
    for month in yr:
        if month == 8:
            count += 1
            
    baseYr += 1
    
print("There are", count, "Sundays falling on the first of the month in the 21st century.")
    


