#Extract emails from text file

import re

with open("email_input.txt","r") as file1:
    content1=file1.read()

emails=re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",content1)
emails=list(set(emails))

with open("only_email.txt","w") as file2:
    for email in emails:
        file2.write(email+"\n")

with open("only_email.txt","r") as file3:
    content2=file3.read()
    print(content2)
    
print("\nFile created successfully")
