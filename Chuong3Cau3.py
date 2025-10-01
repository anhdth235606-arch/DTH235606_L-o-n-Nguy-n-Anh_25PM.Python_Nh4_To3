from math import sqrt
print ("Phuong Trinh Bac 2")
a=float(input("Nhap vao so a"))
b=float(input("Nhap vao so b"))
c=float(input("Nhap vao so c"))
if a==0:
    print("Phuong Trinh Co Mot Nghiem")
    if b==0 and c==0:
     print("Phuong Trinh Co Vo So Nghiem")
    if b==0 and c!=0:
       print("Phuong Trinh Vo Nghiem")
    else:
       x=-c/b
       print("Nghiem X:",x)
else:
   delta=b**2-4*a*c
if delta<0:
     print(" Phuong Trinh Vo Nghiem")
elif delta==0:
 x=-b/(2*a)
 print("Phuong Trinh Co Nghiem Kep x1,x2",x)
else:
 print(" Phuong Trinh Co Hai Nghiem Phan Biet")
x1=(-b-sqrt(delta))/(2*a)
x2=(-b+sqrt(delta))/(2*a)
print("x1",x1)
print("x2",x2)


