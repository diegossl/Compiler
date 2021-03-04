from os.path import isfile, join
from os import listdir

class FileManager:

  @staticmethod
  def readFiles():
    filePath = 'input'
    fileData = []

    for fileName in listdir(filePath):
      if isfile(join(filePath, fileName)):
        with open(join(filePath, fileName), 'r') as content:
          text = content.read()
          fileData.append({
            'fileName': fileName,
            'content': text
          })
          
    return fileData

  @staticmethod
  def writeFiles(data):
    pass