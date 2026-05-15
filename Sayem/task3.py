#31. Prime Number Check. 
n = int(input("Enter a number: "))
if n<2:
    print("Not Prime")
else:
    for i in range(2, n):
        if n%i==0:
            print("Not Prime")
            break
    else:
        print("Prime")

#32. Print All Prime Numbers (1 to N).
n = int(input("Enter a number: "))

for num in range(2, n+1):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num, end=" ")    # ← print if prime
#33. GCD (Greatest Common Divisor).

#34. LCM (Least Common Multiple). 

#35. Perfect Number. 

#36. Strong Number. 

#37. Binary to Decimal.
 
#38. Decimal to Binary.

#39. Menu Driven Calculator

#40. Login System (3 Attempts)
password = 1234
time = 3
while time > 0:
    n = int(input("Enter password: "))
    if password == n:
        print("Login successful")
        break
    else:
        time -= 1
        print(f"Wrong! {time} attempts remaining")

if time == 0:
    print("Account locked!")

#41. Guessing Game (3 Attempts)
import random
random=random.randint(1,20)
for i in range(3):
    n=int(input("Enter number:"))
    if random==n:
        print("You Win")
        break
    else:
        if(random>n):
            print("You loss, Enter a higher number")
        elif(random<n):
          print("You loss,Enter a lower number")

print("The random number is:",random)

#42. Digit Frequency

#43. Second Largest (3 Numbers)

#44. Sum of Even Numbers (1 to N)
evensum=0
n=int(input("Enter a number:"))
for i in range(0,n+1):
    if(i%2==0):
        evensum+=i
print("Sum of even:",evensum)


#45. Pattern Printing ⭐
n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()

n = int(input())
for i in range(n, 0, -1):
    for j in range(1, i+1):
        print(j, end="")
    print()


#Strong password
password = input("Enter password: ")

has_upper=False
has_lower=False
has_digit=False
has_special=False

for i in password:
    if i.isupper():
        has_upper=True
    elif i.islower():
        has_lower=True
    elif i.isdigit():
        has_digit=True
    else:
        has_special=True     

if has_upper and has_lower and has_digit and has_special and len(password) >= 8:
    print("Strong password ")
else:
    print("Weak password ")
    
    if not has_upper:
        print("— Add uppercase letter (A-Z)")
    if not has_lower:
        print("— Add lowercase letter (a-z)")
    if not has_digit:
        print("— Add a number (0-9)")
    if not has_special:
        print("— Add special character (!@#$...)")
    if len(password) < 8:
        print("— Minimum 8 characters required")
