import random

x = 1
y = 99
Guess = random.randint(x, y)
print("our Guess was", Guess)
javab = input("is our answer correct?(s=smaller , b=bigger , r=right )")
while javab != 'r':
    if javab == "s":
        y = Guess - 1
        Guess = random.randint(x, y)
        print("our smaller Guess was", Guess)
        javab = input("is our answer correct?(s , b , r )")
    elif javab == "b":
        x = Guess + 1
        Guess = random.randint(x, y)
        print("our bigger Guess was", Guess)
        javab = input("is our answer correct?(s , b , r )")
    else:
        break

print("yeessss correct")

