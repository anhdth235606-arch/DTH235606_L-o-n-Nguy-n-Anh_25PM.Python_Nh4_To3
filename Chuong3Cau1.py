print("kiem tra nam nhuan")
year=int(input("Moi nhap nam :"))
if(year %4 and year %100!=0)or year %400==0:
  print("Nam",year ,"la nam nhuan")
else:
    print("Nam",year,"khong phai la nam nhuan")
