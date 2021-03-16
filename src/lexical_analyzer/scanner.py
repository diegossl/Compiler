from .constants.types import NRO_TK, IDE_TK, PRE_TK, BCM_TK, LCM_TK, NWL_TK, SKP_TK, CAD_TK, SIB_TK, CMF_TK
from .constants.lexical import RESERVED_WORDS, LINE_COMMENT, BLOCK_COMMENT
from .constants.map import TOKEN_MAP, ERROR_TOKEN_MAP
from .token import Token
import re as regex

class Scanner:

  def __init__(self):
    self.code = None

  def scanErrors(self):
    superErrorRegex = '|'.join('(?P<%s>%s)' % pair for pair in ERROR_TOKEN_MAP)
    charactersToRemove = []
    lineNum = 1
    lineStart = 0

    for matches in regex.finditer(superErrorRegex, self.code, regex.MULTILINE):
      groupType = matches.lastgroup
      value = matches.group()

      if groupType == SIB_TK and (groupType != LINE_COMMENT or groupType != BLOCK_COMMENT):
        groupType = SIB_TK
      if groupType == SIB_TK and groupType == CAD_TK:
        groupType = SIB_TK
      if groupType == CMF_TK and groupType == SIB_TK:
        groupType = CMF_TK
      if groupType == CMF_TK and groupType == CAD_TK:
        groupType = CMF_TK
      if groupType == BCM_TK:
        count = 0
        for char in value:
          if char == '\n':
            count += 1
        lineNum += count
      if groupType == NWL_TK:
        lineStart = matches.end()
        lineNum += 1
        continue
      if groupType == SKP_TK:
        continue
      
      if groupType != BCM_TK and groupType != LCM_TK and groupType != CAD_TK:
        if value not in charactersToRemove:
          if groupType == CMF_TK:
            charactersToRemove.insert(0, value)
          else:
            charactersToRemove.append(value)
        yield Token(groupType, value, lineNum)

    for chars in charactersToRemove:
      self.code = self.code.replace(chars, '')

  def scanTokens(self):
    superRegex = '|'.join('(?P<%s>%s)' % pair for pair in TOKEN_MAP)
    lineNum = 1
    lineStart = 0

    for matches in regex.finditer(superRegex, self.code):
      groupType = matches.lastgroup
      value = matches.group()

      if groupType == NRO_TK:
        value = float(value) if '.' in value else int(value)
      if groupType == IDE_TK and value in RESERVED_WORDS:
        groupType = PRE_TK
      if groupType == BCM_TK:
        count = 0
        for char in value:
          if char == '\n':
            count += 1
        lineNum += count
      if groupType == NWL_TK:
        lineStart = matches.end()
        lineNum += 1
        continue
      if groupType == SKP_TK:
        continue

      if groupType != BCM_TK and groupType != LCM_TK:
        yield Token(groupType, value, lineNum)