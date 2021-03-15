# Compiler

Front-end of a compiler made in Python.

## Instructions

1. Have installed Python version 3.9.2 on the machine.
2. Place the data files in the input folder using the following format: **entrada\<n\>.txt** n>=1.
3. Open the terminal in the project's root folder.
4. Run the software using the command: `python main.py`

## Guide

Table of lexemes:

| Acronym | Meaning             |
|---------|---------------------|
| PRE     | RESERVED WORD       |
| IDE     | IDENTIFIER          |
| NRO     | NUMBER              |
| DEL     | DELIMITER           |
| ART     | ARITHMETIC OPERATOR |
| REL     | RELATIONAL OPERATOR |
| LOG     | LOGIC OPERATOR      |
| CAD     | STRING              |

Table of errors:

| Acronym | Meaning            |
|---------|--------------------|
| SIB     | INVALID SYMBOL     |
| NMF     | MALFORMED NUMBER   |
| CMF     | MALFORMED STRING   |
| CoMF    | MALFORMED COMMENT  |
| OpMF    | MALFORMED OPERATOR |

## License

MIT
