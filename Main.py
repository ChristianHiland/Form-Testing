import json
from English import EN
from Korean import KO
from os import path, system
from tqdm import tqdm
import time
import platform

# Paths To Files.
LanguageJSON = "Data/UserLANG.json"
PlatformOS = platform.system()
# Installing Modules
with open(LanguageJSON) as Info:
    Data = json.load(Info)
    if Data['Ran'].lower() == str("no"):
        system("pip install -r requirements.txt")
        system("pip install --upgrade pip")

# 'Loading' 
for i in tqdm (range (100), desc="Loading InfoJSON", ascii=False, ncols=75):
    time.sleep(0.01)
print("Complete.")
if PlatformOS.lower() == str("linux"):
    system("clear")

# Checking The Language Settings.
with open(LanguageJSON) as languagePicked:
    Data = json.load(languagePicked)
    # Check for Language in UserLANG.JSON
    if Data['Language'] != str("Not Set"):
        # Gets the Language in the JSON, and uses that
            if Data['Language'].lower() == str("en"):
                EN.Run()
            elif Data['Language'].lower() == str("ko"):
                KO.Run()
with open(LanguageJSON) as languagePicked:
    Data = json.load(languagePicked)
    if Data['Language'].lower() == str("not set"):
        # This will make a JSON file with the user's language, if it hasn't been made yet.
        print("ENGLISH: KO or EN\n한국어: KO 또는 EN")
        language = input("KO/EN: ")
        # The Data Layout.
        data = {
            "Language": language,
            "Ran": "Ran"
        }
        # Writing to the JSON file.
        with open(LanguageJSON, "w") as LanguageAdd:
            json.dump(data, LanguageAdd, indent=4)
        if language.lower() == str("en"):
            EN.Run()
        elif language.lower() == str("ko"):
            KO.Run()