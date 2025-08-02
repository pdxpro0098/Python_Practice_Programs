email = input("Enter you Email Address: ")

def extractUsername(email):
    username = ""
    for ch in email:
        if(ch == '@'):
            break
        username += ch
    return f"Username: {username}"
        
print(extractUsername(email))
