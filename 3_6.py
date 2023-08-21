string1=input("Enter the input string\n")
str2=[]
new_str=string1.split()
for i in new_str:
    if i==new_str[0]:
        str2.append(i)
        continue
    str2.append(i.upper())
print("The processed string is",' '.join(str2)) 