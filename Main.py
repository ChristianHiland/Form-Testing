# 모듈 가져오기.
# Importing Modules.
import json
import os
import FileMan

# 버전 번호
# Version Number
Version = 0.2

# 사용자가 옵션을 선택하도록 합니다.
# Letting the user chouse an option.
Option = input("\nRead or Write? ")

# 옵션 확인
# Checking the option
if Option.lower() == str("read"):
    # JSON을 읽는다.
    # Reading the JSON.
    FileMan.Read()
elif Option.lower() == str("write"):
    # 질문하기.
    # Asking The Questions.
    FamilyName = input("What is your family name? ")
    FamilySize = input("How many people is in your family? ")
    FamilyDied = input("How many of them has died in your life? ")
    os.system('clear')
    UserName1 = input("What is your frist name? ")
    UserName2 = input("What is your last name? ")
    Email = input("What is your Email? ")
    DOB = input("What is your date of birth? ")
    # JSON에 쓰기.
    # Writing to the JSON.
    FileMan.Write(FamilyName, FamilySize, FamilyDied, UserName1, UserName2, Email, DOB, Version)