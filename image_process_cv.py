import cv2
import numpy as np
import math

def Image_init():
    global img_orig, img_proc
    img_orig = np.zeros((600, 1024, 3), np.uint8)
    img_orig = cv2.cvtColor(img_orig, cv2.COLOR_BGR2RGB)
    img_proc = img_orig.copy()
    return img_proc

def Image_read(imgname):    #受け取ったファイル名を開く
    global img_orig, img_proc
    img_orig = cv2.imread(imgname)
    img_orig = cv2.cvtColor(img_orig, cv2.COLOR_BGR2RGB)
    img_proc = img_orig.copy()
    img_orig_height, img_orig_width, img_orig_channels = img_orig.shape[:3]
    return img_proc, img_orig_width, img_orig_height
 
result = 0
resultmes = ""

clicks = 0
clickpos = [[0 for i in range(2)] for j in range(4)]
zoom = 1.0

def zoom_changed(z):
    global zoom
    
    return img_proc

def mouse_move(x, y, lbtn, mode):
    global img_orig, img_proc, clicks, clickpos
    #if (mode == 0) :
    return img_proc
        
def mouse_lbtn_down(x, y, lbtn, mode):
    global img_orig, img_proc, clicks, clickpos, zoom
    if (mode == 0) :
        print("LBtn_Down")
    return img_proc
        
def mouse_lbtn_up(x, y, lbtn, mode):
    global img_orig, img_proc, clicks, clickpos, zoom
    if (mode == 0) :
        if (clicks < 4):
            print("LBtn_Up")
            clickpos[clicks][0] = x
            clickpos[clicks][1] = y
            #クリックした回数を増加させる
            clicks += 1
            ruler_redraw()
        if (clicks == 4):
            ruler_calc()
            
    return img_proc

def ruler_redraw():
    global img_orig, img_proc, clicks, clickpos, zoom
    img_proc = img_orig.copy()
    for i in range(clicks):
        if i < 2:
            color = (0, 0, 255)
        else: 
            color = (255, 0, 0)
        print("%d", clickpos)
        #偶数回目のクリックの時、線を表示する、
        if ((i+1)%2) == 0:
            print("%d", i)
            cv2.line(img_proc, (clickpos[i-1][0], clickpos[i-1][1]), 
                     (clickpos[i][0], clickpos[i][1]), color,
                     thickness=1, lineType=cv2.LINE_AA)
        
        cv2.circle(img_proc, (clickpos[i][0], clickpos[i][1]), 5, color, -1)
    
def ruler_calc():
    global clickpos, resultmes
    
    #三平方の定理を使用し、点と点の距離の差を算出する
    kyori1 = math.sqrt( (clickpos[0][0]-clickpos[1][0])**2+(clickpos[0][1]-clickpos[1][1])**2 )
    kyori2 = math.sqrt( (clickpos[2][0]-clickpos[3][0])**2+(clickpos[2][1]-clickpos[3][1])**2 )

    #比の計算を行う
    ratio = kyori2/kyori1
    result = 10.0*ratio
    
    resultmes = '基準の距離 : %d ピクセル'%(kyori1) + '測定した距離 : %d ピクセル'%(kyori2) + '結果 : %.2f cm'%(result)
    