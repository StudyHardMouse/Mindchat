# 语聊 （Zhong Chat)
from tkinter import *
import pymysql
import time
import threading
from tkinter import messagebox
import os
from easygui import *
import datetime
import hashlib
import pygame

def main1():
    try:
        # 初始化
        try:
            a = []
            file = r'C:\语聊文件夹\引导程序.txt'
            with open(file, 'r') as file:
                for line in file:
                    a.append(line.strip())
            b = int(a[0]) - xx
            c = int(a[1]) + xx
            d = int(a[2]) - xx
            e = int(a[3]) + xx
            f = int(a[4]) - xx
            global ip1
            global host1
            ip1 = '{}.{}.{}.{}'.format(b, c, d, e)
            host1 = f
            
        except:
            messagebox.showerror('小金豆', '初始化失败！')
        # GUI登录框架
        win = Tk()
        win.title('语聊')
        win.geometry('354x470')
        win.resizable(False, False)
        win.config(background='white')
        win.iconbitmap(r'C:\语聊文件夹\logo.ico')

        Label(win, text='语聊', bg='white', font=('仿宋', 30), fg='black').place(relx=0.452, rely=0.045, height=65, width=93)
        Label(win, text='手机号', bg='white', font=('微软雅黑', 15), fg='black').place(relx=0.085, rely=0.289, height=45, width=67)
        Label(win, text='密码', bg='white', font=('微软雅黑', 15), fg='black').place(relx=0.1, rely=0.421, height=45, width=57)
        Label23 = Label(win)
        Label23.place(relx=0.254, rely=0.045, height=65, width=70)
        Label23.configure(activebackground="#f9f9f9")
        Label23.configure(anchor='w')
        Label23.configure(background="#ffffff")
        Label23.configure(compound='left')
        Label23.configure(disabledforeground="#a3a3a3")
        Label23.configure(foreground="#000000")
        Label23.configure(highlightbackground="#d9d9d9")
        Label23.configure(highlightcolor="black")
        photo_location = os.path.join(r"C:\语聊文件夹\小标.png")
        global _img0
        _img0 = PhotoImage(file=photo_location)
        Label23.configure(image=_img0)
        e1 = Entry(win, width=35, relief="solid")
        e2 = Entry(win, width=35, show='*', relief="solid")
        e1.place(relx=0.311, rely=0.311, height=27, relwidth=0.548)
        e2.place(relx=0.311, rely=0.445, height=27, relwidth=0.548)

        def no_closing():
            os._exit(0)

        win.protocol('WM_DELETE_WINDOW', no_closing)

        def sign_in():
            # 验证账号
            try:
                conn = pymysql.connect(host=ip1, port=host1, user='root', password='xxx', database='mindchat')   # 连接数据库
                cursor = conn.cursor()                                                   # 连接获取游标
                try:                                                                     # 数据库示范操作，其他命令与其相似
                    sql1 = 'select * from 账号 where 手机号=' + str(e1.get())              # 输入SQL指令读取内容
                    cursor.execute(sql1)                                                 # 执行命令
                    global all1
                    all1 = cursor.fetchone()                                             # 获取其中一行数据（由于账号仅允许一个手机号注册，因此用一个最合适）
                    ghy1 = hashlib.md5()                                                 # 将输入端密码进行md5加密
                    ghy1.update(e2.get().encode('utf-8'))
                    fkp1 = str(ghy1.hexdigest())
                    # print(fkp1)
                    conn.close()                                                         # 关闭连接
                    cursor.close()                                                       # 关闭游标
                    if all1 == None:                                                     # 逻辑代码
                        messagebox.showerror('小金豆', '该账号不存在！')
                    else:
                        passw = all1[2]
                        if fkp1 == passw:
                            messagebox.showinfo('小金豆', '登录成功')
                            win.destroy()
                            f2.start()
                        else:
                            messagebox.showerror('小金豆', '密码错误！')
                except:
                    messagebox.showerror('小金豆', '请检查输入！')
            except:
                messagebox.showerror('小金豆', '服务器未开放！或服务器IP地址已变动，请及时联系管理员更换最新程序')

        def sign_up():
            # 注册账号
            root = Toplevel()
            root.title('注册')
            root.geometry('354x470')
            root.resizable(False, False)
            root.config(background='white')
            root.iconbitmap(r'C:\语聊文件夹\logo.ico')
            fg = datetime.date.today()

            Label(root, text='注册', bg='white', font=('仿宋', 30), fg='black').place(relx=0.452, rely=0.045, height=65, width=93)
            Label(root, text='手机号', bg='white', font=('微软雅黑', 15), fg='black').place(relx=0.085, rely=0.289, height=45, width=67)
            Label(root, text='密码', bg='white', font=('微软雅黑', 15), fg='black').place(relx=0.1, rely=0.421, height=45, width=57)
            Label(root, text='昵称', bg='white', font=('微软雅黑', 15), fg='black').place(x=40, y=265)
            Label(root, text='确认密码', bg='white', font=('微软雅黑', 14), fg='black').place(x=20, y=325)
            Label23 = Label(root)
            Label23.place(relx=0.254, rely=0.045, height=65, width=70)
            Label23.configure(activebackground="#f9f9f9")
            Label23.configure(anchor='w')
            Label23.configure(background="#ffffff")
            Label23.configure(compound='left')
            Label23.configure(disabledforeground="#a3a3a3")
            Label23.configure(foreground="#000000")
            Label23.configure(highlightbackground="#d9d9d9")
            Label23.configure(highlightcolor="black")
            #photo_location = os.path.join(r"C:\语聊文件夹\小标.png")
            #global _img1
            _img1 = PhotoImage(file=photo_location)
            Label23.configure(image=_img0)
            e11 = Entry(root, width=35, relief='solid')
            e22 = Entry(root, width=35, show='*', relief='solid')
            e33 = Entry(root, width=35, relief='solid')
            e44 = Entry(root, width=35, show='*', relief='solid')
            e11.place(relx=0.311, rely=0.311, height=27, relwidth=0.548)
            e22.place(relx=0.311, rely=0.445, height=27, relwidth=0.548)
            e33.place(relx=0.311, rely=0.572, height=27, relwidth=0.548)
            e44.place(relx=0.311, rely=0.702, height=27, relwidth=0.548)

            def signup():
                # 注册账号
                mu = Toplevel()
                mu.title('小金豆-密保验证')
                mu.geometry('400x300+0+0')
                mu.config(background='white')
                mu.resizable(False, False)

                Label(mu, text='密保', bg='white', font=('楷体', 32), fg='black').pack()
                Label(mu, text='生日年份', bg='white', font=('黑体', 15), fg='black').place(x=25, y=55)
                Label(mu, text='生日月份', bg='white', font=('黑体', 15), fg='black').place(x=155, y=55)
                Label(mu, text='生日日份', bg='white', font=('黑体', 15), fg='black').place(x=285, y=55)
                cmb = Entry(mu, width=15,  relief='solid')
                cmb.place(x=10, y=85)
                cmb1 = Entry(mu, width=15, relief='solid')
                cmb1.place(x=140, y=85)
                cmb2 = Entry(mu, width=15, relief='solid')
                cmb2.place(x=270, y=85)
                Label(mu, text='电子邮箱', bg='white', font=('黑体', 15), fg='black').place(x=160, y=120)
                cmb3 = Entry(mu, width=50, relief='solid')
                cmb3.place(x=20, y=150)

                def ner():

                    tyr = '{}-{}-{}'.format(cmb.get(), cmb1.get(), cmb2.get())
                    try:
                        conn = pymysql.connect(host=ip1, port=host1, user='root', password='xxx',database='mindchat')
                        cursor = conn.cursor()
                        cursor1 = conn.cursor()
                        try:
                            sql2 = "select * from 账号 where 手机号=" + str(e11.get())
                            cursor.execute(sql2)
                            all2 = cursor.fetchone()
                            result1 = '@' in cmb3.get()
                            result2 = '.' in cmb3.get()
                            # print(result1, result2, len(str(e11.get())), type(len(str(e11.get()))), all2, e22.get(), e44.get())
                            if all2 == None and e22.get() == e44.get() and result1 == True and result2 == True and len(str(e11.get())) == 11:
                                ghy = hashlib.md5()
                                ghy.update(e22.get().encode('utf-8'))
                                fkp = str(ghy.hexdigest())
                                # print(fkp)
                                sql3 = "insert into 账号 values('{}', {}, '{}', '{}', '{}', '{}')".format(e33.get(), e11.get(), fkp, tyr, fg, cmb3.get())
                                print(sql3)
                                # print(sql3)
                                cursor1.execute(sql3)
                                conn.commit()
                                messagebox.showinfo('小金豆', '注册成功！')
                                cursor1.close()
                                cursor.close()
                                conn.close()
                                mu.destroy()
                                root.destroy()

                            else:
                                messagebox.showwarning('小金豆', '错误！（1.该手机号已注册或您两次输入的密码不一致 2.您输入的密保有误！ 3.电子邮箱格式有误 4.手机号格式错误）')
                        except:
                            messagebox.showerror('小金豆', '请检查输入！(可能你输入的密保有误）')
                    except:
                        messagebox.showerror('小金豆', '服务器未开放！或服务器IP地址已变动，请及时联系管理员更换最新程序')
                Button(mu, text='确认', bg='green', fg='white', command=ner, width=10, height=1, relief=RIDGE).pack(side='bottom', pady=20)
                messagebox.showwarning('小金豆', '请记牢您的密保！如果忘记，请联系开发者解决。邮箱：xuebaxiaoniudun@outlook.com')

            Button(root, text='注册', bg='white', fg='black', command=signup, width=12, height=1, relief='groove').pack(side='bottom', pady=40)
        def forget_pass():
            ret = Toplevel()
            ret.title('找回密码')
            ret.config(background='white')
            ret.resizable(False, False)
            ret.geometry('300x250+0+0')

            Label(ret, text='您的手机号', bg='white', font=('黑体', 15), fg='black').pack(pady=3)
            art1 = Entry(ret, width=30, relief='solid')
            art1.pack()
            Label(ret, text='您的生日(YYYY-MM-DD)格式', bg='white', font=('黑体', 15), fg='black').pack(pady=3)
            art2 = Entry(ret, width=30, relief='solid')
            art2.pack()
            Label(ret, text='您的电子邮件', bg='white', font=('黑体', 15), fg='black').pack(pady=3)
            art3 = Entry(ret, width=30, relief='solid')
            art3.pack()

            def syt():
                try:
                    conn = pymysql.connect(host=ip1, port=host1, user='root', password='xxx', database='mindchat')
                    cursor = conn.cursor()
                    try:
                        sql1 = 'select * from 账号 where 手机号=' + str(art1.get())
                        cursor.execute(sql1)
                        global all1
                        all1 = cursor.fetchone()
                        # print(fkp1)
                        conn.close()
                        cursor.close()
                        if all1 == None:
                            messagebox.showerror('小金豆', '该账号不存在！')
                        else:
                            # passw = all1[2]
                            if str(all1[3]) == art2.get() and str(all1[5]) == art3.get():
                                messagebox.showinfo('小金豆', '验证成功！')
                                ret.destroy()
                                # f2.start()
                                retw = Toplevel()
                                retw.title('小金豆-找回密码')
                                retw.geometry('300x200+0+0')
                                retw.config(background='white')
                                retw.resizable(False, False)

                                Label(retw, text='您的新密码', bg='white', font=('黑体', 15), fg='black').pack(pady=3)
                                art12 = Entry(retw, width=30, show='*', relief='solid')
                                art12.pack()
                                Label(retw, text='请再次输入您的密码', bg='white', font=('黑体', 15), fg='black').pack(pady=3)
                                art22 = Entry(retw, width=30, show='*', relief='solid')
                                art22.pack()

                                def mrty():
                                    try:
                                        conn = pymysql.connect(host=ip1, port=host1, user='root', password='xxx', database='mindchat')
                                        cursor = conn.cursor()
                                        cursor1 = conn.cursor()
                                        try:
                                            '''sql2 = "select * from 账号 where 手机号=" + str(e11.get())
                                            cursor.execute(sql2)
                                            all2 = cursor.fetchone()'''
                                            if art12.get() == art22.get():
                                                ghy23 = hashlib.md5()
                                                ghy23.update(art22.get().encode('utf-8'))
                                                fkp2 = str(ghy23.hexdigest())
                                                sql3 = "update 账号 set 密码='{}' where 手机号={}".format(fkp2, all1[1])
                                                # print(sql3)
                                                cursor1.execute(sql3)
                                                conn.commit()
                                                messagebox.showinfo('小金豆', '修改成功！即将重启程序！')
                                                cursor1.close()
                                                cursor.close()
                                                conn.close()
                                                retw.destroy()
                                                os._exit(0)
                                            else:
                                                messagebox.showwarning('小金豆', '错误！（您两次输入的密码不一致！）')
                                        except:
                                            messagebox.showerror('小金豆', '请检查输入！')
                                    except:
                                        messagebox.showerror('小金豆', '服务器未开放！或服务器IP地址已变动，请及时联系管理员更换最新程序')

                                Button(retw, text='确认', bg='green', fg='white', width=6, command=mrty, relief=RIDGE).pack(side='bottom', pady=10)
                            else:
                                messagebox.showerror('小金豆', '密保错误！')
                    except:
                        messagebox.showerror('小金豆', '未知错误')
                except:
                    messagebox.showerror('小金豆', '服务器未开放！或服务器IP地址已变动，请及时联系管理员更换最新程序')

            Button(ret, text='下一步', bg='green', fg='white', command=syt, width=6, height=1, relief=RIDGE).pack(side='bottom', pady=3)

        Label(win, text='Written by Jindou  2023—2024', bg='white', fg='black').pack(side='bottom')
        Button(win, relief=FLAT, text='没有账号？点击注册', bg='white', fg='blue', command=sign_up, width=10, height=1).place(relx=0.621, rely=0.872, height=28, width=119)
        Button(win, text='登录', bg='white', fg='black', command=sign_in, width=10, height=1, relief=GROOVE).place(relx=0.395, rely=0.596, height=28, width=89)
        Button(win, relief=FLAT, text='找回密码', bg='white', fg='blue', command=forget_pass, width=10, height=1).place(relx=0.706, rely=0.823, height=28, width=59)

        win.mainloop()
    except:
        pass
def main2():
    # 聊天界面
    global zh
    zh = Tk()
    zh.title('收发消息')
    zh.geometry('800x530+0+0')
    zh.config(background='white')
    zh.resizable(False, False)
    zh.iconbitmap(r'C:/语聊文件夹/logo.ico')

    def no_closing():
        os._exit(0)

    zh.protocol('WM_DELETE_WINDOW', no_closing)

    ast = '{}的信箱'.format(all1[0])
    Label(zh, bg='white', text=ast, font=('微软雅黑', 13)).pack(pady=5)


    Label(zh, text='收件人手机号', font=('微软雅黑', 12), bg='white').place(x=150, y=38)
    e4 = Entry(zh, width=45, relief='solid')
    e4.place(x=265, y=42)
    e3 = Text(zh, width=50, height=25, relief='solid')
    scrollbary = Scrollbar(zh, orient=VERTICAL)  # 滚轮初始

    scrollbary.pack(fill=Y, side=RIGHT)

    e3.place(x=400, y=120)
    # we = '{}({})发送的信息内容：\n\n'.format(all1[0], all1[1])
    # e3.insert(INSERT, we)

    scrollbary.config(command=e3.yview)

    e3.config(yscrollcommand=scrollbary.set)
    global e5
    e5 = Text(zh, width=50, height=25, relief='solid')
    scrollbary1 = Scrollbar(zh, orient=VERTICAL)  # 滚轮初始
    scrollbary1.pack(fill=Y, side=LEFT)

    e5.place(x=30, y=120)

    scrollbary1.config(command=e3.yview)

    e5.config(yscrollcommand=scrollbary1.set)
    e5.configure(state='disabled')
    Label(zh, bg='white', text='收件箱：', font=('微软雅黑', 13)).place(x=30, y=80)
    Label(zh, bg='white', text='发件箱：', font=('微软雅黑', 13)).place(x=400, y=80)
    # Beta 3.0 菜单栏
    zyb = Menu(zh)
    filemenu = Menu(zyb, tearoff=False)

    def open_file():
        zsy = Toplevel()
        # 信息修改
        zsy.title('基本信息修改')
        zsy.geometry('400x430')
        zsy.resizable(False, False)
        zsy.config(background='white')

        Label(zsy, text='基本信息修改', bg='white', font=('楷体', 32), fg='black').pack()
        Label(zsy, text='手机号', bg='white', font=('微软雅黑', 15), fg='black').place(x=20, y=120)
        Label(zsy, text='密码', bg='white', font=('微软雅黑', 15), fg='black').place(x=30, y=180)
        Label(zsy, text='昵称', bg='white', font=('微软雅黑', 15), fg='black').place(x=30, y=240)
        Label(zsy, text='确认密码', bg='white', font=('微软雅黑', 14), fg='black').place(x=10, y=300)
        frt = all1[1]
        frt1 = all1[0]
        e11 = Entry(zsy, width=35, state=NORMAL, relief='solid')
        e22 = Entry(zsy, width=35, show='*', relief='solid')
        e33 = Entry(zsy, width=35,  relief='solid')
        e33.insert(0, frt1)
        e11.insert(0, frt)
        e11.configure(state=DISABLED)
        e44 = Entry(zsy, width=35, show='*', relief='solid')
        e11.place(x=100, y=126)
        e22.place(x=100, y=186)
        e33.place(x=100, y=246)
        e44.place(x=100, y=306)

        def check1():
            try:
                conn = pymysql.connect(host=ip1, port=host1, user='root', password='xxx',
                                       database='mindchat')
                cursor = conn.cursor()
                cursor1 = conn.cursor()
                try:
                    '''sql2 = "select * from 账号 where 手机号=" + str(e11.get())
                    cursor.execute(sql2)
                    all2 = cursor.fetchone()'''
                    if e22.get() == e44.get():
                        ghy2 = hashlib.md5()
                        ghy2.update(e22.get().encode('utf-8'))
                        fkp2 = str(ghy2.hexdigest())
                        sql3 = "update 账号 set 手机号={}, 密码='{}', 昵称='{}' where 手机号={}".format(e11.get(), fkp2, e33.get(), all1[1])
                        # print(sql3)
                        cursor1.execute(sql3)
                        conn.commit()
                        messagebox.showinfo('小金豆', '修改成功！即将重启程序！')
                        cursor1.close()
                        cursor.close()
                        conn.close()
                        zsy.destroy()
                        os._exit(0)
                    else:
                        messagebox.showwarning('小金豆', '错误！（您两次输入的密码不一致！）')
                except:
                    messagebox.showerror('小金豆', '请检查输入！')
            except:
                messagebox.showerror('小金豆', '服务器未开放！或服务器IP地址已变动，请及时联系管理员更换最新程序')

        Button(zsy, text='确认', bg='green', fg='white', command=check1, width=10, height=1, relief=RIDGE).pack(side='bottom', pady=20)
        messagebox.showwarning('小金豆', '暂时不支持手机号设置，如有需要，请在周末9:00——22:00发送电子邮件给开发者以解决。电子邮件：xuebaxiaoniudun@outlook.com')
        zsy.attributes('-topmost', 'true')

    def close_file():
        pass
    def lyf():
        pass
    def safe():
        pass
    def fuck():
        os._exit(0)
    def fku():
        fr = messagebox.askokcancel('确认操作', '您确认注销账号吗') #返回值true/false
        if fr == True:
            try:
                art = passwordbox('请输入密码以继续操作', '小金豆')
                ghy3 = hashlib.md5()
                ghy3.update(art.encode('utf-8'))
                fkp3 = str(ghy3.hexdigest())
                if fkp3 == str(all1[2]):
                    try:
                        # print(all1[1])
                        conn = pymysql.connect(host=ip1, port=host1, user='root', password='xxx', database='mindchat')
                        cursor = conn.cursor()
                        sql9 = 'delete from 账号 where 手机号={}'.format(all1[1])
                        cursor.execute(sql9)
                        conn.commit()
                        messagebox.showinfo('小金豆', '已注销，即将重启程序！')
                        # messagebox.showinfo('小金豆', '已注销，即将重启程序！')
                        cursor.close()
                        conn.close()
                        os._exit(0)
                    except:
                        messagebox.showerror('小金豆', '服务器未开放！或服务器IP地址已变动，请及时联系管理员更换最新程序')
                else:
                    messagebox.showerror('小金豆', '密码错误！')
            except:
                messagebox.showerror('小金豆', '密码错误！')

        else:
            pass

    filemenu.add_command(label='账号设置', command=open_file)
    filemenu.add_command(label='主题', command=close_file)
    filemenu.add_command(label='注销账号', command=fku)
    zyb.add_cascade(label='账号', menu=filemenu)
    zyb.add_command(label='接发', command=lyf)
    zyb.add_command(label='安全', command=safe)
    zyb.add_command(label='退出', command=fuck)

    zh.config(menu=zyb)


    f3.start()

    def send():
        try:
            conn = pymysql.connect(host=ip1, port=host1, user='root', password='xxx', database='mindchat')
            cursor = conn.cursor()
            sql5 = 'select * from 账号 where 手机号={}'.format(e4.get())
            cursor.execute(sql5)
            all2 = cursor.fetchone()
            if all2 == None:
                messagebox.showerror('小金豆', '没有此收件人，请检查！')
            else:
                try:
                    sql4 = "insert into 内容 values('{}', '{}', {}, {}, '{}', {})".format(e3.get('1.0', 'end'), all1[0], all1[1], e4.get(), time.ctime(), 0)
                    cursor.execute(sql4)
                    conn.commit()
                    cursor.close()
                    conn.close()
                    messagebox.showinfo('小金豆', '发送成功！')
                except:
                    messagebox.showerror('小金豆', '发送失败！请检查信息！')
        except:
            messagebox.showerror('小金豆', '未知错误！请联系管理员解决！或服务器IP地址已变动，请及时联系管理员更换最新程序')

    def recieve():
        try:
            e5.configure(state='normal')
            e5.delete('1.0', END)
            # we = '{}的收信箱：\n\n'.format(all1[0])
            # e5.insert(INSERT, we)
            conn = pymysql.connect(host=ip1, port=host1, user='root', password='xxx', database='mindchat')
            cursor = conn.cursor()
            sql6 = 'select * from 内容 where 收件人账号={}'.format(all1[1])
            cursor.execute(sql6)
            all8 = cursor.fetchall()
            for t in all8:
                e5.insert('end', '{}\n{}({})发送的内容\n{}\n\n\n'.format(t[4], t[1], t[2], t[0]))
            sql11 = 'update 内容 set 已读未读=1 where 收件人账号={}'.format(all1[1])
            cursor.execute(sql11)
            conn.commit()
            e5.configure(state='disabled')
            conn.close()
            cursor.close()

        except:
            messagebox.showerror('小金豆', '未知错误！请检查数据或联系管理员！')
    def clear():
        try:
            conn = pymysql.connect(host=ip1, port=host1, user='root', password='xxx', database='mindchat')
            cursor = conn.cursor()
            sql9 = 'delete from 内容 where 收件人账号 = {}'.format(all1[1])
            cursor.execute(sql9)
            conn.commit()
            messagebox.showinfo('小金豆', '已清空您的聊天数据！')
            cursor.close()
            conn.close()
        except:
            messagebox.showerror('小金豆', '服务器未开放！或服务器IP地址已变动，请及时联系管理员更换最新程序')

    recieve()

    Button(zh, text='一键清空聊天记录', bg='white', fg='blue', command=clear, relief=FLAT).place(x=0, y=0)
    Button(zh, text='发送', bg='green', fg='white', command=send, width=20, relief=RIDGE).place(x=400, y=460)
    Button(zh, text='刷新', bg='green', fg='white', command=recieve, width=20, relief=RIDGE).place(x=235, y=460)

    zh.mainloop()

def main3():
    try:
        while True:
            e5.configure(state='normal')
            # e5.delete('1.0', END)
            conn = pymysql.connect(host=ip1, port=host1, user='root', password='xxx', database='mindchat')
            cursor = conn.cursor()
            sql6 = 'select * from 内容 where 收件人账号={} and 已读未读=0'.format(all1[1])
            cursor.execute(sql6)
            all2 = cursor.fetchall()
            # print(all2)
            for t in all2:
                e5.insert('end', '{}\n{}({})发送的内容\n{}\n\n\n'.format(t[4], t[1], t[2], t[0]))
                file = r'C:\语聊文件夹\叮.mp3'
                pygame.mixer.init()
                pygame.mixer.music.load(file)
                pygame.mixer.music.play()
                time.sleep(1.5)
                pygame.mixer.music.stop()
            sql11 = 'update 内容 set 已读未读=1 where 收件人账号={}'.format(all1[1])
            cursor.execute(sql11)
            conn.commit()
            e5.configure(state='disabled')
            time.sleep(5)
            conn.close()
            cursor.close()
            zh.update()



    except:
        pass

if __name__ == '__main__':
    f1 = threading.Thread(target=main1)
    f2 = threading.Thread(target=main2)
    f3 = threading.Thread(target=main3)


    f1.start()
