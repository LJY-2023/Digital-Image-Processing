import cv2
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
import time
'''
        实验四--图像低通与高通滤波实验
        一、实验任务
            运用Matlab 实现图像的FFT变换，分析变换系数的特点，
        并显示变换系数；利用图像低通滤波器和高通滤波器的
        实现对图像的滤波的方法，能够分析不同滤波的滤波效果。
        二、实验目的
            1、学习图像傅里叶变换的特点与应用；
            2、掌握FFT实现图像的高通与低通滤波的方法；
            3、熟悉图像不同滤波图像的效果。
'''
class Class_Experiment_4:
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
        #低通滤波器核心代码
        def select_LPF():

            P_LPF=int(x_name.get())

            #读取彩色图片的通道0，得到灰度图像
            img = cv2.imread(file_name,0)  
            #转为float类型
            img_float = np.float32(img)

            #采用DFT，得到频谱图
            dft = cv2.dft(img_float,flags=cv2.DFT_COMPLEX_OUTPUT)
            dft_shift = np.fft.fftshift(dft)

            #构造低通滤波器
            #得到图像的高和宽
            rows,cols = img.shape 
            #计算中心点坐标
            crow,col = int(rows/2), int(cols/2) 
            # 构造低通滤波器，相当于构造一个掩模
            #构造的size和原图相同，同2通道存储实部和虚部
            mask_LPF = np.zeros((rows,cols,2),np.uint8)
           
            #构造一个以频率为0点中心对称，长30+30，宽30+30的一个区域，只保留区域内部的频率
            mask_LPF[  crow-P_LPF : crow+P_LPF  ,  col-P_LPF  :  col+P_LPF ] = 255 


            #低频的信息都在中间，滤波器和频谱图相乘，遮挡四周，保留中间，中间是低频
            fshift_LPF = dft_shift*mask_LPF  
            #将低频点从图像中间移动到边缘点
            f_ishift_LPF = np.fft.ifftshift(fshift_LPF)

            #IDFT
            img_back_LPF  = cv2.idft(f_ishift_LPF )
            # 还原后的还是有实部和虚部，求二维矢量的幅值，即求图像的幅值
            img_back_LPF  = cv2.magnitude(img_back_LPF [:,:,0],img_back_LPF [:,:,1])


            #画图部分
            plt.subplot(121), plt.imshow(img, cmap='gray')
            plt.title('Original'), plt.xticks([]), plt.yticks([]) 
            plt.subplot(122), plt.imshow(img_back_LPF, cmap='gray')
            plt.title('LPF'), plt.xticks([]), plt.yticks([])  

            return

        #高通滤波器核心代码
        def select_HPF():
           
            P_HPF=int(y_name.get())

            #读取彩色图片的通道0，得到灰度图像
            img = cv2.imread(file_name,0)  
            #转为float类型
            img_float = np.float32(img)
            #采用DFT，得到频谱图
            dft = cv2.dft(img_float,flags=cv2.DFT_COMPLEX_OUTPUT)
            dft_shift = np.fft.fftshift(dft)


            #构造低通滤波器
            #得到图像的高和宽          
            rows,cols = img.shape 
            crow,col = int(rows/2), int(cols/2)  


            #构造高通滤波器，相当于构造一个掩模，设置的越大，低频信息删除的越多

            #构造的size和原图相同，2通道，傅里叶变换后有实部和虚部
            mask_HPF = np.ones((rows,cols,2),np.uint8) 
            #以频率为0处坐标为中心，宽10+10，高10+10的部分抹除
            mask_HPF[crow-P_HPF:crow+P_HPF, col-P_HPF:col+P_HPF] = 0   


            # 删除中间的信息，保留其他部分的信息，低频都集中在中央位置，统一删除
            fshift_HPF = dft_shift*mask_HPF  
            #将低频点从图像中间移动到边缘点
            f_ishift_HPF = np.fft.ifftshift(fshift_HPF)
            #IDFT
            img_back_HPF = cv2.idft(f_ishift_HPF)
            #还原后的还是有实部和虚部，求二维矢量的幅值，即求图像的幅值
            img_back_HPF = cv2.magnitude(img_back_HPF[:,:,0],img_back_HPF[:,:,1])


            #画图部分
            plt.subplot(121), plt.imshow(img, cmap='gray')
            plt.title('Original'), plt.xticks([]), plt.yticks([]) 
            plt.subplot(122), plt.imshow(img_back_HPF, cmap='gray')
            plt.title('HPF'), plt.xticks([]), plt.yticks([])  

            return


        time_start = time.time() 
        window = tk.Tk()
        window.title('实验四')
        window.geometry('700x300')
        window.minsize(700, 300)   
        window.maxsize(700, 300) 
        window.resizable(0,0)

        tk.Label(window, text='LPF参数:').place(x=20, y=80)
        tk.Label(window, text='HPF参数:').place(x=20, y=120)

        x_translation = tk.StringVar()
        x_name = tk.Entry(window, textvariable=x_translation)
        x_name.place(x=95, y=80)

        y_translation = tk.StringVar()
        y_name = tk.Entry(window, textvariable=y_translation)
        y_name.place(x=95, y=120)


        bt_login = tk.Button(window, text='设计低通滤波器', command=select_LPF)
        bt_login.place(x=40, y=200)
        bt_logup = tk.Button(window, text='设计高通滤波器', command=select_HPF)
        bt_logup.place(x=160, y=200)


        bt_logquit = tk.Button(window, text='退出', command=exit)
        bt_logquit.place(x=10, y=10)

        plt.ion()
        plt.show()

        tk.Label(window, text=
        '        从信号的频谱角度来看，随空间位置突变的信息在频域对应的高频部分，而缓变的'
        '信息的低频部分。具体到图像中，边缘和噪声对应于高频区域，而背景及信号缓变部分则对应'
        '于低频区域。因此，可以采用低通滤波的方法来达到滤除（高频）噪声的目的。'+'\n'+
        '        设F(u,v)和G（u,v）分别为含噪声图像f(m,n)和滤除输出图像g(m,n)的频域表示，'
        'H(u，v)为低通滤波器传递函数。'
            ,wraplength=300,justify='left').place(x=300, y=10)
        window.mainloop()
    pass
