import datetime


def first_friday(date):
    while True:
        if date.weekday() == 4:
            return date
        date += datetime.timedelta(days=1)


def friday_counter(year):
    year_start = datetime.datetime(year, 1, 1)
    year_end = datetime.datetime(year, 12, 31)
    friday = first_friday(year_start)
    counter = 0
    while friday <= year_end:
        counter += 1
        friday += datetime.timedelta(days=7)
    return(counter)


def friday_years(start, end):
    return sum([1 for x in range(start, end + 1) if friday_counter(x) == 53])


def main():
    print(friday_years(1000, 2000))
    print(friday_years(1753, 2000))
    print(friday_years(1990, 2015))

if __name__ == '__main__':
    main()
