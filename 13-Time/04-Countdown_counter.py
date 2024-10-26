import time

c_or_r = input("Press 'C' for counter or press 'R' for reverse counter:\n").lower()

if c_or_r == 'c':
        my_time = int(input("⌚Enter the time in seconds:\t"))
        print("..........Counter is on..............")
        for count in range(1, my_time+1):
            print(count)
            time.sleep(1)
        print("Time is up!")

elif c_or_r == 'r':
        print("..........Reverse Counter is on..............")

        my_time2 = int(input("⌚Enter the time in seconds:\t"))

        for count in reversed(range(1, my_time2+1)):
            print(count)
            time.sleep(1)
        print("Time is up!")
