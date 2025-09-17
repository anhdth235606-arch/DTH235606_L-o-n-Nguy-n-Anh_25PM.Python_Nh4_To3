#Câu 2 Tính Giờ Phút Giây
t=float(input("Nhập số giây:"))
gio=(t//3600)%24
phut=(t%3600)/60
giay=(t%3600)%60
print(gio,":",phut,":",giay,":")