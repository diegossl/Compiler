from .definition.lexical import (ARITHMETIC_OPERATORS, LOGICAL_OPERATORS,
  RESERVED_WORDS, BLOCK_COMMENT, LINE_COMMENT, WHITE_SPACES, IDENTIFIERS, DELIMITERS,
  BREAK_LINE, NUMBER, LETTER, STRING, DIGIT
)

class Comparator:

  def __init__(self):
    pass

  def isReservedWord(self, data):
    return data in RESERVED_WORDS

  def isIdentifier(self, data):
    return re.match(IDENTIFIERS, data) != None
  
  def isDigit(self, data):
    return re.match(DIGIT, data) != None
  
  def isValidString(self, data):
    return re.match(STRING, data) != None

  def isLetter(self, data):
    return re.match(LETTER, data) != None

  def isBreakline(self, data):
    return re.match(BREAK_LINE, data) != None

  def isWhiteSpace(self, data):
    return ord(data) in WHITE_SPACES

  def isValidNumber(self, data):
    return re.match(NUMBER, data) != None

  def isBlockComment(self, data):
    return re.match(BLOCK_COMMENT, data) != None

  def isLineComment(self, data):
    return re.match(LINE_COMMENT, data) != None
  
  def isDelimiter(self, data):
    return data in DELIMITERS

  def isLogicalOperator(self, data):
    return data in LOGICAL_OPERATORS

  def isLogicalOperator(self, data):
    return data in LOGICAL_OPERATORS

  def isArithmeticOperator(self, data):
    return data in ARITHMETIC_OPERATORS