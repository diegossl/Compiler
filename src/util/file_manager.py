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
      firstColumnTabs = None
      secondColumnTabs = None
      for token in tokens:
        firstColumnTabs = '\t\t\t' if token.tokenLine <= 9 else '\t\t'
        secondColumnTabs = '\t\t'
        file.write(f'{token.tokenLine}{firstColumnTabs}{token.tokenType}{secondColumnTabs}{token.tokenValue}\n')
      file.write('\nList of errors\n\n')
      for error in errors:
        firstColumnTabs = '\t\t\t' if error.tokenLine <= 9 else '\t\t'
        secondColumnTabs = '\t\t\t' if len(error.tokenType) < 4 else '\t\t'
        file.write(f'{error.tokenLine}{firstColumnTabs}{error.tokenType}{secondColumnTabs}{error.tokenValue}\n')