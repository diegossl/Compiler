from .definition.types import (ARI_TK, BLO_TK, DEL_TK, DIG_TK, IDE_TK, LET_TK, LIN_TK, LOG_TK,
  NUN_TK, REL_TK, RES_TK, STR_TK)
from .comparator import Comparator
import re

class Scanner:

  def __init__(self):
    self.comparator = Comparator()
    self.content = None
    self.position = 0
    self.term = None
    self.state = 0
 
  def getToken(self):
    if self.__isEndFile():
      return None

    self.state = 0
      
    while True:
      currentChar = self.content[self.position]

      if self.state == 0:
        if self.comparator.isDelimiter(currentChar):
          self.term = currentChar
          self.state = 25
      elif self.state == 25:
        return { 'type': DEL_TK, 'term': self.term }
      else:
        return { 'type': None, 'term': None }

      self.position += 1

  def __currentChar(self):
    currentChar = self.content[self.position]
    self.position += 1
    return currentChar

  def __isEndFile(self):
    return self.position == len(self.content) - 1
  
  def __back(self):
    self.position -= 1