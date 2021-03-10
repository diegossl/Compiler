from ..util.file_manager import FileManager
from .scanner import Scanner

class LexicalAnalyzer:
  
  def __init__(self):
    self.scanner = Scanner()
  
  def startAnalysis(self):
    for fileNumber, file in enumerate(FileManager.readFiles()):
      tokens = []
      errors = []
      for error in self.scanner.scanErrors(file['content']):
        errors.append(error)
      for token in self.scanner.scanTokens(file['content']):
        tokens.append(token)
      FileManager.writeFile(fileNumber, tokens, errors)