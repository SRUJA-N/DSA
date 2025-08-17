def print4(n):
    for i in range(n, 0,-1):
        print("*"*i)
def print6(n):
    for i in range(1,n+1):
        for j in range(1,n-i+1+1):
            print(j,end="")
        print()
def print7(n):
    for i in range(0,n):
        for j in range(0,n-i-1):
            print(" ",end="")
        for k in range(i*2+1):
            print("*",end="")
        for l in range(0,n-i-1):
            print(" ",end="")
        print()
def print8(n):
    for i in range(0, n):
        for j in range(0,i):
            print(" ",end="")
        for k in range((n*2)-1-(2*i)):
            print("*",end="")
        for l in range(0,i):
            print(" ",end="")
        print()
def print9(n):
    for i in range(0,n):
        for j in range(0,n-i-1):
            print(" ",end="")
        for k in range(i*2+1):
            print("*",end="")
        for l in range(0,n-i-1):
            print(" ",end="")
        print()
    for i in range(0, n):
        for j in range(0,i):
            print(" ",end="")
        for k in range((n*2)-1-(2*i)):
            print("*",end="")
        for l in range(0,i):
            print(" ",end="")
        print()
def print10(n):
    for i in range(1,n+1):
        print("*"*i)
    for i in range(n-1,0,-1):
        print("*" * i)

def print11(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            if((i+j)%2==0):
                print("1",end="")
            if((i+j)%2!=0):
                print("0", end="")
        print()
        """hard"""
def print12(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end="")
        for k in range((n-1)*2):
            print("-",end="")
        n=n-1
        for l in range(i,0,-1):
            print(l, end="")
        print()

def print13(n):
    num=1
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(f" {num}",end="")
            num=num+1
        print()

def print14(n):
    for i in range(1,n+1):
        for j in range(n):
            print(chr(65+j),end="")
        n=n-1
        print()
def print15(n):
    for i in range(1,n+1):
        for j in range(i):
            print(chr(65+j),end="")
        print()

def print16(n):
    for i in range(0, n + 1):
        for j in range(i):
            print(chr(64+i),end="")
        print()
def print17(n):
    num=1
    for i in range(1,n+1):
        b=(2 * i)/2 - 1
        w=chr(64)
        for j in range(n-i):
            print("-",end="")
        for k in range((2*i)-1):
            if(k<b):
               print(w+num,end="")
               num=num+1
            else:
                print(w+num,end="")
                num=num-1


        for j in range(n-i):
            print("-",end="")
        print()
print17(5)



