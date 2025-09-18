toan=float(input("Nhập số điểm toán:"))
ly=float(input("Nhập số điểm lý:"))
hoa=float(input("Nhập số điểm hóa:"))
dtb=(toan+ly+hoa)/3
print("Điểm trung bình:",dtb)
if dtb>=8:
    print("Học lực giỏi")
elif dtb>=6.5:
    print("Học lực khá")
elif dtb>=5:
    print("Học lực trung bình")
elif dtb>=3.5:
    print("Học lực yếu")
else:
    print("Học lực kém")
#Câu 3 Tính Điểm Trung Bình và Xếp Loại Học Lực