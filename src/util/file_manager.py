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
    tabs = '\t'
    with open(join(filePath, f'saida{fileNumber + 1}.txt'), 'w+') as file:
      file.write('List of tokens (lines, tokens, lexemes):\n\n')
      for token in tokens:
        line = f'0{token.tokenLine}' if token.tokenLine <= 9 else token.tokenLine
        file.write(f'{line}{tabs}{token.tokenType}{tabs}{token.tokenValue}\n')
      file.write('\nList of errors (lines, tokens, lexical errors):\n\n')
      if len(errors) > 0:
        for error in errors:
          line = f'0{error.tokenLine}' if error.tokenLine <= 9 else error.tokenLine
          file.write(f'{line}{tabs}{error.tokenType}{tabs}{error.tokenValue}\n')
      else:
        file.write('No lexical errors')