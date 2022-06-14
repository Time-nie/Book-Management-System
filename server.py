# -*- codeing=utf-8 -*-
# @Time : 2022-05-25 23:31
# @Author : 聂志强
# @File : server.py
# @Software : PyCharm
from socket import *
import threading
import time
import pymysql
import sqlite3
from tkinter import *
from tkinter import ttk
import tkinter
from tkinter import messagebox
from tkinter.messagebox import *
from PIL import Image, ImageTk

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

db = pymysql.connect(host="114.116.89.58", user="root", password="SS111827jj!", database="library", port=3306, autocommit=True)
def con():
    # 创建游标对象
    cursor1 = db.cursor()
    cursor = [cursor1, db]
    return cursor


# 注册业务
def res(client, dic):
    cursor = con()[0]
    flag = "0"
    sql = "INSERT INTO administrator values('" + dic['name'] + "', " + dic['id'] + ", " + dic['password'] + ");"
    try:
        cursor.execute(sql)
        flag = "1"
    except Exception:
        print(Exception)
    print(flag)
    client.send(flag.encode())


def sig(client, dic):
    cursor = con()[0]
    flag = "0"
    cursor.execute("select * from administrator")
    message_list = cursor.fetchall()
    num = dic['id']
    password_user = dic['password']
    for i in range(len(message_list)):
        if num == message_list[i][1] and password_user == message_list[i][2]:
            flag = "1"
            break
    client.send(flag.encode())


def s_r(client, dic):
    cursor = con()[0]
    sql = "select * from reader;"
    cursor.execute(sql)
    result = cursor.fetchall()
    if len(result) == 0:
        res = '@'
    else:
        res = ""
        for item in result:
            for i in item:
                res += str(i)
                res += ','
            res += '#'
    client.send(res.encode())


def c_r(client, dic):
    cursor = con()[0]
    sql = "select * from reader where student_number= '" + dic['s_num'] + "' ;"
    cursor.execute(sql)
    result = cursor.fetchall()
    res = ""
    for item in result:
        for i in item:
            res += str(i)
            res += ','
        res += '#'
    client.send(res.encode())


def n_r(client, dic):
    cursor = con()[0]
    sql = "INSERT INTO reader values('" + dic['s_num'] \
          + "', '" + dic['s_name'] + "', '" + dic['s_gender'] + "', '" + dic['s_pass'] + "',0, 5, 0);"
    flag = "0"
    try:
        cursor.execute(sql)
        flag = "1"
    except Exception:
        print(Exception)
    client.send(flag.encode())


def f_b(client, dic):
    cursor = con()[0]
    sql = "select * from book natural join bookshelf where book_number ='" + dic['book_num'] + "';"
    cursor.execute(sql)
    result = cursor.fetchall()
    if len(result) == 0:
        res = '@'
    else:
        res = ""
        for item in result:
            for i in item:
                res += str(i)
                res += ','
            res += '#'
    client.send(res.encode())


def f_number(client, dic):
    cursor = con()[0]
    sql = "select * " \
          "from b_r " \
          "where book_number='" + dic['book_number'] + "';"
    cursor.execute(sql)
    result = cursor.fetchall()
    if len(result) == 0:
        res = '@'
    else:
        res = ""
        for item in result:
            for i in item:
                res += str(i)
                res += ','
            res += '#'
    client.send(res.encode())


def f_name(client, dic):
    cursor = con()[0]
    sql = "select * " \
          "from b_r " \
          "where student_number='" + dic['student_num'] + "';"
    cursor.execute(sql)
    result = cursor.fetchall()
    if len(result) == 0:
        res = '@'
    else:
        res = ""
        for item in result:
            for i in item:
                res += str(i)
                res += ','
            res += '#'
    client.send(res.encode())


def s_b(client, dic):
    cursor = con()[0]
    sql = "select * from book natural join bookshelf where No_bookshelf='" + dic['book_num'] + "';"
    cursor.execute(sql)
    result = cursor.fetchall()
    if len(result) == 0:
        res = '@'
    else:
        res = ""
        for item in result:
            for i in item:
                res += str(i)
                res += ','
            res += '#'
    client.send(res.encode())


def f3(client, dic):
    cursor = con()[0]
    flag = "0"
    try:
        cursor.execute("START TRANSACTION")
        sql = "INSERT INTO borrow_or_return" \
              " values('" + dic['student_number'] + "', '" + dic['book_number'] + "', '" + dic['b_time'] + "');"
        sql2 = "update reader " \
               "set Number_of_books_available =Number_of_books_available-1 " \
               "where student_number ='" + dic['student_number'] + "';"
        sql3 = "update reader " \
               "set Number_of_borrowed_books =Number_of_borrowed_books+1 " \
               "where student_number ='" + dic['student_number'] + "';"
        sql4 = "update book " \
               "set Number_of_books_in_the_library =Number_of_books_in_the_library -1 " \
               "where book_number=" + dic['book_number'] + ";"
        cursor.execute(sql)
        cursor.execute(sql2)
        cursor.execute(sql3)
        cursor.execute(sql4)
        flag = "1"
        db.commit()
    except Exception:
        print(Exception)
        db.rollback()
    client.send(flag.encode())


def change(client, dic):
    cursor = con()[0]
    sql = "select * from book natural join bookshelf where ID='" + dic['id'] + "';"
    cursor.execute(sql)
    result = cursor.fetchall()
    if len(result) == 0:
        res = '@'
    else:
        res = ""
        for item in result:
            for i in item:
                res += str(i)
                res += ','
            res += '#'
    client.send(res.encode())


def c_c(client, dic):
    cursor = con()[0]
    sql = "select * from book natural join bookshelf where book_number='" + dic['num'] + "';"
    cursor.execute(sql)
    result = cursor.fetchall()
    if len(result) == 0:
        res = '@'
    else:
        res = ""
        for item in result:
            for i in item:
                res += str(i)
                res += ','
            res += '#'
    client.send(res.encode())


def change_all(client, dic):
    cursor = con()[0]
    db = con()[1]
    flag = "0"
    try:
        sql1 = "update book natural join bookshelf " \
               "set title= '" + str(dic['new_name']) + "', book.location='" + str(dic['new_location']) + "'" \
                                                                                                         "where  book_number= '" + str(
            dic['num']) + "';"
        sql2 = "call update_price(" + str(dic['new_price']) + ", " + "" + str(dic['old_price']) + ");"
        cursor.execute(sql1)
        cursor.execute(sql2)
        flag = "1"
    except Exception:
        print(Exception)
    client.send(flag.encode())


def change_name(client, dic):
    cursor = con()[0]
    db = con()[1]
    flag = "0"
    sql = "update book set  title= '" + str(dic['new']) + "' where title = '" + str(dic['old']) + "';"
    cursor.execute(sql)
    flag = "1"
    client.send(flag.encode())


def change_location(client, dic):
    cursor = con()[0]
    db = con()[1]
    flag = "0"
    try:
        sql = "update book " \
              "set  location= '" + str(dic['new']) + "' where location = '" + str(dic['old']) + "';"
        cursor.execute(sql)
        flag = "1"
    except Exception:
        print(Exception)
    client.send(flag.encode())


def change_price(client, dic):
    cursor = con()[0]
    db = con()[1]
    flag = "0"
    try:
        sql = "call update_price(" + str(dic['new']) + ", " + "" + str(dic['old']) + ");"
        cursor.execute(sql)
        flag = "1"
    except Exception:
        print(Exception)
    client.send(flag.encode())


def delete(client, dic):
    cursor = con()[0]
    sql = "SELECT ID, book_number,title, No_bookshelf " \
          "from book natural join bookshelf " \
          "where ID= " + dic['id'] + " ;"
    cursor.execute(sql)
    result = cursor.fetchall()
    if len(result) == 0:
        res = '@'
    else:
        res = ""
        for item in result:
            for i in item:
                res += str(i)
                res += ','
            res += '#'
    client.send(res.encode())


def f4(client, dic):
    cursor = con()[0]
    db = con()[1]
    flag = "0"
    try:
        cursor.execute("START TRANSACTION")
        sql = "delete from book  " \
              "where  book_number='" + dic['e1'] + "' ;"
        cursor.execute(sql)
        flag = "1"
        db.commit()
    except Exception :
        print(Exception)
        db.rollback()
    client.send(flag.encode())


def f6(client, dic):
    cursor = con()[0]
    db=con()[1]
    flag = "0"
    try:
        cursor.execute("START TRANSACTION")
        sql = "delete from book " \
              "where location in (select location from bookshelf where ID= '" + dic['id'] + "');"
        # sql2 = "INSERT INTO book VALUES('921','F02','文字之美','徐帆',34.6,1,5);"
        cursor.execute(sql)
        # cursor.execute(sql2)
        flag = "1"
        db.commit()

    except Exception:
        print(Exception)
        db.rollback()
    client.send(flag.encode())


def handle(client):
    # 拿2048字节
    message_recv = client.recv(2048).decode()
    lst = message_recv.split('&&&')
    dic = {}
    for item in lst:
        dic[item.split('=')[0]] = item.split('=')[1]

    if dic['service'] == service['registerInfo']:
        res(client, dic)
    elif dic['service'] == service['signInfo']:
        sig(client, dic)
    elif dic['service'] == service['search_reader']:
        s_r(client, dic)
    elif dic['service'] == service['choose_reader']:
        c_r(client, dic)
    elif dic['service'] == service['new_reader']:
        n_r(client, dic)
    elif dic['service'] == service['find_book']:
        f_b(client, dic)
    elif dic['service'] == service['find_number']:
        f_number(client, dic)
    elif dic['service'] == service['find_name']:
        f_name(client, dic)
    elif dic['service'] == service['s_bookshelf']:
        s_b(client, dic)
    elif dic['service'] == service['f3']:
        f3(client, dic)
    elif dic['service'] == service['change']:
        change(client, dic)
    elif dic['service'] == service['change_choose']:
        c_c(client, dic)
    elif dic['service'] == service['change_all']:
        change_all(client, dic)
    elif dic['service'] == service['change_name']:
        change_name(client, dic)
    elif dic['service'] == service['change_location']:
        change_location(client, dic)
    elif dic['service'] == service['change_price']:
        change_price(client, dic)
    elif dic['service'] == service['delete']:
        delete(client, dic)
    elif dic['service'] == service['f4']:
        f4(client, dic)
    elif dic['service'] == service['f6']:
        f6(client, dic)


if __name__ == '__main__':
    serverPort = 8401
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', serverPort))
    serverSocket.listen(1)
    print("服务器开始服务")
    while True:
        # 建立连接，监听8401端口
        client, address = serverSocket.accept()
        handle2 = lambda: handle(client)
        # 开启新线程
        threading.Thread(target=handle2).start()
