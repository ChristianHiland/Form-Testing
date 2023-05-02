import json
import English
import Korean

language = input("KO or EN: ")

if language.lower() == str("en"):
    English.MainEN.Run()
else:
    Korean.FileManKO.Run()