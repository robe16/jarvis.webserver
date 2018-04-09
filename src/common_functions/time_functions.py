import datetime


def timestamp_now():
    #
    timestamp = datetime.datetime.now()
    #
    return datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')


# British Summer Time (BST)

# BST starts: forward 1 hour at 1am on the last Sunday in March
# BST ends: back 1 hour at 2am on the last Sunday in October

def check_is_bst():
    today = datetime.datetime.now()
    current_year = today.year
    #
    return _start_bst(current_year) <= today <= _end_bst(current_year)


def _start_bst(year):
    # Last Sunday in March
    last_sunday = _get_last_sunday(year, 3)
    # 1am
    return datetime.datetime(last_sunday.year, last_sunday.month, last_sunday.day, 1)


def _end_bst(year):
    # Last Sunday in October
    last_sunday = _get_last_sunday(year, 10)
    # 2am
    return datetime.datetime(last_sunday.year, last_sunday.month, last_sunday.day, 2)


def _get_last_sunday(year, month):
    #
    num_of_days = (datetime.date(year, month + 1, 1) - datetime.date(year, month, 1)).days
    #
    d = datetime.date(year, month, num_of_days)
    #
    while not d.weekday() == 6:  # Sunday = 6
        d = d - datetime.timedelta(days=1)
    #
    return d