from io import TextIOWrapper
import os
import re

class EnvParser:
    filename = ".env"
    exampleFile = ".env.example"

    def __init__(self, filename=None, exampleFile=None) -> None:
        self.filename = filename or self.filename
        self.exampleFile = exampleFile or self.exampleFile

    def loadFile(self, file) -> TextIOWrapper | None:
        if os.path.exists(file):
            return open(file, 'r')
        return None

    def getKeys(self, data):
        keys = []
        regex_pattern = r"^([a-zA-Z_]*)="
        lines = data.split("\n")
        
        for line in lines:
            key = line.strip()
            if key != "":
                match = re.match(regex_pattern, key)
                print(match)
                if match is not None:
                    keys.append(match.group(0))
        
        print(keys)
        return keys
        # return re.findall(regex_pattern, data)

    def parseEnvs(self):
        file = self.loadFile(self.filename)
        if file is not None and file.readable():
            data = file.read()
            return self.getKeys(data)
        return []

    def parseExampleEnvs(self):
        file = self.loadFile(self.exampleFile)
        if file is not None and file.readable():
            data = file.read()
            return self.getKeys(data)
        return []

    def saveEnvs(self):
        envKeys = self.parseEnvs()
        exampleKeys = self.parseExampleEnvs()

        diffKeys = []

        # print(exampleKeys)
        # return

        for key in envKeys:
            if key not in exampleKeys:
                # print(f"{key} - absent")
                diffKeys.append(key)

        with open(self.exampleFile, 'a+') as file:
            for key in diffKeys:
                file.write(f"{key}\n")
