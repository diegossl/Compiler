RESERVED_WORDS = [
  'var',
  'const',
  'typedef',
  'struct',
  'extends',
  'procedure',
  'function',
  'start',
  'return',
  'if',
  'else',
  'then',
  'while',
  'read',
  'print',
  'int',
  'real',
  'boolean',
  'string',
  'true',
  'false',
  'global',
  'local'
]

ARITHMETIC_OPERATORS = ['+', '-', '*', '/', '++', '--']

RELATIONAL_OPERATORS = ['==', '!=', '>', '>=', '<', '<=', '=']

LOGICAL_OPERATORS = ['&&', '||', '!']

DELIMITERS = [';', ',', '(', ')', '{', '}', '[', ']', '.']

BLOCK_COMMENT = '\/[*]([^*]|([*][^/]))*[*]+\/'

LINE_COMMENT = '\/\/.*'

IDENTIFIERS = '^([a-z]|[A-Z])(\d|[a-z]|[A-Z]|_)*$'

NUMBERS = '^(-)?(\s)*\d(\d)*(.\d(\d)*)?$'

DIGIT = '^\d$'

LETTER = '^([a-z]|[A-Z])$'

STRING = ''

