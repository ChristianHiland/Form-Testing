# Importing Modules.
import json
import os
import platform
from English import FileMan

def Run():
    # Version Number
    Version = 0.2

    # Letting the user chouse an option.
    Option = input("\nRead or Write? ")
    # Checking the option
    if Option.lower() == str("read"):
        # Reading the JSON.
        FileMan.Read()
    elif Option.lower() == str("write"):
        # Asking The Questions.
        FamilyName = input("What is your family name? ")
        FamilySize = input("How many people is in your family? ")
        FamilyDied = input("How many of them has died in your life? ")
        if platform.system.lower() == str("linux"):
            os.system('clear')
        UserName1 = input("What is your first name? ")
        UserName2 = input("What is your last name? ")
        Email = input("What is your Email? ")
        DOB = input("What is your date of birth? ")
        # Writing to the JSON.
        FileMan.Write(FamilyName, FamilySize, FamilyDied, UserName1, UserName2, Email, DOB, Version)