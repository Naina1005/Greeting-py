#This is a python program which greets the user according to the current time

import time
timestamp = time.strftime("%H:%M:%S")
print("current time is ", timestamp)

hr = time.strftime("%H")
print("Hours:",hr)

min = time.strftime("%M")
print("Minutes:",min)

sec = time.strftime("%S")
print("Seconds:",sec)

#main logic
if(0 <= int(hr) <12 ):
    print("Good morning")

elif(12 <= int(hr) <16 ):
    print("Good Afternoon")

elif(16 <= int(hr) <21 ):
    print("Good Evening")

elif(21 <= int(hr) <24):
    print("Good Night")

else:
    print("Invalid time ")