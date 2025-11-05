from tkinter import*
def tong():
    a=float(stringHSA.get())
    b=float(stringHSB.get())
    tong=a+b
    stringKQ.set(""+tong)

def Tru():
    a=float(stringHSA.get())
    b=float(stringHSB.get())
    tru=a-b
    stringKQ.set(""+tru)
def Nhan():
    a=float(stringHSA.get())
    b=float(stringHSB.get())
    nhan=a*b
    stringKQ.set(""+nhan)
def Chia():
    a=float(stringHSA.get())
    b=float(stringHSB.get())
    chia=a/b
    if a>b :
        stringKQ.set(""+b/a)
    else:
     stringKQ.set(""+chia)
root=Tk()
stringHSA=StringVar()
stringHSB=StringVar()
stringKQ=StringVar()

root.title("Btrancute")
root.minsize(width=200, height=150)
root.resizable(width=True, height=True)
Label(root,text="Cộng Hành Nhập Cắt",fg="deep pink",font=("tohama",16)).grid(row=0,columnspan=3)
frameButton=Frame(root)
Button(frameButton ,text="cộng",command=tong).pack(side=TOP,fill=X)
Button(frameButton ,text="trừ",command=Tru).pack(side=TOP,fill=X)
Button(frameButton ,text="nhân",command=Nhan).pack(side=TOP,fill=X)
Button(frameButton ,text="chia",command=Chia).pack(side=TOP,fill=X)
frameButton.grid(row=1,column=0,rowspan=4)

Label(root,text="số a").grid(row=1,column=1)
Entry(root,width=15,textvariable=stringHSA).grid(row=1,column=2)

Label(root,text="số b").grid(row=2,column=1)
Entry(root,width=15,textvariable=stringHSB).grid(row=2,column=2)


Label(root,text="Kết Quả").grid(row=3,column=1)
Entry(root,width=15,textvariable=stringKQ).grid(row=3,column=2)

Button(root,text="thoát",command=root.quit).grid(row=4,column=2)

root.mainloop()
