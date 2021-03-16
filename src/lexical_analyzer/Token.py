from typing import NamedTuple

# The Token class is of the NamedTuple type, which is a
# class that, like dictionary objects, contains keys and
# that are mapped to some values. In this case, we can
# access the elements using keys and indexes.
class Token(NamedTuple):
  tokenType: str
  tokenValue: str
  tokenLine: int