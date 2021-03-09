RESERVED_WORDS = [
  'var', 'const', 'typedef', 'struct', 'extends', 'procedure', 'function', 'start', 'return',
  'if', 'else', 'then', 'while', 'read', 'print', 'int', 'real', 'boolean', 'string', 'true',
  'false', 'global', 'local'
]
STRING = r'"(?:[^"\x00-\x1f\x7f-\xff]|\\.)*."'
RELATIONAL_OPERATORS = r'(!=|==|<|<=|>|>=|=)'
IDENTIFIERS = r'([a-z]|[A-Z])(\d|[a-z]|[A-Z]|_)*'
BLOCK_COMMENT = r'(\/[*]([^*]|([*][^/]))*[*]+\/)'
DELIMITERS = r'(:|;|,|\(|\)|\[|\]|\{|\}|\.)'
NUMBER = r'(-)?(\s)*\d(\d)*(.\d(\d)*)?'
LOGICAL_OPERATORS = r'(!|&&|\|\|)'
ARITHMETIC_OPERATORS = r'(\+\+|\+)'
LINE_COMMENT = r'(\/\/.*)'
NEWLINE = r'\n'
SKIP = r'[ \t]+'
# LETTER = '^([a-z]|[A-Z])$'
# DIGIT = '^\d$'

