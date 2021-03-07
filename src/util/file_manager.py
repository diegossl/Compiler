from os.path import isfile, join
from os import listdir

class FileManager:

  @staticmethod
  def readFiles():
    filePath = 'input'
    fileData = []

    for fileName in listdir(filePath):
      if isfile(join(filePath, fileName)):
        with open(join(filePath, fileName), 'r') as file:
          text = file.read()
          fileData.append({ 'content': text })
          
    return fileData

  @staticmethod
  def writeFile(fileNumber, data):
    filePath = 'output'

    with open(join(filePath, f'saida{fileNumber + 1}.txt'), 'w+') as file:
      file.write('Token List\n\n')
      for token in data:
        file.write(f'{token.tokenLine} {token.tokenType} {token.tokenValue}\n')