import sys
import cv2
import os
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog
import shutil
from PIL import Image,ImageTk 
from functools import partial
from tkinter import messagebox,simpledialog

class Application(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.pack()
        self.fileName=["",""]
        self.fileLabel=[tk.Label(root),tk.Label(root)]
        self.fileLabelPlace=[[240,640],[900,640]]
        self.image=[cv2.imread("ex1.png"),cv2.imread("ex2.png")]

        self.CreateWigets()

    def CreateWigets(self):
        #画像表示用キャンバス
        self.canvas=[tk.Canvas(root,width=500,height=500),tk.Canvas(root,width=500,height=500)]
        self.canvas[0].place(x=0,y=0)
        self.canvas[1].place(x=640,y=0)

        #ファイル選択ボタン
        image1Button=tk.Button(root,text="画像1を選択",width=15,font=("",15),command=partial(self.SelectImage,0))
        image1Button.place(x=260,y=600)
        image2Button=tk.Button(root,text="画像2を選択",width=15,font=("",15),command=partial(self.SelectImage,1))
        image2Button.place(x=920,y=600)
        #実行ボタン
        margeButton=tk.Button(root,text="実行",width=10,font=("",15),command=partial(self.MargeImage))
        margeButton.place(x=600,y=680)

    #ファイル選択
    def SelectImage(self,num):
        fTyp = [("", "*")]
        iDir=os.path.abspath(os.path.dirname(__file__))
        fileName=tk.filedialog.askopenfilename(filetypes=fTyp,initialdir=iDir)
        if len(fileName) == 0:
            self.fileName[num] = ""
        else:
            self.fileName[num] = fileName
            self.fileLabel[num].destroy()
            self.fileLabel[num]=tk.Label(root,text=fileName,font=("",15),justify="center")
            self.fileLabel[num].place(x=self.fileLabelPlace[num][0],y=self.fileLabelPlace[num][1])
            self.ReadImage(num)
            self.DisplayImage(num)

    #マージ実行/表示
    def MargeImage(self):
        a=0

    #画像読み込み
    def ReadImage(self,num):
        shutil.copy(self.fileName[num],"./image"+str(num+1)+".png")
        self.image[num]=cv2.imread("./image"+str(num+1)+".png")
        self.image[num]=cv2.resize(self.image[num],dsize=(500,500))
        self.image[num]=cv2.cvtColor(self.image[num],cv2.COLOR_BGR2RGB)

    #画像表示
    def DisplayImage(self,num):
        img=ImageTk.PhotoImage(Image.fromarray(self.image[num]))
        self.canvas[num].create_image(0,0,image=img,anchor=tk.NW)

root = tk.Tk()
myapp = Application(master=root)
myapp.master.title("ImageCalc")
myapp.master.geometry("1280x720")

myapp.mainloop()