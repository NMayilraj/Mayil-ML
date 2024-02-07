username = input("Please enter your username: ")

  
valid_users = ["user1", "user2", "user3"]  
valid_passwords = ["pass1", "pass2", "pass3"]  


valid_usersA = ["user1A", "user2S", "user3S"]  
valid_passwordsB = ["pass1", "pass2", "pass3"]  

MegasUser =[valid_users, valid_usersA]
MegaPassword = [valid_passwords, valid_passwordsB]

  
def login_module(userNM, VU, VP):
    print(userNM)
    if userNM not in VU:
        print("Invalid Username")
    else:
        Password = input("Please enter your password: ")
        if userNM in VU and Password == VP[VU.index(username)]:  
            print("Login successful!")   
        else:  
            print("Invalid Password.") 



# login_module(username, valid_users, valid_passwords)
# login_module(username, valid_usersA, valid_passwordsB)

for i in range(len(MegasUser)):
    login_module(username, MegasUser[i], MegaPassword[i])