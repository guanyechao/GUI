#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import tkinter as tk
root = tk.Tk()
root.title('GUI测试')
root.geometry('500x250')


on_hit = False
def hit_me():
    global on_hit
    if on_hit == False: #   从False状态变成True状态
        on_hit = True
        var.set('What Are You Doing ! You Hit Me ?')    #   设置标签的文字
    else:
        on_hit = False
        var.set('') #   设置文字为空

        

label = tk.Label(root,text = 'OMG！这是GUI：',
                 font=("微软雅黑",16),
                 bg='red',width=30,height=2)
#label.pack()


var = tk.StringVar()    #   这是文字变量储存器
label = tk.Label(root,textvariable=var, #   使用textvariable替换text,因为这个可以变化
                 font=("微软雅黑",16),
                 bg='red',width=30,height=2)
label.pack()


button = tk.Button(root,text='你点我试试',   #   显示按钮上的文字
                   width = 15,height=2,
                   command=hit_me)  # 点击按钮执行命令
button.pack()   #   按钮位置


# 进入消息循环
root.mainloop()
