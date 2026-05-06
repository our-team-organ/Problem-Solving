# # # # # # # # # # # # # # # 1.Num Classify
# # # # # # # # # # # # # # # num=int(input("Enter a number:"))
# # # # # # # # # # # # # # # if n>0:
# # # # # # # # # # # # # # #     print("positive")
# # # # # # # # # # # # # # # elif n<0:
# # # # # # # # # # # # # # #     print("Negative")
# # # # # # # # # # # # # # # else :
# # # # # # # # # # # # # # #     print("Zero")       

# # # # # # # # # # # # # # 2.Even/Odd
# # # # # # # # # # # # # # num=int(input("Enter a number:"))
# # # # # # # # # # # # # # if n%2==0:
# # # # # # # # # # # # # #     print("Even")
# # # # # # # # # # # # # # else:
# # # # # # # # # # # # # #     print("Odd")

# # # # # # # # # # # # # 3.Max of 2
# # # # # # # # # # # # # a = int(input("Enter a first number:"))
# # # # # # # # # # # # # b = int(input("Enter a second number:"))
            
# # # # # # # # # # # # # if a>b:
# # # # # # # # # # # # #     print("a is Maximum")
# # # # # # # # # # # # # elif b>a:
# # # # # # # # # # # # #     print("b is maximum")
# # # # # # # # # # # # # else:
# # # # # # # # # # # # #     # print("equal")

# # # # # # # # # # # # 4.max of 3
# # # # # # # # # # # # a = int(input("Enter a first number:"))
# # # # # # # # # # # # b = int(input("Enter a second number:"))
# # # # # # # # # # # # c = int(input("Enter a third number:"))

# # # # # # # # # # # # if a>=b and a>=c:
# # # # # # # # # # # #     print("a is maximum")
# # # # # # # # # # # # elife b>=a and b>=c:
# # # # # # # # # # # #     print("b is the maximum")
# # # # # # # # # # # # else:
# # # # # # # # # # # #     print("c is the maximum")

# # # # # # # # # # # 5.Grading system
# # # # # # # # # # # marks = int(input("Enter a marks:"))

# # # # # # # # # # # if >= 80:
# # # # # # # # # # #     print("A")
# # # # # # # # # # # elif >= 70:
# # # # # # # # # # #     print("B")
# # # # # # # # # # # elif >= 60:
# # # # # # # # # # #     printI("C")
# # # # # # # # # # # elif >= 50:
# # # # # # # # # # #     print("D")
# # # # # # # # # # # else:
# # # # # # # # # # #     print("Fail")

# # # # # # # # # # 6.Leap year
# # # # # # # # # # year = int(input("Enter a year:"))

# # # # # # # # # # if (year % 4==0 and year % 100!=0) or (year % 400==0):
# # # # # # # # # #     print("Leap year")
# # # # # # # # # # else:
# # # # # # # # # #     print("Not")

# # # # # # # # # # 7.Divisibility
# # # # # # # # # # num =int(input("Enter a number:"))

# # # # # # # # # # if num % 5==0 and num % 11==0:
# # # # # # # # # #     print("Divisible by 5 & 11")
# # # # # # # # # # else:
# # # # # # # # # #     print("Not Divisible")

# # # # # # # # # # 8.Vowel/Consonant
# # # # # # # # # # ch =int(input("Enter a character:"))
# # # # # # # # # # if ch in "aeiouAEIOU"
# # # # # # # # # #     print("Vowel")
# # # # # # # # # # else:
# # # # # # # # # #     print("Consonant")

# # # # # # # # # # 9.Case Detect
# # # # # # # # # # ch =int(input("Enter a character:"))
# # # # # # # # # # if ch>='A' and ch>='Z' :
# # # # # # # # # #     print("uppercase")
# # # # # # # # # # elif ch>='a' and ch>='z' :
# # # # # # # # # #     print("lowercase")
# # # # # # # # # # else:
# # # # # # # # # #     print("Invalid Character")

# # # # # # # # # # 10.profit/Loss
# # # # # # # # # # cp = float(input("Enter cost price:"))
# # # # # # # # # # sp = float(input("Enter selling price:"))

# # # # # # # # # # if sp>cp:
# # # # # # # # # #     print("profit")
# # # # # # # # # # elif cp>sp:
# # # # # # # # # #     print("Loss")
# # # # # # # # # # else:
# # # # # # # # # #     print("No profit No Loss")

# # # # # # # # # 11.Temperature
# # # # # # # # # temp =int(input("Enter a temperature:"))
# # # # # # # # # if temp >=30:
# # # # # # # # #     print("Hot")
# # # # # # # # # else:
# # # # # # # # #     print("Cold")

# # # # # # # # # 12.Electricity bill 
# # # # # # # # # unit = int(input("Enter a electricity units:"))
# # # # # # # # # if units <=100:
# # # # # # # # #     bill = units * 5
# # # # # # # # # else: 
# # # # # # # # #     bill =(100 * 5)+((units - 100)* 10)
# # # # # # # # #     print("Electricity bill=", bill)

# # # # # # # # # 13.Triangle validity
# # # # # # # # # a =int(input("Enter a first side:"))
# # # # # # # # # b =int(input("Enter a second side"))
# # # # # # # # # c =int(inputI("Enter a third side:"))
# # # # # # # # # if a+b>c and a+c>b and b+c>a:
# # # # # # # # #     print("Valid triangle")
# # # # # # # # # else:
# # # # # # # # #     print("Invalid Triangle")


# # # # # # # # # 14.Simple calculator
# # # # # # # # # a =float(input("Enter a first number:"))
# # # # # # # # # op =input("Enter operator(+,-,*,/):")
# # # # # # # # # b =float(input("Enter a second number:"))

# # # # # # # # # if op =='+':
# # # # # # # # #     print("Result=", a+b)
# # # # # # # # # elif op =='-':
# # # # # # # # #     print("Result=", a-b)
# # # # # # # # # elif op=='*':
# # # # # # # # #     print("Result=", a*b)
# # # # # # # # # elif op=='/':
# # # # # # # # #     if b!=0:
# # # # # # # # #         print("Result=", a/b)
# # # # # # # # #     else:
# # # # # # # # #         print("Division by zero not possible")
# # # # # # # # # else:
# # # # # # # # #     print("Invalid operator")

# # # # # # # # 15. Pass or Fail 
# # # # # # # # marks = int(input("Enter marks:"))
# # # # # # # # attendance = float(input("Enter attendance:"))
# # # # # # # # if marks>=40 and attendance >=75:
# # # # # # # #     print("Pass")
# # # # # # # # else:
# # # # # # # #     print("Fail")


# # # # # # # 16.
# # # # # # # n = int(input("Enter N:"))
# # # # # # # for i in range (1, n+1):
# # # # # # #     print(i, end=" ")

# # # # # # # 17. 
# # # # # # # n = int(input("Enter N:"))
# # # # # # # for i in range(n, 0, -1):
# # # # # # #     print(i, end" ")

# # # # # # # 18. 
# # # # # # # n = int(input("Enter N:"))
# # # # # # # total = 0
# # # # # # # for i in range(1, n+1):
# # # # # # #     total +=i
# # # # # # # print(total)

# # # # # # # 19. 
# # # # # # # n = int(input("Enter N"))
# # # # # # # result = 1
# # # # # # # for i in range(1, n+1)
# # # # # # #     result *= i
# # # # # # # print(result)

# # # # # # # 20.
# # # # # # # n =int(input("Enter N:"))
# # # # # # # for i in range(1, 11):
# # # # # # #     print(n*i, end=" ")

# # # # # # 21.
# # # # # # n = input("Enter number:")
# # # # # # print(len(n.replace("-", " ")))

# # # # # # # 22.
# # # # # # # n =input("Enter number:")
# # # # # # # print(int(n[::-1]))

# # # # # 23. 
# # # # # n = input("Enter number:")
# # # # # if n==n[::-1]:
# # # # #     print("palindrome")
# # # # # else:
# # # # #     print("Not pallindrome")


# # # # 24.n =input("Enter number:")
# # # # print(sum(int(d)for d in n))

# # # # 25.
# # # # n = input("Enter number:")
# # # # result = 1
# # # # for d in n:
# # # #     result *= int(d)
# # # #     print(result)

# # # # 26.
# # # # n = input("Enter number:")
# # # # if sum(int(d)**3 for d in n)== int(n):
# # # #     print("armstrong")
# # # # else:
# # # #     print("Not")

# # # # 27. 
# # # # n = int(input("Enter N:"))
# # # # a, b=0,1
# # # # for i in range(n):
# # # #     print(a, end=" ")
# # # #     a, b=b, a+b

# # # # 28. 
# # # # n =input("Enter number:")
# # # # even = sum(1 for d in n if int(d)% 2==0)
# # # # odd = sum(1 for d in n if int(d)% 2 != 0)
# # # # print(f"Even:{even} Odd:{odd}")


# # # # 29. 
# # # # n = input("Enter number:")
# # # # print(max(int(d) for d in n))

# # # # 30. 
# # # # a = int(input("Enter base:"))
# # # # b = int(input("Enter exponent:"))
# # # # result = 1
# # # # for i in range(b):
# # # #     result *=a
# # # # print(result)

# # # 31. 
# # # a = int(input("Enter number:"))
# # # if n<2:
# # #     print("Not prime")
# # # else:
# # #     is_prime = True
# # #     for i in range(2, int(n**0.5)+1):
# # #         if n % i==0:
# # #             is_prime = False
# # #             break
# # #     print("prime" if is_prime else "Not prime")

# # # 32.
# # # n = int(input("Enter N:"))
# # # for num in range(2, n+1):
# # #     is_prime = True
# # #     for i in range(2, int(n**0.5)+1):
# # #         if n % i==0:
# # #             is_prime = False
# # #             break
# # #         if is_prime:
# # #     print(num, end=" ")

# # # 33. 
# # # a = int(input("Enter first number:"))
# # # b = int(input("Enter second number:"))
# # # x, y=y, x%y
# # # print(x)

# # # 34. 
# # # a = int(input("Enter first number:"))
# # # b = int(input("Enter second number:"))
# # # x, y = a, b
# # # while y:
# # #     x, y=y, x%y
# # # print((a * b) // x)

# # # 35. 
# # # n = int(input("Enter first number:"))
# # # total = sum(i for i in range(1, n) if n%i == 0)
# # # print("perfect" if total == n else "Not perfect")

# # # 36. 
# # # n = input("Enter number")
# # # total = 0
# # # for d in n:
# # #     fact = 1
# # #     for i in range(1, int(d)+1):
# # #         fact *= i
# # #         total += fact
# # # print("stong" if total == int(n) else "Not strong")

# # # 37. 
# # # b = input("Enter binary:")
# # # decimal = 0
# # # for digit in b:
# # #     decimal = decimal * 2 + int(digit)
# # # print(decimal)

# # # 38. 
# # # n = int(input("Enter decimal:"))
# # # binary = "" 
# # # while n>0:
# # #     binary = str(n % 2) + binary
# # #     n //= 2
# # # print(binary)

# # 39. 
# # while True:
# #     print("\n1. Add 2. Suntrct 3. Multiply 4. Divide 5. Exit")
# #     choice = int(input("choice:"))
# #     if choice == 5:
# #         print("Exit")
# #         break
# #     a = float(input("Enter first number:"))
# #     b = float(input("Enter second number:"))
# #     if choice == 1:
# #         print(a + b)
# #     elif choice == 2:
# #         print(a - b)
# #     elif choice == 3:
# #         print(a * b)
# #     elif choice == 4:
# #         print(a/b if b!=0 else "cannot drive by zero")


# 40.
# password ="1234"
# for attempt in range(3):
#     p = input("Enter password:")
#     if p == password:
#         print("Login success")
#         break
#     else:
#         print("Account Blocked")

# 41.
# secret = 7
# for attempt in range(3):
#     guess = int(input("Guess(1-10):"))
#     if guess == secret:
#         print("you win")
#     elif guess<secret:
#         print("Try higer")
#     else:
#         print("Try lower")
# else:
#     print("You lose")

# 42.
# n =input("Enter number:")
# d =input("Enter digit to find:")
# print(n.count(d))          

# 43.
# nums = sorted([int(input(f"Enter number {i+1}:")) for i in range(3)])
# print(nums[1])

# 44.
# n = int(input("Enter N:"))
# print(sum( i for i in range(1, n+1) if i % 2 == 0))

# 45.
# n = int(input("Enter rows:"))
# for i in range(1, n+1):
#     print("*" * i)