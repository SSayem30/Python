def leap_year(year):
    if year%4==0:
        if year %100==0:
            if year %400==0:
                return True
            else:
                return False
        return True
    else:
        return False
def days_in_month(year,month):
    month_list=[31,28,31,30,31,30,31,31,30,31,30,31]
    if leap_year(year) and month==2:
        return 29
    else:
        return month_list[month-1]

year=int(input("Enter the year: "))
month=int(input("Enter the month: "))
print(f"The day of this month is: {days_in_month(year,month)}")
