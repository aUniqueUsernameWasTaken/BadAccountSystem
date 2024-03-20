import hashlib
import os


def saveaccount(username, password):
    encryptedpassword = hashlib.sha256(password).hexdigest()
    record = open("accounts/"+hashlib.sha256(username).hexdigest()+".user", 'w')
    record.write(encryptedpassword)


def loadaccount(username, password):
    #doesaccountmatch = False
    try:
        with open("accounts/"+hashlib.sha256(username).hexdigest()+".user") as f:
            filecontents = f.read()
            fencrypt = hashlib.sha256(password).hexdigest()
            if fencrypt == filecontents:
                return True
            else:
                return False
    except:
        pass