def selectionSort(Mylist):
   for fillslot in range(len(alist)-1, 0, -1):
       positionOfMax = 0
       for location in range(1, fillslot+1):
           if Mylist[location]> Mylist[positionOfMax]:
               positionOfMax = location

       temp = alist[fillslot]
       Mylist[fillslot] = Mylist[positionOfMax]
       Mylist[positionOfMax] = temp

Mylist = [45,62,39,15,77,31,43,55,20]
selectionSort(Mylist)
print(Mylist)
