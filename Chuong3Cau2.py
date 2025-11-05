print("Dem So Thang")
month=int(input("Nhap vao 1 Thang"))
if month in (1,3,5,7,8,10,12):
    print(" Thang co 31 Ngay ")
elif month in (4,6,9,11):
   print(" Thang co 30 Ngay")
elif month == 2:
    year=int(input(" Moi Ban Nhap Nam"))
    if(year %4 and year %100!=0)or year %400==0:
           print("Thang",month,"co 29 ngay")
    else:
         print("Thang",month,"co 28 ngay")
else:
  print("Thang",month,"Khong hop le")


