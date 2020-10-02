import sys
from PIL import ImageColor
import cv2
import os
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog
import shutil
import numpy as np
from PIL import Image,ImageTk 
from functools import partial
from tkinter import messagebox,simpledialog

class Application(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.pack()
        self.fileName=["",""]
        self.fileLabel=[tk.Label(root),tk.Label(root)]
        self.fileLabelPlace=[[100,640],[750,640]]
        self.image=[cv2.imread("ex1.png"),cv2.imread("ex2.png")]
        self.img=[ImageTk.PhotoImage(Image.fromarray(self.image[0])),ImageTk.PhotoImage(Image.fromarray(self.image[1]))]
        self.imageSize=(400,400)
        self.imgColor=[[0,0,0],[0,0,0]]
        self.formula=""
        self.answer=""

        self.CreateWigets()

    def CreateWigets(self):
        #画像表示用キャンバス
        self.canvas=[tk.Canvas(root,width=500,height=500),tk.Canvas(root,width=500,height=500)]
        self.canvas[0].place(x=110,y=100)
        self.canvas[1].place(x=770,y=100)

        #計算式表示用ラベル
        self.formulaLabel=tk.Label(root,text=self.formula,font=("Bold",30))
        self.answerLabel=tk.Label(root,text=self.answer,font=("Bold",30))

        #ファイル選択ボタン
        image1Button=tk.Button(root,text="画像1を選択",width=15,font=("",15),command=partial(self.SelectImage,0))
        image1Button.place(x=225,y=600)
        image2Button=tk.Button(root,text="画像2を選択",width=15,font=("",15),command=partial(self.SelectImage,1))
        image2Button.place(x=875,y=600)
        #変数ボタン
        r1Button=tk.Button(root,text="R1",width=5,font=("",15),command=partial(self.RButton,0))
        r1Button.place(x=540,y=300)
        g1Button=tk.Button(root,text="G1",width=5,font=("",15),command=partial(self.GButton,0))
        g1Button.place(x=610,y=300)
        b1Button=tk.Button(root,text="B1",width=5,font=("",15),command=partial(self.BButton,0))
        b1Button.place(x=680,y=300)
        r2Button=tk.Button(root,text="R2",width=5,font=("",15),command=partial(self.RButton,1))
        r2Button.place(x=540,y=340)
        g2Button=tk.Button(root,text="G2",width=5,font=("",15),command=partial(self.GButton,1))
        g2Button.place(x=610,y=340)
        b2Button=tk.Button(root,text="B2",width=5,font=("",15),command=partial(self.BButton,1))
        b2Button.place(x=680,y=340)
        #計算ボタン
        addButton=tk.Button(root,text="+",width=5,font=("",15),command=partial(self.AddButton))
        addButton.place(x=540,y=380)
        subButton=tk.Button(root,text="-",width=5,font=("",15),command=partial(self.SubButton))
        subButton.place(x=610,y=380)
        multiButton=tk.Button(root,text="×",width=5,font=("",15),command=partial(self.MultiButton))
        multiButton.place(x=680,y=380)
        divButton=tk.Button(root,text="÷",width=5,font=("",15),command=partial(self.DivButton))
        divButton.place(x=540,y=420)
        equalButton=tk.Button(root,text="=",width=18,font=("",15),command=partial(self.EqualButton))
        equalButton.place(x=540,y=460)
        #記号ボタン
        leftBracketButton=tk.Button(root,text="(",width=5,font=("",15),command=partial(self.LeftBracketButton))
        leftBracketButton.place(x=610,y=420)
        rightBracketButton=tk.Button(root,text=")",width=5,font=("",15),command=partial(self.RightBracketButton))
        rightBracketButton.place(x=680,y=420)
        #消去ボタン
        clearButton=tk.Button(root,text="clear",width=18,font=("",15),command=partial(self.ClearButton))
        clearButton.place(x=540,y=500)

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
            self.fileLabel[num]=tk.Label(root,text=fileName,font=("",15))
            self.fileLabel[num].place(x=self.fileLabelPlace[num][0],y=self.fileLabelPlace[num][1])
            self.ReadImage(num)
            self.DisplayImage(num)

    #Rボタン
    def RButton(self,num):
        self.formula+="R"+str(num+1)
        self.UpdateFormula()

    #Gボタン
    def GButton(self,num):
        self.formula+="G"+str(num+1)
        self.UpdateFormula()

    #Bボタン
    def BButton(self,num):
        self.formula+="B"+str(num+1)
        self.UpdateFormula()

    #+ボタン
    def AddButton(self):
        self.formula+="+"
        self.UpdateFormula()

    #-ボタン
    def SubButton(self):
        self.formula+="-"
        self.UpdateFormula()

    #×ボタン
    def MultiButton(self):
        self.formula+="×"
        self.UpdateFormula()

    #÷ボタン
    def DivButton(self):
        self.formula+="÷"
        self.UpdateFormula()

    #(ボタン
    def LeftBracketButton(self):
        self.formula+="("
        self.UpdateFormula()

    #)ボタン
    def RightBracketButton(self):
        self.formula+=")"
        self.UpdateFormula()

    #=ボタン
    def EqualButton(self):
        self.formula=self.formula.replace("×","*").replace("÷","/")

        for i in range(0,2):
            self.formula=self.formula.replace("R"+str(i+1),str(self.imgColor[i][0]))
            self.formula=self.formula.replace("G"+str(i+1),str(self.imgColor[i][1]))
            self.formula=self.formula.replace("B"+str(i+1),str(self.imgColor[i][2]))

        self.answer="= "+str(eval(self.formula))
        self.DisplayAnswer()

    #消去ボタン
    def ClearButton(self):
        self.formula=""
        self.answer=""
        self.UpdateFormula()
        self.answerLabel.pack_forget()

    #計算式更新
    def UpdateFormula(self):
        self.formulaLabel.pack_forget()
        self.formulaLabel=tk.Label(root,text=self.formula,font=("Bold",30))
        self.formulaLabel.pack(side=tk.TOP,anchor=tk.NE)

    #解表示
    def DisplayAnswer(self):
        self.answerLabel.pack_forget()
        self.answerLabel=tk.Label(root,text=self.answer,font=("Bold",30))
        self.answerLabel.pack(side=tk.TOP,anchor=tk.NE)

    #画像読み込み
    def ReadImage(self,num):
        shutil.copy(self.fileName[num],"./image"+str(num+1)+".png")
        self.image[num]=cv2.imread("./image"+str(num+1)+".png")
        self.image[num]=cv2.resize(self.image[num],dsize=self.imageSize)
        self.image[num]=cv2.cvtColor(self.image[num],cv2.COLOR_BGR2RGB)
        self.GetPixelValue(num)

    #画像表示
    def DisplayImage(self,num):
        self.img[num]=ImageTk.PhotoImage(Image.fromarray(self.image[num]))
        self.canvas[num].create_image(0,0,image=self.img[num],anchor=tk.NW)

    #画素値集計
    def GetPixelValue(self,num):
        for i in range(0,self.imageSize[0]):
            for j in range(0,self.imageSize[1]):
                color=self.image[num][j,i]
                for k in range(0,3):
                    self.imgColor[num][k]+=int(color[k])
        
        for i in range(0,3):
            self.imgColor[num][i]/=self.imageSize[0]*self.imageSize[1]

root = tk.Tk()
myapp = Application(master=root)
myapp.master.title("ImageCalc")
myapp.master.geometry("1280x720")

myapp.mainloop()