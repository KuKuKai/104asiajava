import math
print("請輸入4個數字")
a=eval(input())
b=eval(input())
c=eval(input())
d=eval(input())
e=math.sqrt((a-c)**2+(b-d)**2)
print('(',a,',',b,')')
print('(',c,',',d,')')
print("Distance = %.4f"%e)