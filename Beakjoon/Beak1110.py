Num = int(input())
a=Num
b=0
c=0
while b==0 or a != Num:
    c=Num//10 + Num%10
    Num = (Num%10)*10 + c%10
    b+=1
print(b)