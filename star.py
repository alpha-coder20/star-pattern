import time

print("***Star Pattern Generator***")
row = int(input("Enter number of rows: "))
boole = int(input("Enter Boolean (0 or 1): "))
if boole == 1:
    for i in range(row):
        print("*"*(i+1))
else:
    for i in range(row):
        print("*"*(row-i))

time.sleep(5)