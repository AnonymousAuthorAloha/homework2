# 图形学作业2-使用梁友栋-Barsky算法裁剪直线
# 1.不能使用Tkinter库函数或其他任何函数库绘制图形，只能使用下面预定义的point函数绘制点。 示例point(cv, 1, 2)
#   绘制直线使用第一次作业的Bresenham算法即可
# 2.实现梁友栋-Barsky算法
# 3.将随机直线裁剪到“显示区域”内部，否则不绘制（框架会自动绘制一个红色虚线）

import random
from tkinter import *

def point(cv, x, y,outline="black",width=5):
    # cv: tkinter画布
    x *= 5
    y *= 5
    cv.create_rectangle(x, y, x + 1, y + 1, outline=outline, width=width)

################################以下为作业区(算法)################################
def Bresenham(cv, p0, p1,color='black'):
    (x0,y0)=p0
    (x1,y1)=p1
    steep = abs(y1 - y0) > abs(x1 - x0)
    if steep:
        x0,y0=y0,x0
        x1,y1=y1,x1
    if x0 > x1:
        x0,x1=x1,x0
        y0,y1=y1,y0
    if y0 > y1:
        t = -1
    else:
        t = 1
    xx = x1 - x0
    yy = abs(y1 - y0)
    y = y0
    error = 0
    for x in range(x0, x1 + 1):
        if steep:
            point(cv, y, x,color)
        else:
            point(cv, x, y,color)
        error = error + yy
        if 2 * error >= xx:
            y = y + t
            error = error - xx

def L_Barsky(cv, p0, p1,xl,xr,yt,yb):
    return

def cansee(q, d, t0, t1):
    return
    

################################以上为作业区(算法)################################

if __name__ == "__main__":
    root = Tk()
    root.title("图形学作业2-使用梁友栋-Barsky算法裁剪直线")
    root.geometry("+100+100")
    cv = Canvas(root, background="white", width=500, height=500)
    cv.pack(fill=BOTH, expand=YES)

    def my_mainloop():
        cv.delete("all")
        ################################显示区域设置################################
        xl=30;xr=70;yt=30;yb=70 # 设置一个虚拟的显示区域
        cv.create_rectangle(xl*5,yt*5,xr*5,yb*5,width=5)# 显示区域矩形框
        # 随机生成两点
        p0=(random.randint(5,90),random.randint(5,90))
        p1=(random.randint(5,90),random.randint(5,90))
        # 生成两点间虚线
        cv.create_line(p0[0]*5,p0[1]*5,p1[0]*5,p1[1]*5,fill="red",width=3,dash=".-")
        ################################显示区域设置################################
        L_Barsky(cv, p0, p1,xl,xr,yt,yb)# 调用梁友栋-Barsky算法
        root.after(1000, my_mainloop) # 循环生成测试用例并显示
 
    root.after(1, my_mainloop)
    root.mainloop()

