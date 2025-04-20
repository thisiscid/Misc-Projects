import getpass
import utils.logger
import auth.password_utils
import utils.storage
import os
def create_user():
    while True:
        user=input("User: ")
        password=getpass.getpass()
        confirmpassword=getpass.getpass("Confirm: ")
        if password != confirmpassword:
            os.system('clear')
            print("Passwords didn't match \n")
            continue
        if not auth.password_utils.is_strong_password(password):
            utils.logger.log("User failed password check.")
            os.system('clear')
            print("Password was not strong enough. Try again. \n"); continue
        users_and_passes=utils.storage.load_user()
        if user in users_and_passes:
            utils.logger.log("User attempted to create already existant user.")
            os.system('clear')
            print("User already exists"); continue
        if password == confirmpassword:
            hashed=auth.password_utils.hash_and_salt(password)
            hashed_value, salt=hashed.split(':')
            utils.storage.save_user(user, f"{hashed_value}:{salt}")
            print("User successfully created. \n")
            break
