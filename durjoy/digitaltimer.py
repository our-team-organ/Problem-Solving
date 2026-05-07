import time
desire_time=int(input("enter your time in seconds: "))
for second in range(desire_time,0,-1):
    seconds = second % 60
    minits = int(second/60)%60
    hours = int(second/3600)
    print(f"{hours:02}:{minits:02}:{seconds:02}")
    time.sleep(1)

print("times up motherfuckers")