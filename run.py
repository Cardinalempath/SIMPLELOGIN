def hash_password(password):
    hashed_password = ''
    for i in range(len(password)):
        if i % 2 == 1:  
            hashed_password += '#'
        else:
            hashed_password += password[i]
    return hashed_password

def details():
    name = input("Enter your name: ")
    surname = input("Enter your Surname: ")
    email = input("Enter your email: ")

    return name, surname, email

def access():
    entered_password = input("Enter password: ")
    reentered_password = input("Re-Enter password: ")

    
    hashed_entered_password = hash_password(entered_password)
    hashed_reentered_password = hash_password(reentered_password)

  
    if hashed_entered_password == hashed_reentered_password:
        print("Passwords match.")
    else:
        print("Passwords do not match.")

# Get user details
name, surname, email = details()

# Print user details
print("Name:", name)
print("Surname:", surname)
print("Email:", email)

# Access the system
access()
