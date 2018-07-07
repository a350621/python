print("功課1")
n1=int(input("Enter a Number:"))
n2=int(input("Enter a Number:"))
op=input("運算：+,-,*,/:")
if op=="+":
    print(n1+n2)
elif op=="-":
    print(n1-n2)
elif op=="*":
    print(n1*n2)
elif op=="/":
    print(n1/n2)
else :
    prinr("不支援的運算")
print("==========")

print("功課2")
n=int(input("輸入一個正整數"))
#算出整數平方根 9=>3,25=>5,8=>沒有
for i in range(n):
    if n==i*i:
        print(i)
        break
else:
    print("沒有整數平方根")

print("==========")

print("功課3 99乘法表")
for i in range(1,10):
    for j in range(1,10):
        print(i,"*",j,"=",i*j)
