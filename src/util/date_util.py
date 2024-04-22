# date and time util functions

import datetime
import pytz



def now_str(fmt=None):
    """ current time in required format"""  

    if fmt is None:
        fmt="%Y%m%d%H%M%S"
    return datetime.datetime.now(tz=pytz.timezone("US/Eastern")).strftime(fmt)



def verify_date(date_str: str, fmt:str):
    """ verify the datetime format """

    try:
        datetime.datetime.strptime(date_str,fmt)
        return True
    except:
        return False
    


def format_datetime (date_str:str, fmt : str):
    """ convert the str format time to datetime format """

    return datetime.datetime.strptime(date_str,fmt)



def compare(dt1:datetime.datetime, dt2: datetime.datetime):
    """ compare two times if first > second return true, else flase"""
    return dt1>dt2
    
