def maghsom(num):
    counter = 0
    for i in range(1, num+1):
        if num % i == 0:
            counter = counter + 1

    return counter

chap = 0
Bigest_maghsom = 0
Bigest_num = 0
num = 0

for i in range(0,20):
    num = int(input())
    chap = maghsom(num)
    if chap > Bigest_maghsom:
        Bigest_maghsom = chap
        Bigest_num = num
    elif chap == Bigest_maghsom and num > Bigest_num:
        Bigest_num = num





print(Bigest_num , Bigest_maghsom)




