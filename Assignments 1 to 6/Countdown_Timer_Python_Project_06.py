import time 

def countdown(t):
    print("⏳ Countdown Timer Started! ⏳")
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}: {:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print("Timer Complted!")

t = int(input("Enter the time un second: "))

countdown(t)