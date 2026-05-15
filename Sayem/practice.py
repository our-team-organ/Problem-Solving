import random
random=random.randint(1,20)
for i in range(5):
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