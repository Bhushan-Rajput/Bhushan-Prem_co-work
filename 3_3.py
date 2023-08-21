correct_str= input("Enter Correct String: ").upper()
content_str= input("Enter Contestant String: ").upper()
count=0
if len(content_str)<=10 and len(content_str)==len(correct_str):
    for i in correct_str:
        for j in content_str:
            if i==j:
                count+=1
if count==len(content_str):
    print(content_str,"IS CORRECT")
elif count==len(content_str)-2:
    print(content_str,"IS ALMOST CORRECT")
else:
    print(content_str,"IS WRONG")