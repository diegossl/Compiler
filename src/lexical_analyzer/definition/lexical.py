RESERVED_WORDS = [
  'var', 'const', 'typedef', 'struct', 'extends', 'procedure', 'function', 'start', 'return',
  'if', 'else', 'then', 'while', 'read', 'print', 'int', 'real', 'boolean', 'string', 'true',
  'false', 'global', 'local'
]
RELATIONAL_OPERATORS = ['==', '!=', '>', '>=', '<', '<=', '=']
DELIMITERS = [';', ',', '(', ')', '{', '}', '[', ']', '.']
ARITHMETIC_OPERATORS = ['+', '-', '*', '/', '++', '--']
IDENTIFIERS = '^([a-z]|[A-Z])(\d|[a-z]|[A-Z]|_)*$'
BLOCK_COMMENT = '\/[*]([^*]|([*][^/]))*[*]+\/'
NUMBER = '^(-)?(\s)*\d(\d)*(.\d(\d)*)?$'
LOGICAL_OPERATORS = ['&&', '||', '!']
LETTER = '^([a-z]|[A-Z])$'
LINE_COMMENT = '\/\/.*'
WHITE_SPACES = [9, 32]
BREAK_LINE = '^\\n$'
DIGIT = '^\d$'
STRING = ''