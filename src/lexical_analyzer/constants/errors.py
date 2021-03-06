# Expressions to find lexical errors
MALFORMED_STRING = r'(\")([^\"\x0a]+)|(\"([a-z]|[A-Z]|[0-9]|[\x00-\x20\x7f-\xff])*([\x00-\x1f\x7f-\xff])+([a-z]|[A-Z]|[0-9]|[\x00-\x20\x7f-\xff])*\")'
INVALID_SYMBOL = r'([\x7e-\xff]|[\#\$\%\'\?\@\\\^\`\~\:])|((?<![a-z]|[A-Z]|[0-9])\_)+'
MALFORMED_COMMENT = r'(?!([^*]|([*][^/]))*[*]+\/)(\/[*]([^*]|([*][^/]))*)'
MALFORMED_OPERATOR = r'((?<!\&)(\&)(?!\&))|((?<!\|)(\|)(?!\|))'
MALFORMED_NUMBER = r'\-?[0-9]+(\.+|\.$)(?![0-9])'