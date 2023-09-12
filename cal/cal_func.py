# 公历：能被4整除、但不能被100整除，或能被400整除的年份为闰年；其余为平年。

def is_leap_year(year):
    """判断是否为闰年"""
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0