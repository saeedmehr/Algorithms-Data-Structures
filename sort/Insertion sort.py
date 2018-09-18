def insertionSort(Mylist):
   for index in range(1,len(Mylist)):

     currentvalue = Mylist[index]
     position = index

     while position>0 and Mylist[position-1]>currentvalue:
         Mylist[position]=Mylist[position-1]
         position = position-1

     Mylist[position]=currentvalue

Mylist = [45,62,28,23,97,77,31,44,55,20]
insertionSort(Mylist)
print(Mylist)
