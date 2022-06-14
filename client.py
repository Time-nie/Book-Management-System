# -*- codeing=utf-8 -*-
# @Time : 2022-05-25 23:43
# @Author : 聂志强
# @File : client.py
# @Software : PyCharm

from socket import *
import pymysql
import sqlite3
from tkinter import *
from tkinter import ttk
import tkinter
from tkinter import messagebox
from tkinter.messagebox import *
from PIL import Image, ImageTk
import time


# 向服务器发送请求
def connect(string):
    # 服务器IP
    serverName = "114.116.89.58"
    # 服务器端口
    serverPort = 8401
    client = socket(AF_INET, SOCK_STREAM)
    # 与服务器建立连接并发送数据参数
    client.connect((serverName, serverPort))
    client.send(string.encode())
    # 接受服务器回传数据
    receive = client.recv(2048).decode()
    # 断开连接
    client.close()
    return receive


service = {
    'registerInfo': "1",
    'signInfo': "2",
    'search_reader': "3",
    'choose_reader': "4",
    'new_reader': "5",
    'find_book': "6",
    'find_number': "7",
    'find_name': "8",
    's_bookshelf': "9",
    'f3': "10",
    'change': "11",
    'change_choose': "12",
    'change_all': "13",
    'change_name': "14",
    'change_location': "15",
    'change_price': "16",
    'delete': "17",
    'f4': "18",
    'f6': "19",
}


def registerInfo():
    root.withdraw()
    top = Toplevel()
    top.title('注册页面')
    top.geometry('700x500')

    # 加载图片
    canvas = tkinter.Canvas(top, width=700, height=500, bg=None)
    image = canvas.create_image(0, 0, anchor='nw', image=image_file_login)
    canvas.pack()

    # 返回
    def quiteInfo():
        top.withdraw()
        root.deiconify()

    def register():
        if id.get() == "":
            showerror(title='提示', message='输入不能为空')
        elif name.get() == "":
            showerror(title='提示', message='输入不能为空')
        elif password.get() == "":
            showerror(title='提示', message='输入不能为空')
        elif len(password.get()) < 5:
            showerror(title='提示', message='密码不能小于5位')
        else:
            string = "service=" + service['registerInfo'] + "&&&name=" + name.get() + \
                     "&&&id=" + id.get() + "&&&password=" + password.get()
            flag = connect(string)
            if flag == "1":
                showinfo(title='提示', message="注册成功")
                quiteInfo()
            else:
                messagebox.showerror('注册失败')

    def toggle_password():
        if passwd_entry.cget('show') == '':
            passwd_entry.config(show='*')
            toggle_btn.config(text='Show Password')
        else:
            passwd_entry.config(show='')
            toggle_btn.config(text='Hide Password')

    Label(top, text="ID：", font=(20,)).place(relx=0.3, rely=0.1, relwidth=0.1, height=25)
    Entry(top, textvariable=id).place(relx=0.5, rely=0.1, relwidth=0.2, height=25)
    Label(top, text="姓名：", font=(20,)).place(relx=0.3, rely=0.2, relwidth=0.1, height=25)
    Entry(top, textvariable=name).place(relx=0.5, rely=0.2, relwidth=0.2, height=25)
    Label(top, text="密码(不少于5位)：", font=(20,)).place(relx=0.22, rely=0.3, relwidth=0.26, height=25)
    passwd_entry = Entry(top, textvariable=password, show='*')
    passwd_entry.place(relx=0.5, rely=0.3, relwidth=0.2, height=25)
    toggle_btn = ttk.Button(top, text='Show Password', command=toggle_password)
    toggle_btn.place(relx=0.73, rely=0.3, relwidth=0.1, height=25)
    Button(top, text="注册", command=register, font=(20,)).place(relx=0.53, rely=0.5, width=200, height=25)
    Button(top, text="返回上一页", command=quiteInfo, font=(20,)).place(relx=0.2, rely=0.5, width=200, height=25)


# 登录界面
def signInfo():
    root.withdraw()
    top = Toplevel()
    top.geometry('700x500')
    top.title('登录界面')

    # 加载图片
    canvas = tkinter.Canvas(top, width=700, height=500, bg=None)
    image = canvas.create_image(0, 0, anchor='nw', image=image_file_login)
    canvas.pack()

    def quiteInfo():
        top.withdraw()
        root.deiconify()

    def check():
        if id.get() == "":
            showerror(title='提示', message='输入不能为空')
        elif password.get() == "":
            showerror(title='提示', message='输入不能为空')
        else:
            string = "service=" + service['signInfo'] + "&&&id=" + id.get() + \
                     "&&&password=" + password.get()
            flag = connect(string)
            if flag == "1":
                showinfo(title='提示', message="登录成功")
                top.withdraw()
                num = id.get()
                print("成功")
                main_choose(num)
            else:
                showerror(title='提示', message='ID或密码有错，登录失败')

    Label(top, text="ID：", font=('楷体', 20,)).place(relx=0.32, rely=0.2, relwidth=0.13, height=30)
    Label(top, text="密码：", font=('楷体', 20)).place(relx=0.32, rely=0.3, relwidth=0.13, height=30)
    Entry(top, textvariable=id, font=('楷体', 20)).place(relx=0.5, rely=0.2, relwidth=0.15, height=30)
    Entry(top, textvariable=password, font=('楷体', 20)).place(relx=0.5, rely=0.3, relwidth=0.15, height=30)
    Button(top, text="登录", command=check, font=('楷体', 20)).place(relx=0.35, rely=0.5, width=200, height=30)
    Button(top, text="返回上一页", command=quiteInfo, font=('楷体', 20)).place(relx=0.35, rely=0.6, width=200, height=30)


# 选择中心
def main_choose(id):
    top = Toplevel()
    top.geometry('700x500')
    # 加载图片
    canvas = tkinter.Canvas(top, width=700, height=500, bg=None)
    image = canvas.create_image(0, 0, anchor='nw', image=image_file_choose2)
    canvas.pack()

    def handler():
        onCloseOtherFrame(top)
        top.withdraw()

    handler = lambda: onCloseOtherFrame(top)
    Text(top, width=300, height=200, font=("微软雅黑", 50), )
    btn = Button(top, text="退出", command=handler)
    btn.pack(side='bottom', anchor='ne')

    Label(top, foreground='blue', text='图 书 馆 管 理 系 统',
          font=('华文琥珀', 30), width=17, height=2).place(relx=0.23, rely=0.1)

    # 文本或图像在背景内容区的位置：anchor
    search2 = lambda: search(top, id)
    change2 = lambda: change(top, id)
    delete2 = lambda: delete(top, id)
    add2 = lambda: add(top)

    Button(top, text='查询中心', command=search2).place(relx=0.35, rely=0.3, relwidth=0.3, height=40)
    Button(top, text='更新图书信息', command=change2).place(relx=0.35, rely=0.4, relwidth=0.3, height=40)
    Button(top, text='添加借还信息', command=add2).place(relx=0.35, rely=0.5, relwidth=0.3, height=40)
    Button(top, text='删除图书管理信息', command=delete2).place(relx=0.35, rely=0.6, relwidth=0.3, height=40)
    Button(top, text='退出', command=handler).place(relx=0.9, rely=0.95, relwidth=0.1)


# 总查询
def search(old_otherFrame, id):
    old_otherFrame.withdraw()
    otherFrame = Toplevel()

    def quiteInfo():
        otherFrame.withdraw()
        old_otherFrame.deiconify()

    def handler():
        onCloseOtherFrame(old_otherFrame)
        otherFrame.withdraw()

    otherFrame.geometry('700x500')

    # 加载图片
    canvas = tkinter.Canvas(otherFrame, width=700, height=500, bg=None)
    image = canvas.create_image(0, 0, anchor='nw', image=image_file_choose2)
    canvas.pack()

    Label(otherFrame, foreground='blue', text='查 询 中 心', font=('华文琥珀', 30), width=20, height=2).place(relx=0.2,
                                                                                                      rely=0.1)
    # 文本或图像在背景内容区的位置：anchor
    searchbook2 = lambda: searchbook(otherFrame, id)
    search_record2 = lambda: search_record(otherFrame)
    search_bookshelf2 = lambda: search_bookshelf(otherFrame)
    search_reader2 = lambda: search_reader(otherFrame)
    Button(otherFrame, text='查询图书', command=searchbook2).place(relx=0.23, rely=0.35, relwidth=0.25, height=40)
    Button(otherFrame, text='查询借还信息', command=search_record2, ).place(relx=0.53, rely=0.35, relwidth=0.25, height=40)
    Button(otherFrame, text='查询书架图书信息', command=search_bookshelf2, ).place(relx=0.23, rely=0.45, relwidth=0.25,
                                                                           height=40)
    Button(otherFrame, text='查询读者信息', command=search_reader2, ).place(relx=0.53, rely=0.45, relwidth=0.25, height=40)
    Button(otherFrame, text="返回上一页", command=quiteInfo).place(relx=0.37, rely=0.55, relwidth=0.25, height=40)
    Button(otherFrame, text='退出', command=handler).place(relx=0.9, rely=0.95, relwidth=0.1)


# 查询读者信息
def search_reader(old_otherFrame):
    old_otherFrame.withdraw()
    otherFrame = Toplevel()

    def quiteInfo():
        otherFrame.withdraw()
        old_otherFrame.deiconify()

    otherFrame.geometry("800x600")
    otherFrame.title("查询读者信息")
    # 加载图片
    canvas = tkinter.Canvas(otherFrame, width=800, height=600, bg=None)
    image = canvas.create_image(0, 0, anchor='nw', image=image_file_choose)
    canvas.pack()

    # 返回
    def quiteInfo():
        otherFrame.withdraw()
        old_otherFrame.deiconify()

    # 退出
    def handler():
        onCloseOtherFrame(old_otherFrame)
        otherFrame.withdraw()

    Button(otherFrame, text='退出', command=handler).place(relx=0.9, rely=0.95, relwidth=0.1)
    string = "service=" + service['search_reader']
    res = connect(string).split('#')
    result = []
    for i in res:
        temp = tuple(i.split(','))
        result.append(temp)
    result = tuple(result)
    tree = ttk.Treeview(otherFrame)
    ls = ["学号", "姓名", "性别", "密码", "欠费", "可借图书", "在借图书"]
    tree["columns"] = ("学号", "姓名", "性别", "密码", "欠费", "可借图书", "在借图书")
    for i in ls:
        tree.column(i, anchor="center", width=85)
        tree.heading(i, text=i)
    for i in range(len(result)):
        tree.insert("", i, values=result[i])
    tree['show'] = 'headings'
    tree.place(relx=0.15, rely=0.05, relheight=0.2)
    # 滚动条插件
    VScroll1 = Scrollbar(tree, orient='vertical', command=tree.yview)
    VScroll1.place(relx=0.971, rely=0.028, relwidth=0.024, relheight=0.958)
    # 给treeview添加配置
    tree.configure(yscrollcommand=VScroll1.set)

    Label(otherFrame, text='请输入查询读者学号', font=('Arial', 18)).place(relx=0.3, rely=0.4, relwidth=0.4)
    s_num = StringVar()
    Entry(otherFrame, textvariable=s_num, font=('Arial', 14)).place(relx=0.4, rely=0.47, relwidth=0.2)
    new = lambda: choose_reader(otherFrame, s_num)
    Button(otherFrame, text='查询', command=new).place(relx=0.4, rely=0.54, relwidth=0.2)
    add_reader2 = lambda: add_reader(otherFrame)
    Button(otherFrame, text='添加读者信息', command=add_reader2).place(relx=0.4, rely=0.61, relwidth=0.2)
    Button(otherFrame, text="返回上一页", command=quiteInfo).place(relx=0.4, rely=0.9, relwidth=0.2)


# 选择读者
def choose_reader(otherFrame, s_num):
    string = "service=" + service['choose_reader'] + "&&&s_num=" + s_num.get()
    res = connect(string).split('#')
    result = []
    for i in res:
        temp = tuple(i.split(','))
        result.append(temp)
    result = tuple(result)

    tree = ttk.Treeview(otherFrame)
    ls = ["学号", "姓名", "性别", "密码", "欠费", "可借图书", "在借图书"]
    tree["columns"] = ("学号", "姓名", "性别", "密码", "欠费", "可借图书", "在借图书")
    for i in ls:
        tree.column(i, anchor="center", width=85)
        tree.heading(i, text=i)
    for i in range(len(result)):
        tree.insert("", i, values=result[i])
    tree['show'] = 'headings'
    tree.place(relx=0.15, rely=0.28, relheight=0.1)


# 添加读者信息（输入）
def add_reader(otherFrame):
    s_num = StringVar()
    Label(otherFrame, text="学号：", font=('楷体', 20,)).place(relx=0.17, rely=0.68, relwidth=0.13, height=30)
    Entry(otherFrame, textvariable=s_num, font=('楷体', 20)).place(relx=0.33, rely=0.68, relwidth=0.15, height=30)
    s_name = StringVar()
    Label(otherFrame, text="姓名：", font=('楷体', 20)).place(relx=0.55, rely=0.68, relwidth=0.13, height=30)
    Entry(otherFrame, textvariable=s_name, font=('楷体', 20)).place(relx=0.7, rely=0.68, relwidth=0.15, height=30)
    s_gender = StringVar()
    Label(otherFrame, text="性别：", font=('楷体', 20)).place(relx=0.17, rely=0.75, relwidth=0.13, height=30)
    Entry(otherFrame, show='', textvariable=s_gender, font=('楷体', 20)).place(relx=0.33, rely=0.75, relwidth=0.15,
                                                                             height=30)
    s_pass = StringVar()
    Label(otherFrame, text="密码：", font=('楷体', 20)).place(relx=0.55, rely=0.75, relwidth=0.15, height=30)
    Entry(otherFrame, show='', textvariable=s_pass, font=('楷体', 20)).place(relx=0.7, rely=0.75, relwidth=0.15,
                                                                           height=30)
    new_reader2 = lambda: new_reader(otherFrame, s_num, s_name, s_gender, s_pass)
    Button(otherFrame, text='一键添加', command=new_reader2).place(relx=0.4, rely=0.83, relwidth=0.2)


# 添加读者信息（执行）
def new_reader(otherFrame, s_num, s_name, s_gender, s_pass):
    s_num = s_num.get()
    s_name = s_name.get()
    s_gender = s_gender.get()
    s_pass = s_pass.get()
    flag = "0"
    string = "service=" + service['new_reader'] + \
             "&&&s_num=" + s_num + "&&&s_name=" + s_name + "&&&s_gender=" + s_gender + "&&&s_pass=" + s_pass
    flag = connect(string)
    if flag == "1":
        messagebox.showinfo(message='添加该读者信息成功！')
    else:
        messagebox.showerror('添加失败')


# 查询图书
def searchbook(old_otherFrame, id):
    old_otherFrame.withdraw()
    otherFrame = Toplevel()
    otherFrame.geometry("800x600")
    otherFrame.title("查询图书")
    # 加载图片
    canvas = tkinter.Canvas(otherFrame, width=800, height=600, bg=None)
    image = canvas.create_image(0, 0, anchor='nw', image=image_file_choose)
    canvas.pack()

    def quiteInfo():
        otherFrame.withdraw()
        old_otherFrame.deiconify()

    def handler():
        onCloseOtherFrame(old_otherFrame)
        otherFrame.withdraw()

    Button(otherFrame, text='退出', command=handler).place(relx=0.9, rely=0.95, relwidth=0.1)
    Label(otherFrame, text='请输入书号', font=('微软雅黑', 18)).place(relx=0.3, rely=0.15, relwidth=0.2)
    e1 = StringVar()
    Entry(otherFrame, show='', textvariable=e1, font=('微软雅黑', 14)).place(relx=0.5, rely=0.15, relwidth=0.1)
    click = lambda: find_book(otherFrame, e1)
    click2 = lambda: change(otherFrame, id)
    Button(otherFrame, text='查询', command=click).place(relx=0.38, rely=0.6, relwidth=0.2)
    Button(otherFrame, text='更新图书信息', command=click2).place(relx=0.38, rely=0.7, relwidth=0.2)
    Button(otherFrame, text="返回上一页", command=quiteInfo).place(relx=0.38, rely=0.8, relwidth=0.2)


def find_book(otherFrame, e1):
    book_num = e1.get()
    string = "service=" + service['find_book'] + "&&&book_num=" + book_num
    res = connect(string).split('#')
    if res[0] == '@':
        messagebox.showinfo(message='该图书不存在')
    result = []
    for i in res:
        temp = tuple(i.split(','))
        result.append(temp)
    result = tuple(result)
    tree = ttk.Treeview(otherFrame)
    ls = ["书架号", "书号", "书名", "作者", "价格", "在馆数量", "馆藏总数", "位置", "管理员ID"]
    # 设置列标识符
    tree["columns"] = ("书架号", "书号", "书名", "作者", "价格", "在馆数量", "馆藏总数", "位置", "管理员ID")
    for i in ls:
        tree.column(i, anchor="center", width=85)
        tree.heading(i, text=i)
    for i in range(len(result)):
        tree.insert("", i, values=result[i])
    tree['show'] = 'headings'
    tree.place(relx=0.02, rely=0.3, relheight=0.15)
    if len(result) == 0:
        messagebox.showinfo(message='所查询图书不存在')


# 查询某本书借还信息
def search_record(old_otherFrame):
    old_otherFrame.withdraw()
    otherFrame = Toplevel()
    otherFrame.geometry("800x600")
    otherFrame.title("查询借书信息")
    # 加载图片
    canvas = tkinter.Canvas(otherFrame, width=800, height=600, bg=None)
    image = canvas.create_image(0, 0, anchor='nw', image=image_file_choose)
    canvas.pack()

    def quiteInfo():
        otherFrame.withdraw()
        old_otherFrame.deiconify()

    def handler():
        onCloseOtherFrame(old_otherFrame)
        otherFrame.withdraw()

    Button(otherFrame, text="退出", command=handler, font=('楷体', 10)).place(relx=0.9, rely=0.95, relwidth=0.1)
    Label(otherFrame, text='请输入书号', font=('楷体', 18)).place(relx=0.2, rely=0.1, relwidth=0.2)
    e1 = StringVar()
    Entry(otherFrame, show='', textvariable=e1, font=('楷体', 14)).place(relx=0.45, rely=0.1, relwidth=0.2)
    Label(otherFrame, text='请输入学号', font=('楷体', 18)).place(relx=0.2, rely=0.2, relwidth=0.2)
    e2 = StringVar()
    Entry(otherFrame, show='', textvariable=e2, font=('楷体', 14)).place(relx=0.45, rely=0.2, relwidth=0.2)
    click = lambda: find_number(otherFrame, e1)
    click2 = lambda: find_name(otherFrame, e2)
    click3 = lambda: add(otherFrame)
    Button(otherFrame, text='按书号查询', command=click, font=('楷体', 14)).place(relx=0.38, rely=0.65, relwidth=0.2)
    Button(otherFrame, text='按学号查询', command=click2, font=('楷体', 14)).place(relx=0.38, rely=0.73, relwidth=0.2)
    Button(otherFrame, text='添加借书信息', command=click3, font=('楷体', 14)).place(relx=0.38, rely=0.81, relwidth=0.2)
    Button(otherFrame, text="返回上一页", command=quiteInfo, font=('楷体', 14)).place(relx=0.38, rely=0.9, relwidth=0.2)


# 按书号查询
def find_number(otherFrame, e1):
    book_number = e1.get()
    string = "service=" + service['find_number'] + "&&&book_number=" + book_number
    res = connect(string).split('#')
    if res[0] == '@':
        messagebox.showinfo(message='该图书不存在借阅记录')
        res = ""
    result = []
    for i in res:
        temp = tuple(i.split(','))
        result.append(temp)
    result = tuple(result)
    tree = ttk.Treeview(otherFrame)
    # columns为列名集合
    ls = ["学号", "书名", "书号", "借书时间"]
    tree["columns"] = ("学号", "书名", "书号", "借书时间")
    for i in ls:
        tree.column(i, anchor="center", width=180)
        tree.heading(i, text=i)
    for i in range(len(result)):
        tree.insert("", i, values=result[i])
    tree['show'] = 'headings'
    tree.place(relx=0.06, rely=0.3, relheight=0.3)
    # 滚动条控件
    VScroll1 = Scrollbar(tree, orient='vertical', command=tree.yview)
    VScroll1.place(relx=0.971, rely=0.028, relwidth=0.024, relheight=0.958)
    # 给treeview添加配置
    tree.configure(yscrollcommand=VScroll1.set)


# 按学号查询
def find_name(otherFrame, e1):
    student_num = e1.get()
    string = "service=" + service['find_name'] + "&&&student_num=" + student_num
    res = connect(string).split('#')
    if res[0] == '@':
        messagebox.showinfo(message='该学生不存在借阅记录')
        res = ""
    result = []
    for i in res:
        temp = tuple(i.split(','))
        result.append(temp)
    result = tuple(result)
    tree = ttk.Treeview(otherFrame)
    # columns为列名集合
    ls = ["学号", "书名", "书号", "借书时间"]
    tree["columns"] = ("学号", "书名", "书号", "借书时间")
    for i in ls:
        tree.column(i, anchor="center", width=180)
        tree.heading(i, text=i)
    for i in range(len(result)):
        tree.insert("", i, values=result[i])
    tree['show'] = 'headings'
    tree.place(relx=0.06, rely=0.3, relheight=0.3)
    # 滚动条控件
    VScroll1 = Scrollbar(tree, orient='vertical', command=tree.yview)
    VScroll1.place(relx=0.971, rely=0.028, relwidth=0.024, relheight=0.958)
    # 给treeview添加配置
    tree.configure(yscrollcommand=VScroll1.set)


# 查询某个书架的图书信息
def search_bookshelf(old_otherFrame):
    old_otherFrame.withdraw()
    otherFrame = Toplevel()
    otherFrame.geometry("800x600")
    otherFrame.title("查询书架图书信息")
    # 加载图片
    canvas = tkinter.Canvas(otherFrame, width=800, height=600, bg=None)
    image = canvas.create_image(0, 0, anchor='nw', image=image_file_choose)
    canvas.pack()

    def quiteInfo():
        otherFrame.withdraw()
        old_otherFrame.deiconify()

    def handler():
        onCloseOtherFrame(old_otherFrame)
        otherFrame.withdraw()

    Button(otherFrame, text="返回上一页", command=quiteInfo).place(relx=0.38, rely=0.9, relwidth=0.2)
    Text(otherFrame, width=300, height=200, font=("微软雅黑", 50), )
    Button(otherFrame, text='退出', command=handler).place(relx=0.9, rely=0.95, relwidth=0.1)
    Label(otherFrame, text='请输入书架号', font=('微软雅黑', 18)).place(relx=0.3, rely=0.1, relwidth=0.2)
    e1 = StringVar()
    Entry(otherFrame, show='', textvariable=e1, font=('微软雅黑', 14)).place(relx=0.5, rely=0.1, relwidth=0.2)
    click = lambda: s_bookshelf(otherFrame, e1)
    Button(otherFrame, text='查询', command=click).place(relx=0.38, rely=0.8, relwidth=0.2)


def s_bookshelf(otherFrame, e1):
    book_num = e1.get()
    string = "service=" + service['s_bookshelf'] + "&&&book_num=" + book_num
    res = connect(string).split('#')
    result = []
    for i in res:
        temp = tuple(i.split(','))
        result.append(temp)
    result = tuple(result)
    tree = ttk.Treeview(otherFrame)
    ls = ["位置", "书号", "书名", "作者", "价格", "在馆数量", "馆藏总数", "书架号", "管理员ID"]
    tree["columns"] = ("位置", "书号", "书名", "作者", "价格", "在馆数量", "馆藏总数", "书架号", "管理员ID")
    for i in ls:
        tree.column(i, anchor="center", width=85)
        tree.heading(i, text=i)
    for i in range(len(result)):
        tree.insert("", i, values=result[i])
    tree['show'] = 'headings'

    tree.place(relx=0.02, rely=0.3, relheight=0.4)
    # 滚动条
    VScroll1 = Scrollbar(tree, orient='vertical', command=tree.yview)
    VScroll1.place(relx=0.971, rely=0.028, relwidth=0.024, relheight=0.958)
    # 给treeview添加配置
    tree.configure(yscrollcommand=VScroll1.set)

    if len(result) == 0:
        messagebox.showinfo(message='所查询书架不存在图书')


# 触发器添加借还信息
def add(old_otherFrame):
    old_otherFrame.withdraw()
    otherFrame = Toplevel()

    otherFrame.geometry("800x600")
    otherFrame.title("借书申请")
    # 加载图片
    canvas = tkinter.Canvas(otherFrame, width=800, height=600, bg=None)
    image = canvas.create_image(0, 0, anchor='nw', image=image_file_choose)
    canvas.pack()

    def quiteInfo():
        otherFrame.withdraw()
        old_otherFrame.deiconify()

    handler = lambda: onCloseOtherFrame(otherFrame)
    Text(otherFrame, width=300, height=200, font=("微软雅黑", 50), )
    Button(otherFrame, text="退出", command=handler, font=('Arial', 10)).place(relx=0.9, rely=0.95, relwidth=0.1)
    Label(otherFrame, text='请输入学号', font=('Arial', 18)).place(relx=0.2, rely=0.1, relwidth=0.25)
    e1 = StringVar()
    Entry(otherFrame, show='', textvariable=e1, font=('Arial', 14)).place(relx=0.5, rely=0.1, relwidth=0.25)

    Label(otherFrame, text='请输入书号', font=('Arial', 18)).place(relx=0.2, rely=0.2, relwidth=0.25)
    e2 = StringVar()
    Entry(otherFrame, show='', textvariable=e2, font=('Arial', 14)).place(relx=0.5, rely=0.2, relwidth=0.25)

    Label(otherFrame, text='请输入借书时间', font=('Arial', 18)).place(relx=0.2, rely=0.3, relwidth=0.25)
    e3 = StringVar()
    Entry(otherFrame, show='', textvariable=e3, font=('Arial', 14)).place(relx=0.5, rely=0.3, relwidth=0.25)

    click = lambda: f3(otherFrame, e1, e2, e3)
    Button(otherFrame, text='插入', command=click, font=(14)).place(relx=0.35, rely=0.7, width=200)
    Button(otherFrame, text="返回上一页", command=quiteInfo, font=(14)).place(relx=0.35, rely=0.8, width=200)


def f3(otherFrame, e1, e2, e3):
    student_number = e1.get()
    book_number = e2.get()
    b_time = e3.get()
    print(student_number)
    print(book_number)
    print(b_time)
    string = "service=" + service['f3'] + "&&&student_number=" + student_number + \
             "&&&book_number=" + book_number + "&&&b_time=" + b_time
    flag = connect(string)
    if flag == "1":
        showinfo(title='提示', message="添加成功")
    else:
        showerror(title='提示', message='添加失败')


# 更新某个管理员管理的图书信息
def change(old_otherFrame, id):
    old_otherFrame.withdraw()
    otherFrame = Toplevel()
    otherFrame.geometry("800x600")
    otherFrame.title("更新信息")
    # 加载图片
    canvas = tkinter.Canvas(otherFrame, width=800, height=600, bg=None)
    image = canvas.create_image(0, 0, anchor='nw', image=image_file_choose)
    canvas.pack()

    # 返回上一页
    def quiteInfo():
        otherFrame.withdraw()
        old_otherFrame.deiconify()

    # 退出
    def handler():
        onCloseOtherFrame(old_otherFrame)
        otherFrame.withdraw()

    Button(otherFrame, text='退出', command=handler).place(relx=0.9, rely=0.95, relwidth=0.1)
    string = "service=" + service['change'] + "&&&id=" + id
    res = connect(string).split('#')
    if res[0] == '@':
        messagebox.showinfo(message='当前管理员权限下无图书')
        quiteInfo()
    result = []
    for i in res:
        temp = tuple(i.split(','))
        result.append(temp)
    result = tuple(result)
    tree = ttk.Treeview(otherFrame)
    ls = ["位置", "书号", "书名", "作者", "价格", "在馆数量", "馆藏总数", "书架号", "管理员ID"]
    tree["columns"] = ("位置", "书号", "书名", "作者", "价格", "在馆数量", "馆藏总数", "书架号", "管理员ID")
    for i in ls:
        tree.column(i, anchor="center", width=85)
        tree.heading(i, text=i)
    for i in range(len(result)):
        tree.insert("", i, values=result[i])
    tree['show'] = 'headings'
    tree.place(relx=0.02, rely=0.07, relheight=0.2)
    # 滚动控件
    VScroll1 = Scrollbar(tree, orient='vertical', command=tree.yview)
    VScroll1.place(relx=0.971, rely=0.028, relwidth=0.024, relheight=0.958)
    # 给treeview添加配置
    tree.configure(yscrollcommand=VScroll1.set)
    Button(otherFrame, text="返回上一页", command=quiteInfo).place(relx=0.4, rely=0.65, relwidth=0.2)

    if len(result) != 0:
        Label(otherFrame, text='请输入待更新书号', font=('Arial', 18)).place(relx=0.3, rely=0.32, relwidth=0.4)
        num = StringVar()
        Entry(otherFrame, show='', textvariable=num, font=('Arial', 14)).place(relx=0.4, rely=0.4, relwidth=0.2)
        new = lambda: change_choose(otherFrame, num)
        Button(otherFrame, text='选择更新内容', command=new).place(relx=0.4, rely=0.58, relwidth=0.2)
    else:
        messagebox.showinfo(message='无可更新图书')


def change_choose(otherFrame, num):
    # 显示所选更新图书信息
    num = num.get()
    string = "service=" + service['change_choose'] + "&&&num=" + num
    res = connect(string).split('#')
    result = []
    for i in res:
        temp = tuple(i.split(','))
        result.append(temp)
    result = tuple(result)

    tree = ttk.Treeview(otherFrame)
    ls = ["位置", "书号", "书名", "作者", "价格", "在馆数量", "馆藏总数", "书架号", "管理员ID"]
    tree["columns"] = ("位置", "书号", "书名", "作者", "价格", "在馆数量", "馆藏总数", "书架号", "管理员ID")
    for i in ls:
        tree.column(i, anchor="center", width=85)
        tree.heading(i, text=i)
    for i in range(len(result)):
        tree.insert("", i, values=result[i])
    tree['show'] = 'headings'
    tree.place(relx=0.02, rely=0.46, relheight=0.1)
    if result[0][1] == num:
        name = result[0][2]
        location = result[0][0]
        price = result[0][4]
    # 控件设置
    e3 = StringVar()
    Entry(otherFrame, textvariable=e3, font=('Arial', 14)).place(relx=0.5, rely=0.73)
    click1 = lambda: change_name(otherFrame, e3, name)
    Button(otherFrame, text='更新书名', command=click1).place(relx=0.25, rely=0.73, relwidth=0.2)
    e4 = StringVar()
    Entry(otherFrame, textvariable=e4, font=('Arial', 14)).place(relx=0.5, rely=0.79)
    click2 = lambda: change_location(otherFrame, e4, location)
    Button(otherFrame, text="更新位置", command=click2, ).place(relx=0.25, rely=0.79, relwidth=0.2)
    e5 = StringVar()
    Entry(otherFrame, textvariable=e5, font=('Arial', 14)).place(relx=0.5, rely=0.85)
    click3 = lambda: change_price(otherFrame, e5, price)
    Button(otherFrame, text="更新价格", command=click3, ).place(relx=0.25, rely=0.85, relwidth=0.2)
    click4 = lambda: change_all(otherFrame, e3, name, e4, location, e5, price, num)
    Button(otherFrame, text="更新全部", command=click4, ).place(relx=0.4, rely=0.91, relwidth=0.2)


# 更改全部信息
def change_all(otherFrame, new_name, old_name, new_location, old_location, new_price, old_price, num):
    new_name = new_name.get()
    new_location = new_location.get()
    new_price = new_price.get()
    flag = "0"
    string = "service=" + service['change_all'] + "&&&new_name=" + new_name + \
             "&&&new_location=" + new_location + "&&&new_price=" \
             + new_price + "&&&old_price=" + old_price + "&&&num=" + num
    flag = connect(string)
    if flag == "1":
        showinfo(title='提示', message="更新成功")
        # otherFrame.withdraw()
        # change(otherFrame, num)
    else:
        showerror(title='提示', message='更新失败')


# 单独更改书名
def change_name(otherFrame, new, old):
    new = new.get()
    string = "service=" + service['change_name'] + "&&&new=" + new + "&&&old=" + old
    flag = connect(string)
    if flag == "1":
        showinfo(title='提示', message="更新成功")
    else:
        showerror(title='提示', message='更新失败')


# 单独更改位置
def change_location(otherFrame, new, old):
    new = new.get()
    string = "service=" + service['change_location'] + "&&&new=" + new + "&&&old=" + old
    flag = connect(string)
    if flag == "1":
        showinfo(title='提示', message="更新成功")
    else:
        showerror(title='提示', message='更新失败')


# 单独更改价格
def change_price(otherFrame, new, old):
    new = new.get()
    string = "service=" + service['change_price'] + "&&&new=" + new + "&&&old=" + old
    flag = connect(string)
    if flag == "1":
        showinfo(title='提示', message="更新成功")
    else:
        showerror(title='提示', message='更新失败')


# 删除某个管理员的指定书籍
# 连接book和bookshelf
def delete(old_otherFrame, id):
    old_otherFrame.withdraw()
    otherFrame = Toplevel()
    otherFrame.geometry("800x600")
    otherFrame.title("删除书籍")
    # 加载图片
    canvas = tkinter.Canvas(otherFrame, width=800, height=600, bg=None)
    image = canvas.create_image(0, 0, anchor='nw', image=image_file_choose)
    canvas.pack()

    # 退出
    def quiteInfo():
        otherFrame.withdraw()
        old_otherFrame.deiconify()

    # 返回上一页
    def handler():
        onCloseOtherFrame(old_otherFrame)
        otherFrame.withdraw()

    tree = ttk.Treeview(otherFrame)
    ls = ["管理员ID", "书号", "书名", "书架号"]
    tree["columns"] = ("管理员ID", "书号", "书名", "书架号")
    for i in ls:
        tree.column(i, anchor="center", width=180)
        tree.heading(i, text=i)
    string = "service=" + service['delete'] + "&&&id=" + id
    res = connect(string).split('#')
    if res[0] == '@':
        messagebox.showinfo(message='当前管理员权限下无图书')
        quiteInfo()
    result = []
    for i in res:
        temp = tuple(i.split(','))
        result.append(temp)
    result = tuple(result)
    for i in range(len(result)):
        tree.insert("", i, values=result[i])
    tree['show'] = 'headings'
    tree.place(relx=0.05, rely=0.05, relheight=0.3)
    # 滚动条控件
    VScroll1 = Scrollbar(tree, orient='vertical', command=tree.yview)
    VScroll1.place(relx=0.971, rely=0.028, relwidth=0.024, relheight=0.958)
    # 给treeview添加配置
    tree.configure(yscrollcommand=VScroll1.set)
    Label(otherFrame, text='请输入书号', font=('Arial', 18)).place(relx=0.37, rely=0.5, width=200)
    e1 = StringVar()
    Entry(otherFrame, show='', textvariable=e1, font=('Arial', 14)).place(relx=0.37, rely=0.6, width=200)

    click = lambda: f4(otherFrame, e1, id, old_otherFrame)
    Button(otherFrame, text='删除所选书号', command=click).place(relx=0.37, rely=0.7, width=200)

    click2 = lambda: f6(otherFrame, id, old_otherFrame)
    Button(otherFrame, text='删除全部图书信息', command=click2).place(relx=0.37, rely=0.8, width=200)
    Button(otherFrame, text="返回上一页", command=quiteInfo).place(relx=0.37, rely=0.9, width=200)
    Button(otherFrame, text='退出', command=handler).place(relx=0.9, rely=0.95, relwidth=0.1)


def f4(otherFrame, e1, id, old_otherFrame):
    e1 = e1.get()
    string = "service=" + service['f4'] + "&&&e1=" + e1
    flag = connect(string)
    if flag == "1":
        showinfo(title='提示', message="删除所选图书信息成功")
        otherFrame.withdraw()
        delete(old_otherFrame, id)
    else:
        showerror(title='提示', message='删除所选图书信息失败')


def f6(otherFrame, id, old_otherFrame):
    string = "service=" + service['f6'] + "&&&id=" + id
    flag = connect(string)
    if flag == "1":
        showinfo(title='提示', message="全部删除成功")
        otherFrame.withdraw()
        delete(old_otherFrame, id)
    else:
        showerror(title='提示', message='全部删除失败')


def onCloseOtherFrame(otherFrame):
    """"""
    otherFrame.destroy()
    show()


def show():
    """
    shows main frame
    """
    root.update()
    root.deiconify()


if __name__ == '__main__':
    try:
        root = Tk()
        root.geometry('800x600')
        root.title('图书管理系统')

        # 加载图像
        canvas = tkinter.Canvas(root, width=800, height=600, bg=None)
        # 打开图片.jpg格式图片需要用PIL模块的PhotoImage打开
        img_root = Image.open("library.jpg")
        image_file_root = ImageTk.PhotoImage(img_root)

        image = canvas.create_image(0, 0, anchor='nw', image=image_file_root)
        canvas.pack()

        img_login = Image.open("login.jpg")
        image_file_login = ImageTk.PhotoImage(img_login)

        img_choose = Image.open("choose.jpg")
        image_file_choose = ImageTk.PhotoImage(img_choose)

        img_choose2 = Image.open("choose2.jpg")
        image_file_choose2 = ImageTk.PhotoImage(img_choose2)
        # 设为全局变量，注册/登录只用输入一遍
        id = StringVar()
        name = StringVar()
        password = StringVar()
        Button(root, text="登录", command=signInfo, font=('华文行楷', 20)).place(relx=0.4, rely=0.4, width=200, height=40)
        Button(root, text="个人信息注册", command=registerInfo, font=('华文行楷', 20)).place(relx=0.4, rely=0.6, width=200,
                                                                                   height=40)
        root.mainloop()
    except KeyboardInterrupt:
        print('成功')
