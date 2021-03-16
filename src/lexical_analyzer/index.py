from ..util.file_manager import FileManager
from .scanner import Scanner

class LexicalAnalyzer:
  
  def __init__(self):
    self.scanner = Scanner()
  
  def startAnalysis(self):
    tokensByFile = []

    for fileNumber, file in enumerate(FileManager.readFiles()):
      self.scanner.code = file['fileContent']
      fileName = file['fileName']
      print(f'INPUT: {fileName}')
      tokens = []
      errors = []

      for error in self.scanner.scanErrors():
        errors.append(error)
      for token in self.scanner.scanTokens():
        tokens.append(token)

      tokensByFile.append({ 'file': fileName, 'tokens': tokens })
      FileManager.writeFile(fileNumber, tokens, errors)

      if len(errors) > 0:
        print(f'OUTPUT: {len(errors)} lexical errors were found\n')
      else:
        print(f'OUTPUT: Successfully completed! {len(tokens)} leximes were found\n')
        
    return tokensByFile
