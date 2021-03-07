from .constants.types import NRO_TK, IDE_TK, PRE_TK, BCM_TK, LCM_TK, NWL_TK, SKP_TK
from .constants.lexical import RESERVED_WORDS
from .constants.map import TOKENS_MAP
from .Token import Token
import re as regex

class Scanner:

  def tokenize(self, code):
    superRegex = '|'.join('(?P<%s>%s)' % pair for pair in TOKENS_MAP)
    lineNum = 1
    lineStart = 0

    for matches in regex.finditer(superRegex, code):
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
      if groupType == 'MISMATCH':
        raise RuntimeError(f'{value!r} unexpected on line {lineNum}')

      if groupType != BCM_TK and groupType != LCM_TK:
        yield Token(groupType, value, lineNum)