#作業1.1
#把99乘法表包裝成函式，可做成nxn 乘法
#def list(n1,n2):
def list(n1=10,n2=10):
    for n1 in range(1,10):
        for n2 in range(1,10):
            print(n1,"*",n2,"=",n1*n2)
#1.2把四則運算幾包裝成函式
def count(n1,n2,op):  
    if op=="+":
        print(n1+n2)
    elif op=="-":
        print(n1-n2)
    elif op=="*":
        print(n1*n2)
    elif op=="/":
        print(n1/n2)
    else :
        print("不支援的運算")