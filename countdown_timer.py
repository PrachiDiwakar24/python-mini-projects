# Countdown Timer

import time

def countdown(seconds):

    while seconds > 0:
        minutes, secs = divmod(seconds, 60)

        timer = f"{minutes:02d}:{secs:02d}"
        print(timer, end="\r", flush=True)

        time.sleep(1)
        seconds -= 1

    print("00:00")
    print("Time's up! Countdown completed.")

print("=== Countdown Timer ===")

try:

    minutes = int(input("Enter minutes: "))
    seconds = int(input("Enter seconds: "))

    if minutes < 0 or not 0 <= seconds < 60:
        print("Please enter valid time.")

    elif minutes == 0 and seconds == 0:
        print("Please enter a time greater than zero.")

    else:
        total_seconds = minutes * 60 + seconds
        countdown(total_seconds)

except ValueError:
    
    print("Please enter numbers only.")