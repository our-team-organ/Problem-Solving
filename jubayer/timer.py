import time

h = int(input("Enter hours: "))
m = int(input("Enter minutes: "))
s = int(input("Enter seconds: "))

total_seconds = (h * 3600) + (m * 60) + s

while total_seconds >= 0:
    mins, secs = divmod(total_seconds, 60)
    hours, mins = divmod(mins, 60)
    
    timer = f"{hours:02d}:{mins:02d}:{secs:02d}"
    print(f"\rTime Remaining: {timer}", end="")
    
    time.sleep(1)
    total_seconds -= 1

print("\nTime's up! Finished.")