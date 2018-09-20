def mergeSort(Mylist):
    print("Splitting ",Mylist)
    if len(Mylist)>1:
        mid = len(Mylist)//2
        lefthalf = Mylist[:mid]
        righthalf = Mylist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                Mylist[k]=lefthalf[i]
                i=i+1
            else:
                Mylist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            Mylist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            Mylist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",Mylist)

Mylist = [24,46,39,97,77,31,74,55,10]
mergeSort(Mylist)
print(Mylist)
