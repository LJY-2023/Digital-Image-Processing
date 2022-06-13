import matplotlib.pyplot as plt
import numpy as np
import cv2 
import tkinter as tk
import time
'''
        实验三--图像模板操作与边缘检测实验
        一、实验任务
            熟悉模板操作，编制一个通用的边缘提取函数。通过输入不同的参数，
        能够实现Sobel算子、Prewitt算子、Roberts算子和Canny边缘检测。
        二、实验目的
            1、学习图像模板操作原理，与实现方法；
            2、能够利用模板操作实现各种图像边缘检测；
            3、掌握各种边缘检测算法的特点与作用；
'''
class Class_Experiment_3:
    def sys_loop_1(file_name):
        def exit():
            from Register import Class_Select
            time_end = time.time()
            time_c= time_end - time_start   #运行所花时间
            #print('time cost', time_c, 's')
            time_cost=int(time_c)
            tk.messagebox.showinfo(title='成绩结算',
                                       message='实验结束'+'\n')

            window.destroy()
            Class_Select.select()
            return


        #OpenCV核心代码

        def start():

            #读取彩色图片
            source=cv2.imread(file_name)
            #转换成灰度图
            img_gray = cv2.cvtColor(source,cv2.COLOR_RGB2GRAY)


            #输入算子参数
            N1 =int(Num1.get())
            N2 =int(Num2.get())
            N3 =int(Num3.get())
            N4 =int(Num4.get())
            N5 =int(Num5.get())
            N6 =int(Num6.get())
            N7 =int(Num7.get())
            N8 =int(Num8.get())
            N9 =int(Num9.get())
            #生成空矩阵
            gaussian = np.zeros([3, 3])
            #生成算子
            gaussian[0,0] =  N1
            gaussian[0,1] =  N2
            gaussian[0,2] =  N3
            gaussian[1,0] =  N4
            gaussian[1,1] =  N5
            gaussian[1,2] =  N6
            gaussian[2,0] =  N7
            gaussian[2,1] =  N8
            gaussian[2,2] =  N9


            #读取图像的行数与列数
            W,H = img_gray.shape

            #生成新图像的矩阵
            new_gray = np.zeros([W-2, H-2])

            # 与高斯矩阵卷积实现滤波 
            for i in range(0+1,W-1-1):
                for j in range(0+1,H-1-1):
                    img_M=img_gray[i-1:(i+1)+1,j-1:(j+1)+1]
                    new_gray[i-1,j-1] = np.sum(img_M*gaussian)



            #画图部分
            fig=plt.figure(1)  
            b=fig.add_subplot(121)
            b.imshow(img_gray,cmap=plt.cm.gray)  
            fig=plt.figure(1)  
            plt.title("Original")
            plt.xticks([]), plt.yticks([])

            b=fig.add_subplot(122)  
            b.imshow(new_gray,cmap=plt.cm.gray) 
            fig=plt.figure(1)  
            plt.title("Edge")
            plt.xticks([]), plt.yticks([])



        


        time_start = time.time()
        window = tk.Tk()
        window.title('实验三')
        window.geometry('700x300')
        window.minsize(700, 300)   
        window.maxsize(700, 300)  
        window.resizable(0,0) 
        Num1=tk.Entry(window,show=None,width=3)
        Num1.place(x=90, y=80)
        Num2=tk.Entry(window,show=None,width=3)
        Num2.place(x=90, y=110)
        Num3=tk.Entry(window,show=None,width=3)
        Num3.place(x=90, y=140)

        Num4=tk.Entry(window,show=None,width=3)
        Num4.place(x=120, y=80)
        Num5=tk.Entry(window,show=None,width=3)
        Num5.place(x=120, y=110)
        Num6=tk.Entry(window,show=None,width=3)
        Num6.place(x=120, y=140)

        Num7=tk.Entry(window,show=None,width=3)
        Num7.place(x=150, y=80)
        Num8=tk.Entry(window,show=None,width=3)
        Num8.place(x=150, y=110)
        Num9=tk.Entry(window,show=None,width=3)
        Num9.place(x=150, y=140)

        b1=tk.Button(window,text='start',width=15,height=2,command=start)
        b1.place(x=120, y=200)


        bt_logquit = tk.Button(window, text='退出', command=exit)
        bt_logquit.place(x=10, y=10)



        plt.ion()
        plt.show()
        tk.Label(window, text=
    '        边缘，是指图像中像素灰度由阶跃变化或屋顶状变化的那些像素的集合，是图像的基本特征。'
    '边缘有幅度和方向两个基本特征，沿边缘走向像素灰度值变化比较平缓，垂直于边缘走向像素灰度值变'
    '化比较明显。'+'\n'+
    '        边缘检测是图像预处理中的关键。边缘是指其周围像素灰度发生阶跃变化或屋顶状变化的那些像素'
    '的集合，图像的大部分信息都存在于图像的边缘中，主要表现为图像局部特征的不连续性，是图像灰度变化'
    '比较剧烈的地方。在一幅图像中，边缘有方向和幅度两个特性。'
            ,wraplength=310,justify='left').place(x=300, y=10)
        window.mainloop()
        return
    pass
