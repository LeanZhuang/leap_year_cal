import tkinter as tk
import tkinter.font as tkfont

root = tk.Tk()

# 创建一个Text控件
text = tk.Text(root)
text.pack()

# 在Text中插入文字，并为其设置标记（tag）
text.insert("1.0", "Hello, world!")
text.tag_add("color_tag", "1.0", "end")

# 创建一个自定义的字体
font = tkfont.Font(family="Arial", size=12, weight=tkfont.BOLD, slant=tkfont.ITALIC)

# 配置标记的样式，设置字体颜色为红色
text.tag_configure("color_tag", font=font, foreground="red")

root.mainloop()
