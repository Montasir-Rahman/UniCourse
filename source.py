def credentials ():
    username = "admin"
    password = "Admin2025!"
    return username, password
    
def check_credentials(user_name, pass_word):
    username, password = credentials()
    
    if user_name == username and pass_word == password:
        return True
    else: 
        return False

username = input("Enter username: ")
password = input("Enter password: ")
verification = check_credentials(username, password)

if verification == True:
    print("Login Successful!")
else:
    print("Login failed!!!")

