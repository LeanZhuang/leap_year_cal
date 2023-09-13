# 公历：能被4整除、但不能被100整除，或能被400整除的年份为闰年；其余为平年。

import tkinter as tk
from tkinter import ttk, font

import cal.cal_func as cf
import cal.list_func as lf


def set_result(result_text:tk.Text, text:str, res_error=False):
    '''配置输出结果'''
    result_text.config(state='normal')
    result_text.delete('1.0', 'end')
    result_text.insert('end', text)
    result_text.configure(state='disabled')
    if res_error == True:
        result_text.tag_add("color_tag", "1.0", "end")
        result_text.tag_configure("color_tag", font=error_font, foreground="red", background="yellow")


def calculate_is_leap():
    try:
        year = int(year_entry_1.get())
        if cf.is_leap_year(year):
            text=f'{year}年是闰年'
            set_result(result_text, text)
        else:
            text=f'{year}年是平年'
            set_result(result_text, text)
    except ValueError:
        text='输入错误，请检查输入是否为年份'
        set_result(result_text, text, True)


def calculate_leap_list():
    try:
        year1 = int(year_entry_2_1.get())
        year2 = int(year_entry_2_2.get())
        text = lf.leap_year_list(year1, year2)
        set_result(result_text, text)
    except ValueError:
        text='输入错误，请检查输入是否为年份'
        set_result(result_text, text, True)


# 窗口配置
window = tk.Tk()

window.title('闰年计算器')
window.geometry('600x400')

# 字体配置
normal_font = font.Font(family='Arial', size=14)
bold_font = font.Font(family='Arial', size=12, weight='bold')
error_font = font.Font(family='Arial', size=15, weight='bold')
mark_font = font.Font(family='Arial', size=10)


# 框架 1
frame1 = ttk.Frame(window)
frame1.pack(side='top', expand=True)

label1 = ttk.Label(frame1, text='请输入年份：', font=normal_font)
label1.pack(side='left', expand=True, pady=25)

year_entry_1 = ttk.Entry(frame1, width=10, font=normal_font)
year_entry_1.pack(side='left', expand=True, pady=25)

button1 = ttk.Button(frame1, text='计算', command=calculate_is_leap)
button1.pack(side='left', expand=True, padx=25, pady=25)


# 框架 2
frame2 = ttk.Frame(window)
frame2.pack()

label2 = ttk.Label(frame2, text='请输入年份区间：', font=normal_font)
label2.pack(side='left')

year_entry_2_1 = ttk.Entry(frame2, width=10, font=normal_font)
year_entry_2_1.pack(side='left')

label2 = ttk.Label(frame2, font=normal_font)
label2.configure(text=' ~ ')
label2.pack(side='left')

year_entry_2_2 = ttk.Entry(frame2, width=10, font=normal_font)
year_entry_2_2.pack(side='left')

button2 = ttk.Button(frame2, text='计算', command=calculate_leap_list)
button2.pack(side='left', padx=25)


# 框架 3
frame3 = ttk.Frame(window)
frame3.pack(fill='x', padx=20, pady=20)

label3 = ttk.Label(frame3, text='- 结果窗口 -', font=bold_font, anchor='w')
label3.pack(anchor='w', pady=5)

result_text = tk.Text(frame3, font=normal_font)
result_text.configure(font=normal_font)
result_text.pack(anchor='w', fill='x')
result_text.pack_propagate(False)


label_marked = ttk.Label(window, text='by Lean Zhuang 2023.09', font=mark_font)
label_marked.pack(pady=2, expand=True)


window.mainloop()
