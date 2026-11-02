a = int(input(" nhap so: "))
def kiemtra(n):
    if n >2:
        for i in range(2,a+1):
           
            if n %i ==0:
                return 0 
            return 1
    else:
        return 0


if kiemtra(a):
    print("so nguyn to")
else: 
    print(" ko")
