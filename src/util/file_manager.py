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
          fileData.append({ 'content': text, 'fileName': fileName })
    return fileData

  @staticmethod
  def writeFile(fileNumber, tokens, errors):
    filePath = 'output'
    with open(join(filePath, f'saida{fileNumber + 1}.txt'), 'w+') as file:
      file.write('List of tokens\n\n')
      for token in tokens:
        file.write(f'{token.tokenLine} {token.tokenType} {token.tokenValue}\n')
      file.write('\nList of errors\n\n')
      for error in errors:
        file.write(f'{error.tokenLine} {error.tokenType} {error.tokenValue}\n')