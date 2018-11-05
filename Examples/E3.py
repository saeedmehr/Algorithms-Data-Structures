sen = 0
Big1 = 0
Big2 = 0

while sen != -1:
    sen = int(input())
    if sen > Big1:
        Big2 = Big1
        Big1 = sen

print(Big1,Big2)
