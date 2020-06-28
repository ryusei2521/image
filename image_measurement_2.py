import tkinter
import tkinter.filedialog  as tkdialog
from tkinter import font
from PIL import Image, ImageTk
import os
import image_process_cv
 
root = tkinter.Tk()
window_width = 1280
window_height = 720
root.geometry(str(window_width)+"x"+str(window_height))


def Disp_image(img_temp):
    global img_tk, labelmes
    img_tk= ImageTk.PhotoImage(Image.fromarray(img_temp))
    canvas.create_image(0, 0, image = img_tk, anchor = tkinter.NW )
    labelmes = image_process_cv.resultmes
    label.set(labelmes)
 
def File_open():
    fname = tkdialog.askopenfilename(filetypes=[('画像ファイル', '*.bmp;*.dib;*.jpg;*.jpeg;*.jpe;*.jfif;*.gif;*.tif*.tiff;*.png')],initialdir=os.getcwd())
    img, ox, oy = image_process_cv.Image_read(fname)
    Disp_image(img)
    root.title("画像計測ツール - "+str(fname))
 
def Mode_ruler():
    mode = 0
 
def Mode_tparc():
    mode = 1

def getwindowsize(event):
    global window_width, window_height
    if (event.type != 'configure') and (event.widget != root):
        return

    # サイズが変わってなかった無視
    if (event.width == window_width) and (event.height == window_height):
        return

    # グローバル変数を更新
    window_width = event.width
    window_height = event.height
    canvas.config(width = window_width-4, height = window_height-40)
    
lbtn = 0
mode = 0
def mouse_move(event):
    img = image_process_cv.mouse_move(event.x-2, event.y, lbtn, mode)
    Disp_image(img)
    
def mouse_lbtn_down(event):
    lbtn = 1
    img = image_process_cv.mouse_lbtn_down(event.x-2, event.y, lbtn, mode)
    Disp_image(img)
    
def mouse_lbtn_up(event):
    lbtn = 0
    img = image_process_cv.mouse_lbtn_up(event.x-2, event.y, lbtn, mode)
    Disp_image(img)
 

menubar = tkinter.Menu(root)
filemenu = tkinter.Menu(menubar, tearoff=0)
filemenu.add_command(label="画像を開く", command=File_open)
filemenu.add_separator()
filemenu.add_command(label="終了", command=root.quit)
menubar.add_cascade(label="ファイル", menu=filemenu)
editmenu = tkinter.Menu(menubar, tearoff=0)
editmenu.add_command(label="直線で長さ計測", command=Mode_ruler)
editmenu.add_command(label="3点円弧", command=Mode_tparc)
menubar.add_cascade(label="計測モード", menu=editmenu)
 
root.config(menu=menubar)
root.config()

label = tkinter.StringVar()
label.set("画像ファイルを開いてください")
lbl = tkinter.Label(textvariable = label, font = ("Meiryo UI", 12))
lbl.place(x = window_width-64, y = 16, anchor = tkinter.E)

img_File_Open = tkinter.PhotoImage(file="Icons\File_Open.png")
btn_File_Open = tkinter.Button(root, text="a", image=img_File_Open, bd = 0, width=32, command=File_open)
btn_File_Open.place(x=2, y=2)

canvas = tkinter.Canvas(root, width = window_width, height = window_height, bg = 'black')
canvas.place(x=0, y=36)  
canvas.bind('<Motion>', mouse_move)
canvas.bind('<ButtonPress-1>', mouse_lbtn_down)
canvas.bind('<ButtonRelease-1>', mouse_lbtn_up) 

root.bind('<Configure>', getwindowsize)
root.title("画像計測ツール")
root.option_add('*font', ('Meiryo UI', 9))

img = image_process_cv.Image_init()
Disp_image(img)

root.mainloop()
