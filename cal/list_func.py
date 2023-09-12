# 列出两个年份之间的所有闰年
from cal.cal_func import is_leap_year

the_list = []

def leap_year_list(year1, year2):
    year_range = range(int(year1), int(year2))
    for year in year_range:
        if is_leap_year(year):
            the_list.append(year)

    year_count = len(the_list)
    the_list_str = str(the_list).removeprefix('[')
    the_list_str = the_list_str.removesuffix(']')


    result = f'{year1} 到 {year2} 之间共有 {year_count} 个闰年，分别为: {the_list_str}'
    return result
