from selectors import SelectSelector
from tkinter import *
from tkinter.constants import CENTER


def giaiAction():
    a=float(stringHSA.get())
    b=float(stringHSB.get())
    if a==0 and b==0:
        stringKQ.set("VOSONGHIEM")
    elif a==0 and b!=0:
        stringKQ.set("VONghiem")
    else:
        stringKQ.set("X="+str(-b/a))
root=Tk()
stringHSA=StringVar()
stringHSB=StringVar()
stringKQ=StringVar()
def tiepAction():
    stringHSA.set("")
    stringHSB.set("")
    stringKQ.set("")
root.title("dualuoi")
root.minsize(width=250, height=150)
root.resizable(width=True, height=True)
Label(root,text="Phuonng Trinh Bac 1",fg="light pink",font=("tohama",16),justify=CENTER).grid(row=0,columnspan=2)

Label(root,text="Hệ Số a").grid(row=1,column=0)
Entry(root,width=30,textvariable=stringHSA).grid(row=1,column=1)

Label(root,text="Hệ Số b").grid(row=2,column=0)
Entry(root,width=30,textvariable=stringHSB).grid(row=2,column=1)

frameButton=Frame()
Button(frameButton,text="giai action",command=giaiAction).pack(side=LEFT)
Button(frameButton,text="tiep action",command=tiepAction).pack(side=LEFT)
Button(frameButton,text="giai action",command=giaiAction).pack(side=LEFT)
frameButton.grid(row=3,columnspan=2)
Label(root,text="Kết Quả").grid(row=4,column=0)
Entry(root,width=30,textvariable=stringKQ).grid(row=4,column=1)
root.mainloop()

