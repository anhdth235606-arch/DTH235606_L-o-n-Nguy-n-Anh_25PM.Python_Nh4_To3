from tkinter import *
import tkinter as tk
from tkinter import messagebox
#from SQL_connec import conn, cur, connect_db
#import pyodbc
from DoAn import mo_Doan




def center_window(win, w = 550, h =200):
   ws = win.winfo_screenwidth()
   hs = win.winfo_screenheight()
   x = (ws // 2) - (w // 2)
   y = (hs // 2) - (h // 2)
   win.geometry(f'{w}x{h}+{x}+{y}')


def dangnhap():
   ma = stringUser.get()
   matkhau = stringMK.get()

   if ma == "" or matkhau == "":
       messagebox.showerror("Lỗi", "Vui lòng nhập đăng tên và mật khẩu ")
       return
   elif (ma == "admin" and matkhau == "123456789"):
       messagebox.showinfo("Thành công", "Đăng nhập thành công với quyền Admin!")
       rootDN.destroy()
       mo_Doan()
       return
   else:
        messagebox.showerror("Lỗi", f"Lỗi kết nối cơ sở dữ liệu:")




rootDN = Tk()
rootDN.title("Đăng nhập")
rootDN.minsize(width=550,height=200)
center_window(rootDN)

stringUser = StringVar()
stringMK = StringVar()

Label(rootDN, text="ĐĂNG NHẬP HỆ THỐNG",font=("Times New Roman", 18, "bold")).pack(pady=5, anchor = CENTER)

frame = Frame(rootDN)
frame.pack(pady=5, padx=10, fill="x")

Label(frame, text="Tên đăng nhập:", font=("Times New Roman", 14)).grid(row=0, column=0, padx=5, pady=5,sticky="w")
Entry (frame, width=30, textvariable=stringUser).grid(row=0, column=1, padx=5, pady=5,sticky="w")


Label(frame, text="Mật khẩu:", font=("Times New Roman", 14)).grid(row=1, column=0, padx=5, pady=5,sticky="w")
Entry (frame, width=30, textvariable=stringMK, show="*").grid(row=1, column=1, padx=5, pady=5,sticky="w")


Button(frame, text="Đăng nhập", font=("Times New Roman", 12), width=10, command = dangnhap).grid(row=2, column=1, padx=5, pady=5,sticky="w")


rootDN.mainloop()