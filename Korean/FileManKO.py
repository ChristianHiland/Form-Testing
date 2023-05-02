# 모듈 가져오기.
import json
import time
import platform

File = "Data/InfoKO.json"

# JSON에 쓰기.
def Write(FamilyName, FamilySize, FamilyDied, UserName1, UserName2, Email, DOB, Version):
    # 기타 변수
    # 시간
    DateTime = time.ctime()
    # 플랫폼 정보
    Platform = platform.system()
    VersionPlat = platform.version()
    # JSON 문자열에 입력된 데이터
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
            "About": "JSON 파일을 사용하는 방법을 가르쳐준 간단한 프로그램입니다."
        },
        "System": {
            "Platform": Platform,
            "Version": VersionPlat,
            "Hostname": HostName
        },
    }
    # JSON에 쓰기.
    with open(File, "w") as write_file:
        json.dump(Info, write_file, indent=4)
# 정보를 출력하도록 정의합니다.
def FamilyPrint():
    with open(File) as read:
        # 데이터 얻기
        data = json.load(read)
        print("\n가족 정보 표시")
        print("\n성: " + data['Family']['Name'])
        print("가족 규모: " + data['Family']['Size'])
        print("죽은 가족: " + data['Family']['Died'])
    return
def UserPrint():
    with open(File) as read:
        # 데이터 얻기
        data = json.load(read)
        print("\n사용자 정보 인쇄")
        print("\n이름: " + data['User']['FirstName'])
        print("성: " + data['User']['LastName'])
        print("이메일: " + data['User']['Email'])
        print("생년월일: " + data['User']['DOB'])  
    return
def FilePrint():
    with open(File) as read:
        # 데이터 얻기
        data = json.load(read)
        print("\n파일 정보 출력하기")
        print("\n만든 날짜: " + data['File']['DateMade'])
    return
def ProgramPrint():
    with open(File) as read:
        # 데이터 얻기
        data = json.load(read)
        print("\n프로그램 정보 인쇄")
        print("\n버전: " + data['Program']['Version'])
        print("소개: " + data['Program']['About'])
    return
def SystemPrint():
    with open(File) as read:
        # 데이터 얻기
        data = json.load(read)
        print("\n시스템 정보 표시\n")
        print("\플랫폼: " + data['System']['Platform'])
        print("OS 버전: " + data['System']['Version'])
        print("호스트 이름: " + data['System']['Hostname'])
    return
# JSON을 읽는다.
def Read():
    # JSON 파일을 읽고 출력합니다.
    with open(File) as read_file:
        # 데이터 얻기
        data = json.load(read_file)
        Output = json.dumps(data, indent=4, separators=(',', ': '), sort_keys=True)
        # 사용자 옵션 출력
        Option = input("하나의 데이터 항목을 원하십니까? [예/아니요] ")
        if Option == str("아니요"):
            # 전체를 표시합니다.
            print("\nInfo.json을 표시하는 중\n")
            print(Output)
        else:
            # 사용자가 카테고리를 선택하게 하
            print("\n옵션은 다음과 같습니다.\n1.가족 정보\n2.사용자 정보\n3. 파일 정보\n4. 프로그램 정보\n5. 시스템 정보")
            OptionPrint = input("O옵션 번호: ")
            if OptionPrint == str("1"):
                # 가족 정보 인쇄
                FamilyPrint()
            elif OptionPrint == str("2"):
                # 사용자 정보 인쇄
                UserPrint()
            elif OptionPrint == str("3"):
                # 파일 정보 출력하기
                FilePrint()
            elif OptionPrint == str("4"):
                # 프로그램 정보 인쇄
                ProgramPrint()
            elif OptionPrint.lower() == str("5"):
                SystemPrint()
            else:
                print("앗 잘못 눌리셨나보네요. :)")
