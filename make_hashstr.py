import tkinter as tk
import hashlib

def exec_ooo(str_origin_var, str_processed_var):
    origin_str = str_origin_var.get()
    processed_str = hashlib.md5(origin_str.encode()).hexdigest()

    str_processed_var.set(processed_str)


# 共通のpaddingサイズ設定
padSize = dict(padx=5, pady=5)
padSize_fillx = padSize.copy()
padSize_fillx.update(expand='1', fill=tk.X)

root = tk.Tk()
root.geometry('300x300')
str_origin_var = tk.StringVar()
str_processed_var = tk.StringVar()

upper_frame = tk.Frame(root)
right_frame = tk.Frame(upper_frame)
left_frame = tk.Frame(upper_frame)
bottom_frame = tk.Frame(root)

origin_label = tk.Label(left_frame, text='元の文字列')
processed_label = tk.Label(left_frame, text='ハッシュ化後の文字列')
origin_label.pack()
processed_label.pack()
left_frame.pack(side=tk.LEFT)
right_frame.pack(side=tk.LEFT, **padSize_fillx)
upper_frame.pack(anchor=tk.NW, **padSize_fillx)

original_str_entry = tk.Entry(right_frame, textvariable=str_origin_var)
processed_str_entry = tk.Entry(right_frame, textvariable=str_processed_var)
exec_button = tk.Button(root, text='お”お”お”お”お”！！！',command=lambda:exec_ooo(str_origin_var, str_processed_var))

original_str_entry.pack(**padSize_fillx)
processed_str_entry.pack(**padSize_fillx)
exec_button.pack(anchor=tk.N)
bottom_frame.pack(anchor=tk.NW, **padSize_fillx)

root.mainloop()
