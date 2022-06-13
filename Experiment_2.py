import tkinter as tk
import cv2 
import numpy as np
from matplotlib import pyplot as plt
import time
'''
        实验二--基于FFT的图像平移与旋转实验
        一、实验任务
            编制一个图像几何变换的函数，函数输入图像、水平平移值、垂直平移值，
        旋转角度四个参数，输出为输入图像经平移以后的结果。显示源图像和几何变换
        的结果。要求利用FFT的时移性质，实现基于FFT的图像的平移算法。
        二、实验目的
            1、学习图像的FFT性质；
            2、理解图像平移旋转等几何变换的工作原理;
            3、熟悉图像几何变换的应用。
'''
class Class_Experiment_2:
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

        #图像平移核心代码
        def select_translation():

            #输入需要移动的距离
            x_move =int(x_name.get())
            y_move =int(y_name.get())

            #读取彩色图片的通道0，得到灰度图像
            img = cv2.imread(file_name, 0)

            #傅里叶变换
            f = np.fft.fft2(img)
            #移动零频率分量到数组的中心
            fshift = np.fft.fftshift(f)

            #信号时域的平移等于频域乘以exp(-j*2pi/N*n)
            N,M=fshift.shape
            for i in range(M):
                for j in range(N):
                    fshift[i][j]= np.exp(-1j*2*np.pi*(i*y_move/M+j*x_move/N))*fshift[i][j]
            #取实部的功率谱
            res = np.log(np.abs(fshift))


            #移动零频率分量到原来的位置
            ishift = np.fft.ifftshift(fshift)
            #傅里叶逆变换
            iimg = np.fft.ifft2(ishift)
            #取实部
            iimg = np.abs(iimg)
 
            #画图部分
            plt.subplot(131), plt.imshow(img, 'gray'), plt.title('Original Image')
            plt.axis('off')
            plt.subplot(132), plt.imshow(res, 'gray'), plt.title('Fourier Image')
            plt.axis('off')
            plt.subplot(133), plt.imshow(iimg, 'gray'), plt.title('Inverse Fourier Image')
            plt.axis('off')
            return




        #图像旋转核心代码
        def select_rotation():

            #输入需要旋转的角度
            angle =int(r_name.get())

            #读取彩色图片的通道0，得到灰度图像
            img = cv2.imread(file_name, 0)

            #傅里叶变换
            f = np.fft.fft2(img)
            #移动零频率分量到数组的中心
            fshift = np.fft.fftshift(f)

            #读取图像的行数与列数
            (h,w)=fshift.shape[:2]
            center=(w//2,h//2)

            #调用getRotationMatrix2D()生成两行三列变换矩阵M
            #OpenCV中默认原点为图片左上角，需要将其移动到中心
            #(旋转的中心点，表示旋转的角度，图像缩放因子)
            M=cv2.getRotationMatrix2D(center,angle,1)

            #使用旋转变换矩阵M，调用warpAffine()实现线性变换
            #输入图像,变换矩阵,输出图像的大小
            fshift_real=cv2.warpAffine(np.real(fshift),M,(w,h))
            fshift_imag=cv2.warpAffine(np.imag(fshift),M,(w,h))
            #fshift_abs=cv2.warpAffine(np.abs(fshift),M,(w,h))
            #fshift_angle=cv2.warpAffine(np.angle(fshift),M,(w,h))
 
            #实部与虚部合并
            fshift=fshift_real+fshift_imag*1j

            #取实部的功率谱
            res = np.log(np.abs(fshift))

            #移动零频率分量到原来的位置
            ishift = np.fft.ifftshift(fshift)
            #傅里叶逆变换
            iimg = np.fft.ifft2(ishift)
            #取实部
            iimg = np.abs(iimg)
 
            #画图部分
            plt.subplot(131), plt.imshow(img, 'gray'), plt.title('Original Image')
            plt.axis('off')
            plt.subplot(132), plt.imshow(res, 'gray'), plt.title('Fourier Image')
            plt.axis('off')
            plt.subplot(133), plt.imshow(iimg, 'gray'), plt.title('Inverse Fourier Image')
            plt.axis('off')
            plt.show()

            return







        time_start = time.time() 
        window = tk.Tk()
        window.title('实验二')
        window.geometry('700x300')
        window.minsize(700, 300)  
        window.maxsize(700, 300)  
        window.resizable(0,0) 
        
        tk.Label(window, text='X轴平移量:').place(x=20, y=80)
        tk.Label(window, text='Y轴平移量:').place(x=20, y=120)
        tk.Label(window, text=' 旋转角度:').place(x=20, y=160)
       
        x_translation = tk.StringVar()
        x_name = tk.Entry(window, textvariable=x_translation)
        x_name.place(x=100, y=80)

        y_translation = tk.StringVar()
        y_name = tk.Entry(window, textvariable=y_translation)
        y_name.place(x=100, y=120)

        r_translation = tk.StringVar()
        r_name = tk.Entry(window, textvariable=r_translation)
        r_name.place(x=100, y=160)

        bt_login = tk.Button(window, text='平移', command=select_translation)
        bt_login.place(x=50, y=200)
        bt_logup = tk.Button(window, text='旋转', command=select_rotation)
        bt_logup.place(x=150, y=200)

        bt_logquit = tk.Button(window, text='退出', command=exit)
        bt_logquit.place(x=10, y=10)
        plt.ion()
        plt.show()
        tk.Label(window, text=
            '        上述公式为信号时移和频移公式，其中u,v是频率变量，x,y是空间域'
            '图像变量，平移的过程中，无论是时移还是频移都不会改变幅值。源'
            '代码中的meshgrid函数为生成网格采样点函数，帮助绘图。在使用这个'
            '函数采样时，需要注意图像的长宽都需要是偶数，不然就会使原图像'
            '变暗，甚至没有图像。'+'\n'+
            '        图像的平移变换就是将图像中的所有像素点按照要求的偏移量进行垂直、'
            '水平移动。平移变换只是改变了原有景物在画面上的位置，而图像内容不'
            '发生改变。而图像的平移就是讲图像像素点（x,y）平移到(x-x0,y-y0),'
            '而FFT的时移特性满足此效果。'
            ,wraplength=300,justify='left').place(x=300, y=10)
        window.mainloop()



    pass
