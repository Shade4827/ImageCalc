import sys
sys.path.append('D:/anaconda3/envs/ImageCalc/Lib/site-packages')
import cv2
import os
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog
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

        self.CreateWigets()

    def CreateWigets(self):
        #画像表示用キャンバス
        self.canvas1=tk.Canvas(root,width=500,height=500)
        self.canvas1.place(x=-640,y=0)
        self.canvas2=tk.Canvas(root,width=500,height=500)
        self.canvas2.place(x=640,y=0)

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

    #マージ実行
    def MargeImage(self):
        a=0

root = tk.Tk()
myapp = Application(master=root)
myapp.master.title("ImageCalc")
myapp.master.geometry("1280x720")

myapp.mainloop()