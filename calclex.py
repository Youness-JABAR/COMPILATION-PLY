# ------------------------------------------------------------
# calclex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------
import ply.lex as lex

# List of token names.   This is always required
tokens = [
   'NUMBER',
   'PLUS',
   'MINUS',
   'TIMES',
   'DIVIDE',
   'LPAREN',
   'RPAREN',
   'ID',
   'KTEB',

]


reserved = {
   'if' : 'IF',
   'then' : 'THEN',
   'else' : 'ELSE',
   'while' : 'WHILE',

   'for'    : 'FOR',
   'input'  :  'INPUT',
   'print'  : 'PRINT',


}

# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_FOR   = r'for'
t_PRINT = r'print'
t_INPUT = r'input'
t_THEN = r'then'
t_ELSE = r'else'
t_IF = r'if'
t_KTEB = r'kteb'


tokens = tokens  + list(reserved.values())

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# EOF handling rule
def t_eof(t):
    # Get more input (Example)
    more = input('saisir : ')
    if more:
        lexer.input(more)
        return lexer.token()
    return None




# Build the lexer
lexer = lex.lex()


# Test it out
data = '''
3 + 4 * 10
  + -20 *2 - /
  kteb
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)

    print(tok.type, tok.value, tok.lineno, tok.lexpos)
