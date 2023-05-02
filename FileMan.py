# 모듈 가져오기.
# Importing Modules
import json
import time
import platform

# JSON에 쓰기.
# Writing To The JSON.
def Write(FamilyName, FamilySize, FamilyDied, UserName1, UserName2, Email, DOB, Version):
    # 기타 변수
    # Other Varables

    # 시간
    # Time
    DateTime = time.ctime()
    # 플랫폼 정보
    # Platform Info
    Platform = platform.platform()
    VersionPlat = platform.version()
    # JSON 문자열에 입력된 데이터
    # The data put into a JSON string.
    Info = {
        "Family": {
            "Name": FamilyName,
            "Size": FamilySize,
            "Died": FamilyDied
        },
        "User": {
            "FirstName": UserName1,
            "LastName": UserName2,
            "Email": Email,
            "DOB": DOB
        },
        "File": {
            "DateMade": DateTime
        },
        "Program": {
            "Version": Version,
            "About": "This is a simple program that tought me how to use a JSON file."
        },
        "System": {
            "Platform": Platform,
            "Version": VersionPlat
        },
    }
    # JSON에 쓰기.
    # Writing to the JSON.
    with open("Info.json", "w") as write_file:
        json.dump(Info, write_file, indent=4)

# 정보를 출력하도록 정의합니다.
# Defines, to print the info out.
def FamilyPrint():
    with open("Info.json") as read:
        # 데이터 얻기
        # Geting The Data
        data = json.load(read)
        print("\nDisplaying Family Info")
        print("\nFamily Name: " + data['Family']['Name'])
        print("Family Size: " + data['Family']['Size'])
        print("Family Dead: " + data['Family']['Died'])
    return
def UserPrint():
    with open("Info.json") as read:
        # 데이터 얻기
        # Geting The Data
        data = json.load(read)
        print("\nDisplaying User Info")
        print("\nFirst Name: " + data['User']['FirstName'])
        print("Last Name: " + data['User']['LastName'])
        print("Email: " + data['User']['Email'])
        print("DOB: " + data['User']['DOB'])
    return
def FilePrint():
    with open("Info.json") as read:
        # 데이터 얻기
        # Geting The Data
        data = json.load(read)
        print("\nDisplaying File Info")
        print("\nDate Made: " + data['File']['DateMade'])
    return
def ProgramPrint():
    with open("Info.json") as read:
        # 데이터 얻기
        # Geting The Data
        data = json.load(read)
        print("\nDisplaying Program Info")
        print("\nVersion: " + data['Program']['Version'])
        print("About: " + data['Program']['About'])
    return
def SystemPrint():
    with open("Info.json") as read:
        # 데이터 얻기
        # Geting The Data
        data = json.load(read)
        print("\nDisplaying System Info\n")
        print("\Platform: " + data['System']['Platform'])
        print("OS Version: " + data['System']['Version'])
    return

# JSON을 읽는다.
def Read():
    # JSON 파일을 읽고 출력합니다.
    # Reading The JSON File, and Printing It Out.
    with open("Info.json") as read_file:
        # 데이터 얻기
        # Geting The Data
        data = json.load(read_file)
        Output = json.dumps(data, indent=4, separators=(',', ': '), sort_keys=True)
        # 사용자 옵션 출력
        # Printing the User's options
        Option = input("Want one data entry? [Y/N] ")
        if Option.lower() == str("n"):
            # 전체를 표시합니다.
            # Displaying the whole thing.
            print("\nDisplaying Info.json\n")
            print(Output)
        else:
            # 사용자가 카테고리를 선택하게 하기
            # Letting the user pick a catgory
            print("\nHere are the options:\n1.Family Info\n2.User Info.\n3. File Info\n4. Program Info\n5. System Info")
            OptionPrint = input("Option Number: ")
            if OptionPrint == str("1"):
                # 가족 정보 인쇄
                # Printing Family Info
                FamilyPrint()
            elif OptionPrint == str("2"):
                # 사용자 정보 인쇄
                # Printing User Info
                UserPrint()
            elif OptionPrint == str("3"):
                # 파일 정보 출력하기
                # Printing File Info
                FilePrint()
            elif OptionPrint == str("4"):
                # 프로그램 정보 인쇄
                # Printing Program Info
                ProgramPrint()
            elif OptionPrint.lower() == str("5"):
                SystemPrint()
            else:
                print("Oops you may have pressed wrong.")
