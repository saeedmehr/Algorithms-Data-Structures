name = input().lower()
for i in name:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        name = name.replace( i , "")

print ('.' + '.'.join(name))


