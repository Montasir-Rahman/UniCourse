def admin_credentials():
    admin_username = "admin"
    admin_password = "Admin2025!"
    return admin_username, admin_password

def verify_credentials(cred1, cred2):
    org_user, org_pass = admin_credentials()
    if cred1 == org_user and cred2 == org_pass:
        return True
    else:
        return False

input_username = input("Enter Username: ")
input_password = input("Enter Password: ")
verification = verify_credentials(input_username, input_password)

if verification == True:
    print("Login Successful!")
else: 
    print("Login failed!!!")