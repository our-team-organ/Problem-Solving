#16. Write a program to take a number N and print numbers from 1 to N.
n=int(input("Enter a number: "))
for i in range(1,n+1):
    print(i,end="")

#17. Reverse Printing .Print numbers from N to 1.
n=int(input("Enter a number: "))
for i in range(n,0,-1):
    print(i,end="")

#18.  Sum of N Numbers Calculate sum of first N numbers.
n=int(input("Enter a number: "))
sum=0
for i in range(0,n+1):
        sum+=i
print(sum)

#19.Find factorial of a number using loop. 
n = int(input("Enter a number: "))
fact = 1
for i in range(1, n+1):
    fact*= i
print(fact)

#20. Print multiplication table of a number.
n = int(input("Enter a number: "))

for i in range(1, 11):
    print(n*i)
#21. Count total digits in a number.
n=input("Enter number:")
length=len(n)
print(length)