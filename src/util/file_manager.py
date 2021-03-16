from os.path import isfile, join
from os import listdir

class FileManager:

  @staticmethod
  def readFiles():
    filePath = 'input'
    fileContent = []
    for fileName in listdir(filePath):
      if isfile(join(filePath, fileName)):
        with open(join(filePath, fileName), 'r') as file:
          text = file.read()
          fileContent.append({ 'fileContent': text, 'fileName': fileName })
    return fileContent

  @staticmethod
  def writeFile(fileNumber, tokens, errors):
    filePath = 'output'
    with open(join(filePath, f'saida{fileNumber + 1}.txt'), 'w+') as file:
      file.write('List of tokens (lines, tokens, lexemes):\n\n')
      firstColumnTabs = None
      secondColumnTabs = None
      for token in tokens:
        firstColumnTabs = '\t\t' if token.tokenLine <= 9 else '\t'
        secondColumnTabs = '\t'
        file.write(f'{token.tokenLine}{firstColumnTabs}{token.tokenType}{secondColumnTabs}{token.tokenValue}\n')
      file.write('\nList of errors (lines, tokens, lexical errors):\n\n')
      if len(errors) > 0:
        for error in errors:
          firstColumnTabs = '\t\t' if error.tokenLine <= 9 else '\t'
          secondColumnTabs = '\t\t' if len(error.tokenType) < 4 else '\t'
          file.write(f'{error.tokenLine}{firstColumnTabs}{error.tokenType}{secondColumnTabs}{error.tokenValue}\n')
      else:
        file.write('No lexical errors')