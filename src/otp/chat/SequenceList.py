from otp.settings import Settings

class SequenceList:

    def __init__(self, filePath):
        self.list = Settings.Settings(filePath)

    def getList(self, word):
        if word in self.list:
            return self.list[word]
        else:
            return []