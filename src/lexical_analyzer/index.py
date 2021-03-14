from ..util.file_manager import FileManager
from .scanner import Scanner

class LexicalAnalyzer:
  
  def __init__(self):
    self.scanner = Scanner()
  
  def startAnalysis(self):
    for fileNumber, file in enumerate(FileManager.readFiles()):
      fileName = file['fileName']
      print(f'INPUT: {fileName}')
      tokens = []
      errors = []
      for token in self.scanner.scanTokens(file['content']):
        tokens.append(token)
      for error in self.scanner.scanErrors(file['content']):
        errors.append(error)
      FileManager.writeFile(fileNumber, tokens, errors)
      if len(errors) > 0:
        print(f'OUTPUT: {len(errors)} lexical errors were found\n')
      else:
        print(f'OUTPUT: Successfully completed! {len(tokens)} leximes were found\n')
