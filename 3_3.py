correct_str= input("Enter Correct String: ").upper()
content_str= input("Enter Contestant String: ").upper()
count=0
size=len(content_str)
if size<=10 and size==len(correct_str):
    for i in correct_str:
        for j in content_str:
            if i==j:
                count+=1
if count==size:
    print(content_str,"IS CORRECT")
elif count>=size-2:
    print(content_str,"IS ALMOST CORRECT")
      
else:
    print(content_str,"IS WRONG")