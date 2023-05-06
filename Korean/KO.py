# 모듈 가져오기.
import json
import os
import platform
from Korean import FileManKO

def Run():
    # 버전 번호
    Version = 0.2
    # 사용자가 옵션을 선택하도록 합니다.
    Option = input("읽기 또는 쓰기? ")
    # 옵션 확인
    if Option == str("읽기"):
        # JSON을 읽는다.
        FileManKO.Read()
    elif Option == str("쓰기"):
        # 질문하기.
        FamilyName = input("가족의 이름은 무엇입니까? ")
        FamilySize = input("가족이 몇 명입니까? ")
        FamilyDied = input("당신의 삶에서 그들 중 얼마나 많은 사람들이 죽었습니까? ")
        if platform.system.lower() == str("linux"):
            os.system('clear')
        UserName1 = input("당신의 이름은 무엇인가? ")
        UserName2 = input("성은 무엇입니까? ")
        Email = input("당신의 이메일은 무엇인가요? ")
        DOB = input("당신의 생년월일은 무엇입니까? ")
        # JSON에 쓰기.
        FileManKO.Write(FamilyName, FamilySize, FamilyDied, UserName1, UserName2, Email, DOB, Version)