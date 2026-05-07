import time

hr = int(input("Enter Time (Hr): "))
mnt = int(input("Enter Time (Mnt): "))
sec = int(input("Enter Time (Sec): "))

total_time = (hr * 60 * 60) + (mnt * 60) + sec

while (total_time > 0):
    hr = total_time // 3600
    mnt = (total_time % 3600) // 60
    sec = total_time % 60
    
    print(f"Hr: {hr:02d} Mnt: {mnt:02d} Sec: {sec:02d}")
    
    total_time -= 1
    
    time.sleep(1)
    
if(total_time == 0):
    print("Finished!")