import tkinter as tk
import tkinter.messagebox
from tkinter import filedialog
import pickle
import matplotlib.pyplot as plt
import numpy as np
import cv2 
import sys 

from Experiment_1 import Class_Experiment_1
from Experiment_2 import Class_Experiment_2
from Experiment_3 import Class_Experiment_3
from Experiment_4 import Class_Experiment_4
from Experiment_5 import Class_Experiment_5
'''
    这部分是登陆界面和文件选择界面的实现部分
'''
class Class_Select():



    def select():
        def exit():
            from Register import Class_Select
            tk.messagebox.showinfo(title='退出登录',
                                       message='确认要退出登录吗'+'\n')
            window.destroy()
            Class_Main.main_cc()  
            return
        def ex1():
            tk.messagebox.showinfo(title='实验一--图像增强实验',
                                       message='一、实验任务'+'\n'
                                            +'\t'+'给定一幅图像，输出其直方图。通过对话框给定一个线性变换函数的参数，'
                                            '实现图像的灰度拉伸；实现图像直方图均衡化；显示变换前后图像直方图。'+'\n'
                                            '二、实验目的'+'\n'
                                            +'\t'+'1、理解图像对比度与图像直方图之间的关系；'+'\n'
                                            +'\t'+'2、掌握线性变换实现图像对比度增强的方法；'+'\n'
                                            +'\t'+'3、掌握直方图均衡化方法，理解直方图均衡化的作用。' )
            window.destroy()
            Class_Experiment_1.sys_loop_1(str(V.get().replace('/', '\\')))
            return
        def ex2():
            tk.messagebox.showinfo(title='实验二--基于FFT的图像平移与旋转实验',
                                       message='一、实验任务'+'\n'
                                            +'\t'+'编制一个图像几何变换的函数，函数输入图像、水平平移值、垂直平移值，'
                                            '旋转角度四个参数，输出为输入图像经平移以后的结果。显示源图像和几何变换'
                                            '的结果。要求利用FFT的时移性质，实现基于FFT的图像的平移算法。'+'\n'
                                            '二、实验目的'+'\n'
                                            +'\t'+'1、学习图像的FFT性质；'+'\n'
                                            +'\t'+'2、理解图像平移旋转等几何变换的工作原理。'+'\n'
                                            +'\t'+'3、熟悉图像几何变换的应用。' )
            window.destroy()
            Class_Experiment_2.sys_loop_1(str(V.get().replace('/', '\\')))
            return 
        def ex3():
            tk.messagebox.showinfo(title='实验三--图像模板操作与边缘检测实验',
                                       message='一、实验任务'+'\n'
                                            +'\t'+'熟悉模板操作，编制一个通用的边缘提取函数。通过输入不同的参数，'
                                            '能够实现Sobel算子、Prewitt算子、Roberts算子和Canny边缘检测。'+'\n'
                                            '二、实验目的'+'\n'
                                            +'\t'+'1、学习图像模板操作原理，与实现方法；'+'\n'
                                            +'\t'+'2、能够利用模板操作实现各种图像边缘检测；'+'\n'
                                            +'\t'+'3、掌握各种边缘检测算法的特点与作用；' )
            window.destroy()
            Class_Experiment_3.sys_loop_1(str(V.get().replace('/', '\\')))
            return 
        def ex4():
            tk.messagebox.showinfo(title='实验四--图像低通与高通滤波实验',
                                       message='一、实验任务'+'\n'
                                            +'\t'+'运用Matlab 实现图像的FFT变换，分析变换系数的特点，并显示'
                                            '变换系数；利用图像低通滤波器和高通滤波器的实现对图像的滤波的方法，'
                                            '能够分析不同滤波的滤波效果。'+'\n'
                                            '二、实验目的'+'\n'
                                            +'\t'+'1、学习图像傅里叶变换的特点与应用；'+'\n'
                                            +'\t'+'2、掌握FFT实现图像的高通与低通滤波的方法；'+'\n'
                                            +'\t'+'3、熟悉图像不同滤波图像的效果。' )
            window.destroy()
            Class_Experiment_4.sys_loop_1(str(V.get().replace('/', '\\')))
            return 
        def ex5():
            tk.messagebox.showinfo(title='实验五--图像阈值分割与形态学运算实验',
                                       message='一、实验任务'+'\n'
                                            +'\t'+'显示图像的直方图，根据图像的直方图中图像的灰度分布，'
                                            '选择最佳阈值，实现图像的二值化；并显示腐蚀、膨胀、开运算、'
                                            '闭运算对二值图像的操作的结果，总结四种形态学运算的特点。'+'\n'
                                            '二、实验目的'+'\n'
                                            +'\t'+'1、学习利用图像直方图选择阈值的方法；'+'\n'
                                            +'\t'+'2、掌握图像阈值分割方法；'+'\n'
                                            +'\t'+'3、掌握基本的图像形态学算法的特点。' )
            window.destroy()
            #Image_sys()       #打开主界面
            Class_Experiment_5.sys_loop_1(str(V.get().replace('/', '\\')))
            return 

        def open_file():
            filename = filedialog.askopenfilename(title='打开jpg文件', filetypes=[('jpg', '*.jpg')])
            enter_data.insert('insert', filename)
           
        fig=plt.figure(1)   #新建2*2绘图窗口
        plt.close(1)

        window = tk.Tk()
        window.title('欢迎进入图像处理系统')
        window.geometry('900x400')
        window.minsize(900, 500)   # 最小尺寸
        window.maxsize(900, 500)   # 最大尺寸

        bt_ex1 = tk.Button(window, text='——————图像增强实验——————', command=ex1)
        bt_ex1.place(x=100, y=50)
        bt_ex2 = tk.Button(window, text='——基于FFT的图像平移与旋转实验———', command=ex2)
        bt_ex2.place(x=100, y=150)
        bt_ex3 = tk.Button(window, text='——图像模板操作与边缘检测实验———', command=ex3)
        bt_ex3.place(x=100, y=250)
        bt_ex4 = tk.Button(window, text='———图像低通与高通滤波实验————', command=ex4)
        bt_ex4.place(x=100, y=350)
        bt_ex5 = tk.Button(window, text='——图像阈值分割与形态学运算实验——', command=ex5)
        bt_ex5.place(x=100, y=450)
        bt_file = tk.Button(window, text='—导入文件—', command=open_file)
        bt_file.place(x=450, y=450)



        V = tk.StringVar()
        enter_data = tk.Entry(window, width=15, font=("宋体", 20, 'bold'),textvariable=V)
        enter_data.place(x=600, y=450)


        tk.Label(window, text=
            '\t''数字图像处理是电子信息工程专业的重要专业课，本实验室课程教材的组成部分。'
            '图像处理理论与技术已渗透到宇宙探测、科研、国防、医学、工农业、日常生活的各个'
            '方面。学生通过数字图像处理的学习，能学习掌握图像处理的基本理论、概念、方法和'
            '技术，了解本领域最新的成果和发展动态；了解交叉学科的特点，培养严谨的治学态度'
            '，启迪创新思路和意识。'+'\n'+
            '本课程配备的实验紧扣教学内容，是对课堂内容的巩固和加强，除了进一步掌握基本'
            '原理外，还锻炼了学生的动手能力和实践能力，分析问题和解决问题的能力，特别是'
            '对高级语言的学习和使用将进一步加深和拓展。通过本课程和相关的实验，是学生'
            '打下一个比较坚实的基础，为以后从事本领域或相关领域工作、深造、研究作准备。'
                ,wraplength=300,justify='left').place(x=450, y=50)

        bt_logquit = tk.Button(window, text='退出', command=exit)
        bt_logquit.place(x=10, y=10)
        window.mainloop()
    pass


class Class_Main():

    def main_cc():

        def exit():
            from Register import Class_Select
            tk.messagebox.showinfo(title='退出平台',
                                    message='确认要退出仿真平台吗'+'\n')

            window.destroy()
            sys.exit(0)
            return
        # 登录函数
        def usr_log_in():
            # 输入框获取用户名密码
            usr_name = var_usr_name.get()
            usr_pwd = var_usr_pwd.get()
            # 从本地字典获取用户信息，如果没有则新建本地数据库
            try:
                with open('usr_info.pickle', 'rb') as usr_file:
                    usrs_info = pickle.load(usr_file)
            except FileNotFoundError:
                with open('usr_info.pickle', 'wb') as usr_file:
                    usrs_info = {'admin': 'admin'}
                    pickle.dump(usrs_info, usr_file)
            # 判断用户名和密码是否匹配
            if usr_name in usrs_info:
                if usr_pwd == usrs_info[usr_name]:
                    tk.messagebox.showinfo(title='welcome',
                                            message='欢迎您：' + usr_name)
                    window.destroy()
                    #Image_sys()       #打开主界面
                    Class_Select.select()

                else:
                    tk.messagebox.showerror(message='密码错误')
            # 用户名密码不能为空
            elif usr_name == '' or usr_pwd == '':
                tk.messagebox.showerror(message='用户名或密码为空')
            # 不在数据库中弹出是否注册的框
            else:
                is_signup = tk.messagebox.askyesno('欢迎', '您还没有注册，是否现在注册')
                if is_signup:
                    usr_sign_up() #打开注册界面
            return


        # 注册函数
        def usr_sign_up():
            # 确认注册时的相应函数
            def signtowcg():
                # 获取输入框内的内容
                nn = new_name.get()
                np = new_pwd.get()
                npf = new_pwd_confirm.get()

                # 本地加载已有用户信息,如果没有则已有用户信息为空
                try:
                    with open('usr_info.pickle', 'rb') as usr_file:
                        exist_usr_info = pickle.load(usr_file)
                except FileNotFoundError:
                    exist_usr_info = {}

                    # 检查用户名存在、密码为空、密码前后不一致
                if nn in exist_usr_info:
                    tk.messagebox.showerror('错误', '用户名已存在')
                elif np == '' or nn == '':
                    tk.messagebox.showerror('错误', '用户名或密码为空')
                elif np != npf:
                    tk.messagebox.showerror('错误', '密码前后不一致')
                # 注册信息没有问题则将用户名密码写入数据库
                else:
                    exist_usr_info[nn] = np
                    with open('usr_info.pickle', 'wb') as usr_file:
                        pickle.dump(exist_usr_info, usr_file)
                    tk.messagebox.showinfo('欢迎', '注册成功')
                    # 注册成功关闭注册框
                    window_sign_up.destroy()
                return

            # 新建注册界面
            window_sign_up = tk.Toplevel(window)
            window_sign_up.geometry('350x200')
            window_sign_up.title('注册')
            # 用户名变量及标签、输入框
            new_name = tk.StringVar()
            tk.Label(window_sign_up, text='用户名：').place(x=10, y=10)
            tk.Entry(window_sign_up, textvariable=new_name).place(x=150, y=10)
            # 密码变量及标签、输入框
            new_pwd = tk.StringVar()
            tk.Label(window_sign_up, text='请输入密码：').place(x=10, y=50)
            tk.Entry(window_sign_up, textvariable=new_pwd, show='*').place(x=150, y=50)
            # 重复密码变量及标签、输入框
            new_pwd_confirm = tk.StringVar()
            tk.Label(window_sign_up, text='请再次输入密码：').place(x=10, y=90)
            tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*').place(x=150, y=90)
            # 确认注册按钮及位置
            bt_confirm_sign_up = tk.Button(window_sign_up, text='确认注册',
                                            command=signtowcg)
            bt_confirm_sign_up.place(x=150, y=130)


        # 窗口
        window = tk.Tk()
        window.title('欢迎进入图像处理系统')
        window.geometry('670x500')
        window.minsize(670, 500)   # 最小尺寸
        window.maxsize(670, 500)   # 最大尺寸
        # 画布放置图片
        canvas=tk.Canvas(window,height=400,width=800)
        imagefile=tk.PhotoImage(file='./pic/DSP.png')
        image=canvas.create_image(0,0,anchor='nw',image=imagefile)
        canvas.pack(side='top')#在这里插入代码片
        # 标签 用户名密码
        tk.Label(window, text='用户名:').place(x=200, y=320)
        tk.Label(window, text='密码:').place(x=200, y=360)
        # 用户名输入框
        var_usr_name = tk.StringVar()
        entry_usr_name = tk.Entry(window, textvariable=var_usr_name)
        entry_usr_name.place(x=260, y=320)
        # 密码输入框
        var_usr_pwd = tk.StringVar()
        entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, show='*')
        entry_usr_pwd.place(x=260, y=360)
        # 登录 注册按钮
        bt_login = tk.Button(window, text='登录', command=usr_log_in)
        bt_login.place(x=230, y=400)
        bt_logup = tk.Button(window, text='注册', command=usr_sign_up)
        bt_logup.place(x=300, y=400)
        bt_logquit = tk.Button(window, text='退出', command=exit)
        bt_logquit.place(x=370, y=400)

        fig=plt.figure(1)   #新建2*2绘图窗口
        plt.close(1)
        window.mainloop()
    pass

