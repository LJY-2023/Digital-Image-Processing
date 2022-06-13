import matplotlib.pyplot as plt
import numpy as np
import cv2 
import tkinter as tk
import time
'''
        实验一--图像增强实验
        一、实验任务
            给定一幅图像，输出其直方图。通过对话框给定一个线性变换函数的参数，
        实现图像的灰度拉伸；实现图像直方图均衡化；显示变换前后图像直方图。
        二、实验目的
            1、理解图像对比度与图像直方图之间的关系；
            2、掌握线性变换实现图像对比度增强的方法；
            3、掌握直方图均衡化方法，理解直方图均衡化的作用。
'''
class Class_Experiment_1():
    def sys_loop_1(file_name):
        def exit():
            from Register import Class_Select
            time_end = time.time()
            time_c= time_end - time_start  
            time_cost=int(time_c)
            tk.messagebox.showinfo(title='成绩结算',
                                       message='实验结束'+'\n')
            window.destroy()
            Class_Select.select()
            return

        def is_number(s):
            try: 
                float(s)
                return True
            except ValueError: 
                pass 
            try:
                import unicodedata 
                unicodedata.numeric(s) 
                return True
            except (TypeError, ValueError):
                pass
            return False




        #OpenCV核心代码

        def insert_point():

            #判断输入的参数是否为整数、是否相等
            if is_number(Num1.get()) == False or is_number(Num1.get()) == False:
                tk.messagebox.showerror(message='请输入数值')
                return
            else:
                A =int(Num1.get())
                B =int(Num2.get())
            if A == B :
                tk.messagebox.showerror(message='两个参数值不能相等')
                return


            #读取彩色图片
            source=cv2.imread(file_name)
            #转换成灰度图
            img_gray = cv2.cvtColor(source,cv2.COLOR_RGB2GRAY)
            #对灰度图进行线性变换
            #公式：g(x,y) = 255 / (B - A) * [f(x,y) - A]
            #A = min[f(x,y)],最小灰度级；B = max[f(x,y)],最大灰度级
            img_gray_plus = np.uint8(255 / (B - A) * (img_gray - A) )
            #调用calcHist()绘制直方图
            #图像，通道[0]-灰度图，掩膜-无，灰度级，像素范围
            hist1 = cv2.calcHist([img_gray],[0],None,[256],[0,255])
            hist2 = cv2.calcHist([img_gray_plus],[0],None,[256],[0,255])
            #画图部分
            #图1
            fig=plt.figure(1)   
            plt.axis('off')
            b=fig.add_subplot(221) 
            b.imshow(img_gray,cmap=plt.cm.gray)  
            fig=plt.figure(1)  
            plt.title("Original")
            plt.xticks([]), plt.yticks([])
            #图2
            b=fig.add_subplot(222)  
            b.imshow(img_gray_plus,cmap=plt.cm.gray)
            fig=plt.figure(1) 
            plt.title("Enhance")
            plt.xticks([]), plt.yticks([])
            #图3
            b=fig.add_subplot(223) 
            plt.plot(hist1)
            fig=plt.figure(1) 
            plt.title("Histogram")
            #图4
            b=fig.add_subplot(224)  
            plt.plot(hist2)
            fig=plt.figure(1) 
            plt.title("Histogram")

        time_start = time.time() 
        window = tk.Tk()
        window.title('实验一')
        window.geometry('700x300')
        window.minsize(700, 300)   
        window.maxsize(700, 300) 
        window.resizable(0,0) 

        tk.Label(window, text='参数A:').place(x=20, y=80)
        tk.Label(window, text='参数B:').place(x=20, y=120)

        x_translation = tk.StringVar()
        Num1 = tk.Entry(window, textvariable=x_translation)
        Num1.place(x=80, y=80)

        y_translation = tk.StringVar()
        Num2 = tk.Entry(window, textvariable=y_translation)
        Num2.place(x=80, y=120)

        b1 = tk.Button(window, text='输入参数', command=insert_point)
        b1.place(x=150, y=200)

        bt_logquit = tk.Button(window, text='退出', command=exit)
        bt_logquit.place(x=10, y=10)


       
        plt.ion()
        plt.show()
        tk.Label(window, text=
            '        通过调整折线拐点的位置及控制分段直线的斜率，可对任一灰度区间'
            '进行扩展或压缩。这种变换适用于在黑色或白色附近有噪声干扰的情况。'
            '例如照片中的划痕，由于变换后0~a以及b~Fmax之间的灰度受到压缩，'
            '因而使噪声干扰得到减弱。'+'\n'+
            '        针对不同的变化效果对原图的影响的不同，这次实验主要使用的是分段'
            '线性变换的方法，将原图的灰度范围分成[0,a][a,b][b,255]三个部分，在'
            '通过c,d变量'
            '将图像拉伸或者压缩，参数a,b给出需要转换的灰度范围，c,d决定线性'
            '变换的斜率。  '
            ,wraplength=300,justify='left').place(x=300, y=10)
        window.mainloop()
        window.mainloop()

    pass

