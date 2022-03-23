import math

print("Wellcom to Check Prime Number Program")

while True:
    n = int(input("Please Enter You'r Number: "))
    if n<=1:
        print("please enter valid number")
    else:
        break

i=2
prime=True;
while i<=math.floor(math.sqrt(n)):
    if n==2:
        break;
    elif n%i==0:
        prime=False;
        break;
    else:
        i+=1

if prime==True:
    print("You'r number is prime!")
else:
    print("You'r number is not prime!")

