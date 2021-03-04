from ..util.file_manager import FileManager
from .scanner import Scanner

class LexicalAnalyzer:
  
  def __init__(self):
    self.files = FileManager.readFiles()
    self.scanner = Scanner()
    self.tokens = []
    self.errors = []
  
  def startAnalysis(self):
    for file in self.files:
      self.scanner.content = file['content']
      while True:
        token = self.scanner.getToken()
        if token == None:
          break
        else:
          self.__addToken(token)

    for token in self.tokens:
      print(f'{token["term"]} {token["type"]}')

  def __addToken(self, token):
    self.tokens.append({
      'type': token['type'],
      'term': token['term']
    })
    
  def __addErros():
    pass