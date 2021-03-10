RESERVED_WORDS = [
  'var', 'const', 'typedef', 'struct', 'extends', 'procedure', 'function', 'start', 'return',
  'if', 'else', 'then', 'while', 'read', 'print', 'int', 'real', 'boolean', 'string', 'true',
  'false', 'global', 'local'
]
STRING = r'"(?:[^"\x00-\x1f\x7f-\xff]|\\.)*([a-z]|[A-Z]|[0-9]|[\x20-\x7f]|\\")"|""'
ARITHMETIC_OPERATORS = r'(\+\+|\+)|(\-\-|\-)|([\/]|[\*])'
IDENTIFIERS = r'(_|[a-z]|[A-Z])(\d|[a-z]|[A-Z]|_)*'
BLOCK_COMMENT = r'(\/[*]([^*]|([*][^/]))*[*]+\/)'
RELATIONAL_OPERATORS = r'(!=|==|<|<=|>|>=|=)'
DELIMITERS = r'(:|;|,|\(|\)|\[|\]|\{|\}|\.)'
NUMBER = r'(-)?(\s)*\d(\d)*(.\d(\d)*)?'
LOGICAL_OPERATORS = r'(!|&&|\|\|)'
LINE_COMMENT = r'(\/\/.*)'
NEWLINE = r'\n'
SKIP = r'[ \t]+'

