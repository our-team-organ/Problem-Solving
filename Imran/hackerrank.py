# print("Hello, World!")


# n = int(input().strip())

# if (n % 2 != 0):
#     print("Weird")

# elif n % 2 == 0 and 2 <= n <= 5:
#     print("Not Weird")

# elif n % 2 == 0 and 6 <= n <= 20:
#     print("Weird")

# else:
#     print("Not Weird")



# n = int(input())
# n1 = int(input())

# sum = n + n1
# dif = n - n1
# pro = n * n1

# print(sum)
# print(dif)
# print(pro)



# a = int(input())
# a1 = int(input())

# div = a // a1
# fdiv = a / a1

# print(div)
# print(float(fdiv))





# n = int(input())

# for i in range(0, n):
#     print(i*i)



# def is_leap(year):

#     if year % 400 == 0:
#         return True

#     elif year % 100 == 0:
#         return False

#     elif year % 4 == 0:
#         return True

#     else:
#         return False


# year = int(input())
# print(is_leap(year))



# n = int(input())
# for i in range(1, n+1):
#     print(i, end="")




# import re

# s = input()
# k = input()

# found = False

# for i in range(len(s)):
    
#     m = re.match(k, s[i:])
    
#     if m:
#         print((i, i + len(k) - 1))
#         found = True

# if not found:
#     print((-1, -1))




# import re
# n = int(input())

# for _ in range(n):
#     line = input()
    
#     line = re.sub(r'(?<= )&&(?= )', 'and', line)
#     line = re.sub(r'(?<= )\|\|(?= )', 'or', line)

#     print(line)



# n = int(input())
# scores = list(map(int, input().split()))

# u_s = sorted(set(scores))
# u_s.sort()

# print(u_s[-2])