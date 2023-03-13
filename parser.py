import json
import sys
import os

import requests

if len(sys.argv) != 2:
    print("USAGE python parser.py [inputFileName]")

url: str = "https://raw.githubusercontent.com/pichsenmeister/WienerScript/master/keywords.json"

page = requests.get(url)
parsedObject = {value: key for key, value in json.loads(page.text).items()}
filePath = "{0}{1}{2}".format(os.getcwd(), os.path.sep, sys.argv[1])

with open(filePath, "r") as source_file:
    content = source_file.read()

contentAsWords = content.split(" ")
newContent = []

for word in contentAsWords:
    newContent.append(word)
    for key, value in parsedObject.items():
        if key == word:
            newContent[len(newContent) - 1] = word.replace(word, value)

content = " ".join(newContent)

with open("{0}.ws".format(sys.argv[1]), "w") as output_file:
    output_file.write(content)
