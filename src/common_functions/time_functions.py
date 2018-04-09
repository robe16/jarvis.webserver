import datetime


def timestamp_now():
    #
    timestamp = datetime.datetime.now()
    timestamp = utc_to_local(timestamp)
    #
    return timestamp.strftime('%d/%m/%Y %H:%M:%S')


def utc_to_local(utc_dt):
    return utc_dt.replace(tzinfo=datetime.timezone.utc).astimezone(tz=None)