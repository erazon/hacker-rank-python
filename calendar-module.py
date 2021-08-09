import calendar

if __name__ == '__main__':
    month, day, year = map(int, input().split())
    week = calendar.weekday(year, month, day)
    print(list(calendar.day_name)[week].upper())
