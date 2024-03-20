import accounthandler

print('Server Log in <plz forgive me for the stupidity of this>\n')
loggedin = False
def loginrequest(username, password):
    if accounthandler.loadaccount(username, password) == True:
        return True
    else:
        return False
    
def signuprequest(username, password):
    accounthandler.saveaccount(username, password)


def validaccount(boolean):
    if boolean == True:
        print("You are now logged in!!")
        loggedin = True
    elif boolean == False:
        print("Please try again!")
    else:
        print(str(boolean))


#while loggedin == False:
if (input('Login or sign up? [L/S]\n>').lower()) == 's':
    print("Signing Up!\n")
    signuprequest(input("Enter your username: ").encode('utf-8'), input("Enter your password: ").encode('utf-8'))
    print('Account Created!')

else:
    print("Loging in!\n")
    validaccount(loginrequest(input("Enter your username: ").encode('utf-8'), input("Enter your password: ").encode('utf-8')))


