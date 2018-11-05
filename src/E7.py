str = input().lower()
l = len(str)
p = l-1
index = 0
while index < p:
    if str[index] == str[p]:
        index = index + 1
        p = p-1
        if index == p or index + 1 == p:
            print("palindrome")
    else:
        print("not palindrome")
        break


# this in another way to do it
#string_to_check = input("Enter a string").lower()

#if string_to_check == string_to_check[::-1]:
#    print("This is a palindrome")
#else:
#    print("This is not a palindrome")
