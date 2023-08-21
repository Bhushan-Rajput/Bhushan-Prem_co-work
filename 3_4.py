string = input()
new_string = string.replace("iiing", "th")
if len(string)<=300:
    print(new_string)
else:
    print("limit exceed")
