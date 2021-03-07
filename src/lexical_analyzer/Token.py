from typing import NamedTuple

class Token(NamedTuple):
  tokenType: str
  tokenValue: str
  tokenLine: int