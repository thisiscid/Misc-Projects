import getpass
from utils.logger import log
from auth.password_utils import verify_hash_and_salt
from utils.storage import load_user

def login():
    users_and_passes = load_user()
    attempts = 0
    while True:
        while attempts < 3:
            user=input("Username: ")
            password=getpass.getpass()
            if user not in users_and_passes:
                print("Username or password did not match our records. Please try again.")
                attempts+=1; log(f"User attempted try {attempts} and failed")
                continue
            matches_hash_and_salt=verify_hash_and_salt(user,password,users_and_passes)
            if users_and_passes.get(user)==None:
                print("Username or password did not match our records. Please try again.")
                attempts+=1; log(f"User attempted try {attempts} and failed")
                continue
            elif not matches_hash_and_salt:
                print("Username or password did not match our records. Please try again.")
                attempts+=1; log(f"User attempted try {attempts} and failed")
                continue
            elif matches_hash_and_salt:
                print(f"Welcome to APP {user}")
                log(f"{user.title()} logged in!")
                return True
        print("Too many tries.")
        log(f'User attempted try {attempts} and hit attempt limit.')
        return False