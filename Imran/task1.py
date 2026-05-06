# Number 1
n=int(input())
print("Positive" if n>=0 else "Negative")

# Number 2
n=int(input())
print("Even" if n%2==0 else "Odd")

# Number 3
a,b=map(int,input().split())
if a>b: print(a)
elif b>a: print(b)
else: print("Equal")

# Number 4
a,b,c=map(int,input().split())
print(max(a,b,c))

# Number 5
m=int(input())
if m>=80: print("A")
elif m>=70: print("B")
elif m>=60: print("C")
elif m>=50: print("D")
else: print("Fail")

# Number 6
y=int(input())
print("Leap Year" if (y%4==0 and y%100!=0) or y%400==0 else "Not")

# Number 7
n=int(input())
print("Divisible" if n%5==0 and n%11==0 else "Not")

# Number 8
c=input()
print("Vowel" if c.lower() in "aeiou" else "Consonant")

# Number 9
c=input()
print("Uppercase" if c.isupper() else "Lowercase")

# Number 10
cp,sp=map(int,input().split())
if sp>cp: print("Profit")
elif sp<cp: print("Loss")
else: print("No Profit No Loss")

# Number 11
t=int(input())
print("Hot" if t>30 else "Cold")

# Number 12
u=int(input())
bill = u*5 if u<=100 else 100*5+(u-100)*10
print(bill)

# Number 13
a,b,c=map(int,input().split())
print("Valid" if a+b>c and a+c>b and b+c>a else "Invalid")

# Number 14
a,op,b=input().split()
a=int(a); b=int(b)
if op=='+': print(a+b)
elif op=='-': print(a-b)
elif op=='*': print(a*b)
elif op=='/': print(a/b)

# Number 15
marks,att=map(int,input().split())
print("Pass" if marks>=40 and att>=75 else "Fail")

# Number 16
n=int(input())
for i in range(1,n+1): print(i,end=" ")

# Number 17
n=int(input())
for i in range(n,0,-1): print(i,end=" ")

# Number 18
n=int(input())
print(sum(range(1,n+1)))

# Number 19
n=int(input())
f=1
for i in range(1,n+1): f*=i
print(f)

# Number 20
n=int(input())
for i in range(1,11): print(n*i,end=" ")

# Number 21
n=input()
print(len(n))

# Number 22
n=input()
print(int(n[::-1]))

# Number 23
n=input()
print("Palindrome" if n==n[::-1] else "Not Palindrome")

# Number 24
n=input()
print(sum(int(i) for i in n))

# Number 25
n=input()
p=1
for i in n: p*=int(i)
print(p)

# Number 26
n=input()
s=sum(int(i)**3 for i in n)
print("Armstrong" if s==int(n) else "Not")

# Number 27
n=int(input())
a,b=0,1
for i in range(n):
    print(a,end=" ")
    a,b=b,a+b

# Number 28
n=input()
e=o=0
for i in n:
    if int(i)%2==0: e+=1
    else: o+=1
print("Even:",e,"Odd:",o)

# Number 29
n=input()
print(max(n))

# Number 30
a,b=map(int,input().split())
print(a**b)

# Number 31
n=int(input())
if n<2: print("Not Prime")
else:
    for i in range(2,n):
        if n%i==0:
            print("Not Prime")
            break
    else: print("Prime")

# Number 32
n=int(input())
for num in range(2,n+1):
    for i in range(2,num):
        if num%i==0: break
    else: print(num,end=" ")

# Number 33
a,b=map(int,input().split())
while b:
    a,b=b,a%b
print(a)

# Number 34
a,b=map(int,input().split())
x,y=a,b
while y:
    x,y=y,x%y
print((a*b)//x)

# Number 35
n=int(input())
s=sum(i for i in range(1,n) if n%i==0)
print("Perfect" if s==n else "Not Perfect")

# Number 36
import math
n=input()
s=sum(math.factorial(int(i)) for i in n)
print("Strong" if s==int(n) else "Not Strong")

# Number 37
b=input()
print(int(b,2))

# Number 38
d=int(input())
print(bin(d)[2:])

# Number 39
while True:
    ch=int(input())
    if ch==5: break
    a,b=map(int,input().split())
    if ch==1: print(a+b)
    elif ch==2: print(a-b)
    elif ch==3: print(a*b)
    elif ch==4: print(a/b)

# Number 40
correct="1234"
for i in range(3):
    p=input()
    if p==correct:
        print("Login Success")
        break
else:
    print("Account Blocked")

# Number 41
import random
num=random.randint(1,10)
for i in range(3):
    g=int(input())
    if g==num:
        print("You Win")
        break
    elif g>num: print("Too High")
    else: print("Too Low")
else:
    print("You Lose")

# Number 42
n=input()
d=input()
print(n.count(d))

# Number 43
a=list(map(int,input().split()))
a.sort()
print(a[1])

# Number 44
n=int(input())
print(sum(i for i in range(1,n+1) if i%2==0))

# Number 45
n=int(input())
for i in range(1,n+1):
    print("*"*i)
    
    
    
    
    
# Number 46
s=input()
print(sum(1 for c in s if c.lower() in "aeiou"))

# Number 47
s=input()
print("Palindrome" if s==s[::-1] else "Not")

# Number 48
s=input()
print(len(s.split()))

# Number 49
s=input()
print(sum(1 for c in s if c.isupper()))

# Number 50
s=input()
print(s.replace(" ",""))

# Number 51
lst=list(map(int,input().split()))
print(max(lst))

# Number 52
lst=list(map(int,input().split()))
print(sum(lst))

# Number 53
lst=list(map(int,input().split()))
print([i for i in lst if i%2==0])

# Number 54
lst=list(map(int,input().split()))
print(list(set(lst)))

# Number 55
lst=list(map(int,input().split()))
print(lst[::-1])

# Number 56
t=tuple(map(int,input().split()))
x=int(input())
print(t.count(x))

# Number 57
t=tuple(map(int,input().split()))
print(max(t),min(t))

# Number 58
t=tuple(map(int,input().split()))
print(list(t))

# Number 59
t=tuple(map(int,input().split()))
x=int(input())
print(t.index(x))

# Number 60
t=tuple(map(int,input().split()))
print(t[:3])

# Number 61
d={"a":10,"b":20}
for k,v in d.items(): print(k,v)

# Number 62
d={"a":10,"b":20}
k=input()
print("Yes" if k in d else "No")

# Number 63
d={"a":10,"b":20}
print(sum(d.values()))

# Number 64
d={"a":10,"b":20}
d["a"]=50
print(d)

# Number 65
d={"a":10,"b":20}
for i in d: print(i,d[i])

# Number 66
def f(n): return "Even" if n%2==0 else "Odd"
print(f(int(input())))

# Number 67
def f(a,b): return a+b
a,b=map(int,input().split())
print(f(a,b))

# Number 68
def f(a,b,c): return max(a,b,c)
a,b,c=map(int,input().split())
print(f(a,b,c))

# Number 69
def f(n):
    r=1
    for i in range(1,n+1): r*=i
    return r
print(f(int(input())))

# Number 70
def f(s): return s[::-1]
print(f(input()))