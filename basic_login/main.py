from auth import login, signup
from utils import logger, storage
import sys

def menu():
    while True:
        choice=input("Simple Login Manager \n 1: Login \n 2: Sign up \n 3: Exit")
        if int(choice)==1:
            login.login()
        if int(choice)==2:
            signup.create_user()
        if int(choice)==3:
            print("Goodbye.")
            logger.log("Exiting application.")
            sys.exit()
if __name__ == "__main__":
    menu()
# To implement, call menu() and customize as needed