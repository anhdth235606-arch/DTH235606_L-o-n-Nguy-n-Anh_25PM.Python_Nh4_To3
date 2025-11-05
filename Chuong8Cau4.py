import tkinter as tk
from tkinter import messagebox

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Máy Tính Bỏ Túi")
root.geometry("300x400")
root.resizable(False, False)

# Biến lưu biểu thức
expression = ""

# Tạo màn hình hiển thị
display = tk.Entry(
    root, 
    font=('Arial', 18), 
    justify='right', 
    bd=10, 
    relief=tk.RIDGE
)
display.grid(row=0, column=0, columnspan=4, sticky="we", padx=10, pady=10)

# Hàm thêm dữ liệu
def add_to_expression(value):
    global expression
    expression += str(value)
    display.delete(0, tk.END)
    display.insert(0, expression)

# Hàm xóa
def clear():
    global expression
    expression = ""
    display.delete(0, tk.END)

# Hàm tính kết quả
def calculate():
    global expression
    try:
        if expression:
            result = eval(expression)
            display.delete(0, tk.END)
            display.insert(0, str(result))
            expression = str(result)
    except ZeroDivisionError:
        messagebox.showerror("Lỗi", "Không thể chia cho 0!")
        clear()
    except Exception:
        messagebox.showerror("Lỗi", "Biểu thức không hợp lệ!")
        clear()

# Danh sách các nút
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C'
]

# Tạo các nút
row = 1
col = 0

for button in buttons:
    if button == '=':
        cmd = calculate
        bg = 'green'
    elif button == 'C':
        cmd = clear
        bg = 'red'
    else:
        cmd = lambda x=button: add_to_expression(x)
        bg = 'white'
    
    if button == 'C':
        btn = tk.Button(
            root, 
            text=button, 
            font=('Arial', 14), 
            command=cmd,
            bg=bg,
            fg='white',
            height=2
        )
        btn.grid(row=row, column=col, columnspan=4, sticky="we", padx=10, pady=5)
    else:
        btn = tk.Button(
            root, 
            text=button, 
            font=('Arial', 14), 
            command=cmd,
            bg=bg,
            height=2,
            width=5
        )
        btn.grid(row=row, column=col, padx=5, pady=5)
    
    col += 1
    if col > 3:
        col = 0
        row += 1

# Chạy chương trình
root.mainloop()