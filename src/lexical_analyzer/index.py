from ..util.file_manager import FileManager
from .scanner import Scanner

class LexicalAnalyzer:
  
  def __init__(self):
    self.scanner = Scanner()
  
  def startAnalysis(self):
    for index, file in enumerate(FileManager.readFiles()):
      data = []
      for token in self.scanner.tokenize(file['content']):
        data.append(token)
      FileManager.writeFile(index, data)