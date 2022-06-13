import matplotlib.pyplot as plt
import numpy as np
import cv2 
import tkinter as tk
import time
'''
        实验五--图像阈值分割与形态学运算实验
        一、实验任务
            显示图像的直方图，根据图像的直方图中图像的灰度分布，
        选择最佳阈值，实现图像的二值化；并显示腐蚀、膨胀、开运算、
        闭运算对二值图像的操作的结果，总结四种形态学运算的特点。
        二、实验目的
            1、学习利用图像直方图选择阈值的方法；
            2、掌握图像阈值分割方法；
            3、掌握基本的图像形态学算法的特点。
'''
class Class_Experiment_5():
    def sys_loop_1(file_name):
        def exit():
            from Register import Class_Select
            time_end = time.time()
            time_c= time_end - time_start   #运行所花时间
            time_cost=int(time_c)
            tk.messagebox.showinfo(title='成绩结算',
                                       message='实验结束'+'\n')

            window.destroy()
            Class_Select.select()
            return
        #判断输入是否为数字
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






        #1,
        #计算图像的直方图，即将图像所有的像素点按照0~255共256个bin，统计落在每个bin的像素点数量

        #2,
        #归一化直方图，也即将每个bin中像素点数量除以总的像素点，使其限制在0~1之间

        #3,
        #设置一个分类的阈值i，也即一个灰度级，开始从0迭代

        #4,
        #通过归一化的直方图，统计0~i 灰度级的像素(假设像素值在此范围的像素叫做前景像素) 所占整幅图像的比例w0，
        #并统计前景像素的平均灰度u0；统计i~255灰度级的像素(假设像素值在此范围的像素叫做背景像素) 所占整幅图像的比例w1，并统计背景像素的平均灰度u1；
        #在这里，设图像的总平均灰度为u2，类间方差记为g
        #其中：
        #u2=ω0∗u0+ω1∗u1
        #g=ω0*(u0−μ2)^2+ω1*(u1−u2)^2
        #将u2带入g中，可得：
        #g=ω0*ω1*(u0−u1)^2

        #5,
        #++i,阈值的灰度值加1，并转到第4个步骤，直到i为256时结束迭代

        #6,
        #将最大g相应的值作为图像的全局阈值




        #OpenCV核心代码

        #OTSU算法

        def otsu(img):

            # 图像像素点总和
            h=img.shape[0]
            w=img.shape[1]
            m=h*w   

            otsuimg=np.zeros((h,w),np.uint8)


            #定义临时阈值和最终阈值
            threshold_max=threshold=0   
            # 各灰度级个数
            histogram=np.zeros(256,np.int32)   
            # 各灰度级占比
            probability=np.zeros(256,np.float32)   


            #得到直方图
            for i in range (h):
                for j in range (w):
                    # 统计每个灰度级在整幅图像中的个数
                    s=img[i,j]
                    histogram[s]+=1   

            #归一化直方图
            for k in range (256):
                #归一化，变为0-1的区间
                probability[k]=histogram[k]/m   


            #根据方差得到阈值
            #从0-255找出最大方差
            for i in range (255):

                #前景像素点 在灰度级的占比
                w0 = 0    
                #背景像素点 在灰度级的占比
                w1 = 0    
                #前景像素点 灰度级总和
                fgs = 0  
                #背景像素点 灰度级总和
                bgs = 0   

                for j in range (256):
                    if j<=i:   # 当前i为分割阈值
                        w0+=probability[j]   # 前景像素点占整幅图像的比例累加
                        fgs+=j*probability[j]
                    else:
                        w1+=probability[j]   # 背景像素点占整幅图像的比例累加
                        bgs+=j*probability[j]

                u0=fgs/w0   # 前景像素点的平均灰度
                u1=bgs/w1   # 背景像素点的平均灰度
                g=w0*w1*(u0-u1)**2   # 类间方差

                #找出i从0到255的最大的方差，即
                #分开程度最大的阈值
                if g>=threshold_max:
                    threshold_max=g
                    threshold=i

            print(threshold)

            #图像二值化
            for i in range (h):
                for j in range (w):
                    if img[i,j]>threshold:
                        otsuimg[i,j]=255
                    else:
                        otsuimg[i,j]=0

            return otsuimg

        #OTSU算法

        def insert_point():

            #读取彩色图片
            img=cv2.imread(file_name,0)
            #转换成灰度图
            img_otsu = otsu(img)

            #创建矩形结构单元
            g=cv2.getStructuringElement(cv2.MORPH_RECT,(9,9))

            #形态学处理
            #膨胀
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
            pic1 = cv2.morphologyEx(img_otsu, cv2.MORPH_ERODE,kernel)
            #腐蚀
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
            pic2 = cv2.morphologyEx(img_otsu, cv2.MORPH_DILATE,kernel)
            #开运算
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
            pic3 = cv2.morphologyEx(img_otsu, cv2.MORPH_OPEN,kernel)
            #闭运算
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
            pic4 = cv2.morphologyEx(img_otsu, cv2.MORPH_CLOSE,kernel)

            #调用calcHist()绘制直方图
            #图像，通道[0]-灰度图，掩膜-无，灰度级，像素范围
            hist1 = cv2.calcHist([img],[0],None,[256],[0,255])
            hist2 = cv2.calcHist([img_otsu],[0],None,[256],[0,255])

            #画图部分
            fig=plt.figure(1,(8, 4))
            b=fig.add_subplot(241)
            b.imshow(img,cmap=plt.cm.gray)
            fig=plt.figure(1)
            plt.title("Original")
            plt.xticks([]), plt.yticks([])

            b=fig.add_subplot(242)
            b.imshow(img_otsu,cmap=plt.cm.gray)
            fig=plt.figure(1)
            plt.title("OTSU")
            plt.xticks([]), plt.yticks([])

            b=fig.add_subplot(243)
            b.imshow(pic1,cmap=plt.cm.gray)
            fig=plt.figure(1)
            plt.title("Erode")
            plt.xticks([]), plt.yticks([])

            b=fig.add_subplot(244) 
            b.imshow(pic2,cmap=plt.cm.gray) 
            fig=plt.figure(1)  
            plt.title("Dilate")
            plt.xticks([]), plt.yticks([])

            b=fig.add_subplot(245)  
            plt.plot(hist1) 
            fig=plt.figure(1)  
            plt.title("Histogram")
            plt.xticks([]), plt.yticks([])

            b=fig.add_subplot(246) 
            plt.plot(hist2)
            fig=plt.figure(1)  
            plt.title("Histogram")
            plt.xticks([]), plt.yticks([])

            b=fig.add_subplot(247) 
            b.imshow(pic4,cmap=plt.cm.gray)  
            fig=plt.figure(1)  
            plt.title("Open")
            plt.xticks([]), plt.yticks([])

            b=fig.add_subplot(248) 
            b.imshow(pic4,cmap=plt.cm.gray)  
            fig=plt.figure(1)  
            plt.title("Close")
            plt.xticks([]), plt.yticks([])


        time_start = time.time() 
        window = tk.Tk()
        window.title('实验五')
        window.geometry('700x300')
        window.minsize(700, 300)  
        window.maxsize(700, 300)  
        window.resizable(0,0) 

        b1 = tk.Button(window, text='开始实验', command=insert_point)
        b1.place(x=150, y=200)

        bt_logquit = tk.Button(window, text='退出', command=exit)
        bt_logquit.place(x=10, y=10)
       
        plt.ion()
        plt.show()

        tk.Label(window, text=
            '        阈值分割是一种按图像像素灰度幅度分割的方法，它是把图像'
            '的灰度分成不同的等级，然后用设置灰度门限(阈值)的方法确定有意义的'
            '区域或要分割物体的边界。阈值化图像分割的难点在于:在图像分割之前，'
            '难以确定图像分割区域的数目，或者说要把图像分割成几个部分;另一个是'
            '阈值的确定，因为阈值选择的准确性直接影响分割的精度及图像描述分析的'
            '正确性。对于只有背景和目标两类对象的灰度图像来说，阈值选取过高，'
            '容易把大量的目标误判为背景，阈值选取过低，又容易把大量的背景误判'
            '为目标。阈值化图像分类往往与分割阈值的选取方法有着密切的关系。'
                ,wraplength=300,justify='left').place(x=300, y=10)
        window.mainloop()
        window.mainloop()

    pass

