import tkinter as tk
from tkinter import messagebox
from tkinter import *
def Hamtao():
 def tinh_bmi():
    try:
      chieucao=float(chieucao_entry.get())
      cannang=float(cannang_entry.get())
      if chieucao<0 and cannang<0:
           messagebox.showerror("Loi","khong hop le")
           return
      else:
       bmi=cannang/(chieucao**2)
       chisobmi_ketqua.set(str(round(bmi,2)))
      if bmi<18.5:
             status='thieu can'
             rick="sap chet doi"
      elif 18.5<bmi<24.9:
            status='binh thuong'
            rick="sduma binh thuong"
      elif 25<bmi<29.9:
            status='thua can'
            rick="on day bia"
      else:
            status='beo phi'
            rick="nguykich"
      trangthai_ketqua.set(status)
      tinhtrang_ketqua.set(rick)
    except ValueError:
        messagebox.showerror("Loi","Vui long nhap so hop le")
 
 def thoat():
    root.quit()
 
 root=tk.Tk()
 root.geometry("300x400")
 root.title("Tính BMI")
 root.configure(bg="yellow")

 nhap_frame=tk.Frame(root)
 nhap_frame.pack(pady=20)
 nhap_frame.configure(bg="yellow")

 chieucao=tk.Label(nhap_frame,text=("ChieuCao"),font=("Arial",12),bg="yellow")
 chieucao.grid(row=0,column=0,pady=10,padx=20,sticky="w")

 cannang=tk.Label(nhap_frame,text=("CanNang"),font=("Arial",12),bg="yellow")
 cannang.grid(row=1,column=0,pady=10,padx=20,sticky="w")

 chieucao_entry=tk.Entry(nhap_frame,font=("Arial",12),width=10)
 chieucao_entry.grid(row=0,column=1,pady=10,sticky="e")

 cannang_entry=tk.Entry(nhap_frame,font=("Arial",12),width=10)
 cannang_entry.grid(row=1,column=1,pady=10,sticky="e")
 
 btn_tinh=tk.Button(nhap_frame,text="Tinh BMI",font=("Arial",12),command=tinh_bmi,bg="pink")
 btn_tinh.grid(row=2,column=1,pady=10,padx=10,sticky="ne")

 chisobmi=tk.Label(nhap_frame,text=("chi so bmi cua ban"),font=("Arial",12),bg="yellow")
 chisobmi.grid(row=3,column=0,pady=10,padx=20,sticky="w")

 chisobmi_ketqua=tk.StringVar()
 chisobmi_ketqua.set("")
 
 chisobmi_entry=tk.Entry(nhap_frame,textvariable=chisobmi_ketqua,width=20)
 chisobmi_entry.grid(row=3,column=1,pady=10,sticky="e")

 trangthai=tk.Label(nhap_frame,text=("Trang thai suc khoe"),font=("Arial",12),bg="yellow")
 trangthai.grid(row=4,column=0,pady=10,padx=20,sticky="w")
  
 trangthai_ketqua=tk.StringVar()
 trangthai_ketqua.set("")
 trangthai_entry=tk.Entry(nhap_frame,textvariable=trangthai_ketqua,width=20)
 trangthai_entry.grid(row=4,column=1,pady=10,sticky="e")

 tinhtrang=tk.Label(nhap_frame,text=("Tinh trang suc khoe"),font=("Arial",12),bg="yellow")
 tinhtrang.grid(row=5,column=0,pady=10,padx=20,sticky="w")

 tinhtrang_ketqua=tk.StringVar()
 tinhtrang_ketqua.set("")
 tinhtrang_entry=tk.Entry(nhap_frame,textvariable=tinhtrang_ketqua,width=20)
 tinhtrang_entry.grid(row=5,column=1,pady=10,sticky="e")
 btn_thoat=tk.Button(nhap_frame,text="Thoat",font=("Arial",12),command=thoat,bg="pink")
 btn_thoat.grid(row=6,column=0,pady=10,padx=10,sticky="nsew")


 root.mainloop()    
 
if __name__=="__main__":
 Hamtao()
