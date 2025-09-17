#Câu 1: Tính chu vi diện tích Hình trò
import math
try:
 r=float(input("Mời Bạn Nhập Diện Tích Hình Tròn"))
 cv=2*math.pi*r
 dt=r*r
 print("chu vi",cv)
 print("diện tích",dt)
except:
 print("lỗi rồi")
