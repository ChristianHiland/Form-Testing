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
# 'Loading' 
for i in tqdm (range (100), desc="Loading InfoJSON", ascii=False, ncols=75):
    time.sleep(0.02)
print("Complete.")
if PlatformOS.lower() == str("linux"):
    system("clear")

# Check for Language in UserLANG.JSON
if path.isfile(LanguageJSON) == True:
    # Gets the Language in the JSON, and uses that
    with open(LanguageJSON) as languagePicked:
        Data = json.load(languagePicked)
        if Data['Language'].lower() == str("en"):
            EN.Run()
        elif Data['Language'].lower() == str("ko"):
            KO.Run()
else:
    # This will make a JSON file with the user's language, if it hasn't been made yet.
    print("ENGLISH: KO or EN\n한국어: KO 또는 EN")
    language = input("KO/EN: ")
    # The Data Layout.
    data = {
        "Language": language
    }
    # Writing to the JSON file.
    with open(LanguageJSON, "w") as LanguageAdd:
        json.dump(data, LanguageAdd, indent=4)
    if language.lower() == str("en"):
        EN.Run()
    elif language.lower() == str("ko"):
        KO.Run()