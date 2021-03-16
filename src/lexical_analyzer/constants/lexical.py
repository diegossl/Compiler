# Reserved word lexemes
RESERVED_WORDS = [
  'var', 'const', 'typedef', 'struct', 'extends', 'procedure', 'function', 'start', 'return',
  'if', 'else', 'then', 'while', 'read', 'print', 'int', 'real', 'boolean', 'string', 'true',
  'false', 'global', 'local'
]
# Expressions to find lexemes
STRING = r'\"(?:[^"\x00-\x1f\x7f-\xff]|\\.)*([a-z]|[A-Z]|[0-9]|[\x20-\x7f]|\\\")\"|\"\"'
RELATIONAL_OPERATORS = r'(\!\=)|(\<\=)|(\>\=)|(\=\=)|(\<)|(\>)|(\=)'
ARITHMETIC_OPERATORS = r'(\+\+|\+)|(\-\-|\-)|([\/]|[\*])'
IDENTIFIERS = r'([a-z]|[A-Z])(\d|[a-z]|[A-Z]|\_)*'
BLOCK_COMMENT = r'(\/[*]([^*]|([*][^/]))*[*]+\/)'
DELIMITERS = r'(\;|\,|\(|\)|\[|\]|\{|\}|\.)'
LOGICAL_OPERATORS = r'(\!)|(\&\&)|(\|\|)'
NUMBER = r'(\-)?(\s)*\d(\d)*(.\d(\d)*)?'
LINE_COMMENT = r'(\/\/.*)'
NEWLINE = r'\n'
SKIP = r'[ \t]+'