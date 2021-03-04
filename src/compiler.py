from .lexical_analyzer.index import LexicalAnalyzer

class Compiler:

  def __init__(self):
    self.lexicalAnalyzer = LexicalAnalyzer()
  
  def run(self):
    self.lexicalAnalyzer.startAnalysis()
