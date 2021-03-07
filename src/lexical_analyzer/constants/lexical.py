RESERVED_WORDS = [
  'var', 'const', 'typedef', 'struct', 'extends', 'procedure', 'function', 'start', 'return',
  'if', 'else', 'then', 'while', 'read', 'print', 'int', 'real', 'boolean', 'string', 'true',
  'false', 'global', 'local'
]
STRING = r'"([A-Z]|[a-z]|[0-9]|[\n]|[\x20-\x21]|[\x23-\x7E]|[\\"])*"'
RELATIONAL_OPERATORS = r'(!=|==|<|<=|>|>=|=)'
IDENTIFIERS = r'([a-z]|[A-Z])(\d|[a-z]|[A-Z]|_)*'
BLOCK_COMMENT = r'(\/[*]([^*]|([*][^/]))*[*]+\/)'
DELIMITERS = r'(:|;|,|\(|\)|\[|\]|\{|\}|\.)'
NUMBER = r'(-)?(\s)*\d(\d)*(.\d(\d)*)?'
LOGICAL_OPERATORS = r'(!|&&|\|\|)'
ARITHMETIC_OPERATORS = r'(\+\+|\+)'
LINE_COMMENT = r'(\/\/.*)'

# LETTER = '^([a-z]|[A-Z])$'
# DIGIT = '^\d$'

NEWLINE = r'\n'
SKIP = r'[ \t]+'