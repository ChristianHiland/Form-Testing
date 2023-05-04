# Importing Modules
import json
import time
import platform

File = "Data/InfoEN.json"

# Writing To The JSON.
def Write(FamilyName, FamilySize, FamilyDied, UserName1, UserName2, Email, DOB, Version):
    # Other Varables
    # Time
    DateTime = time.ctime()
    # Platform Info
    Platform = platform.system()
    VersionPlat = platform.version()
    HostName = platform.node()
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
            "Name": "InfoJSON",
            "Version": Version,
            "About": "This is a simple program that tought me how to use a JSON file."
        },
        "System": {
            "Platform": Platform,
            "Version": VersionPlat,
            "Hostname": HostName
        },
    }
    # Writing to the JSON.
    with open(File, "w") as write_file:
        json.dump(Info, write_file, indent=4)
# Defines, to print the info out.
def FamilyPrint():
    with open(File) as read:
        # Geting The Data
        data = json.load(read)
        print("\nDisplaying Family Info")
        print("\nFamily Name: " + data['Family']['Name'])
        print("Family Size: " + data['Family']['Size'])
        print("Family Dead: " + data['Family']['Died'])
    return
def UserPrint():
    with open(File) as read:
        # Geting The Data
        data = json.load(read)
        print("\nDisplaying User Info")
        print("\nFirst Name: " + data['User']['FirstName'])
        print("Last Name: " + data['User']['LastName'])
        print("Email: " + data['User']['Email'])
        print("DOB: " + data['User']['DOB'])
    return
def FilePrint():
    with open(File) as read:
        # Geting The Data
        data = json.load(read)
        print("\nDisplaying File Info")
        print("\nDate Made: " + data['File']['DateMade'])
    return
def ProgramPrint():
    with open(File) as read:
        # Geting The Data
        data = json.load(read)
        print("\nDisplaying Program Info")
        print("\nName: " + data['Program']['Name'])
        print("Version: " + data['Program']['Version'])
        print("About: " + data['Program']['About'])
    return
def SystemPrint():
    with open(File) as read:
        # Geting The Data
        data = json.load(read)
        print("\nDisplaying System Info\n")
        print("\Platform: " + data['System']['Platform'])
        print("OS Version: " + data['System']['Version'])
        print("HostName: " + data['System']['Hostname'])
    return
# Reading the JSON
def Read():
    # Reading The JSON File, and Printing It Out.
    with open(File) as read_file:
        # Geting The Data
        data = json.load(read_file)
        Output = json.dumps(data, indent=4, separators=(',', ': '), sort_keys=True)
        # Printing the User's options
        Option = input("Want one data entry? [Y/N] ")
        if Option.lower() == str("n"):
            # Displaying the whole thing.
            print("\nDisplaying Info.json\n")
            print(Output)
        else:
            # Letting the user pick a catgory
            print("\nHere are the options:\n1.Family Info\n2.User Info.\n3. File Info\n4. Program Info\n5. System Info")
            OptionPrint = input("Option Number: ")
            if OptionPrint == str("1"):
                # Printing Family Info
                FamilyPrint()
            elif OptionPrint == str("2"):
                # Printing User Info
                UserPrint()
            elif OptionPrint == str("3"):
                # Printing File Info
                FilePrint()
            elif OptionPrint == str("4"):
                # Printing Program Info
                ProgramPrint()
            elif OptionPrint.lower() == str("5"):
                SystemPrint()
            else:
                print("Oops you may have pressed wrong.")
