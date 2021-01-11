# ------------------------------------------------------------
# calclex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------
import sys

import ply.lex as lex

# List of token names.   This is always required
tokens = [
   'RA9M',
   'ZA2ID',
   'NA9ISS',
   'DREB',
   '9SSEM',
   'ID',
    'TUSSAWI',
    '7EL9AWESS',
    'SED9AWESS',
    '7ELM39UFA',
    'SEDM39UFA',
    '7ELLAMA',
    'SEDLAMA',
    'FASSILA',
    'NO9TA',
    'NO9TAFASSILA',
    'JUJNO9AT',

]


reserved = {
    'ila' : 'ILA',                              #IF
    'idan' : 'IDAN',                            #then
    'ola' : 'OLA',                              #if else
    'manghirdakchi' : 'MNGHIRDAKCHI',           #else
    'madam' : 'MADAM',                          #WHILE
    'dir': 'DIR',                               #DO
    'likul'    : 'LIKUL',                       #FOR
    'fi'    : 'FI',                             #in
    'dkhel'  :  'DKHEL',                        #PRINT
    'kteb'  : 'KTEB',                           #INPUT
    'kmel'  : 'KMEL',                           #continue
    'khrej'  : 'KHREJ',                         #BREAK
    'min'  : 'MIN',                             #FROM
    'jib'  : 'JIB',                             #IMPORT
    'm3roof'  : 'M3ROOF',                       #GLOBAL
    'duz'  : 'DUZ',                             #PASS
    'red'  : 'RED',                             #RETURN
    'jreb'  : 'JREB',                           #TRY
    'ched'  : 'CHED',                           #CATCH
    'senf'  : 'SENF',                           #CLASS
    's7i7'  : 'S7I7',                           #TRUE
    'ghalat'  : 'GHALAT',                       #FALSE
    'walo'  : 'WALO',                           #NONE
    'msse7'  : 'MSSE7',                         #DEL



}
#the name following the t_ must exactly match one of the names supplied in tokens
# Regular expression rules for simple tokens
# Delimeters
t_7EL9AWESS          = r'\('
t_SED9AWESS           = r'\)'
t_7ELM39UFA         = r'\['
t_SEDM39UFA         = r'\]'
t_7ELLAMA           = r'\{'
t_SEDLAMA           = r'\}'
t_FASSILA            = r','
t_NO9TA           = r'\.'
t_NO9TAFASSILA             = r';'
t_JUJNO9AT            = r':'

t_MSSE7    = r'msse7'
t_WALO    = r'walo'
t_GHALAT    = r'ghalat'
t_S7I7    = r's7i7'
t_SENF    = r'senf'
t_CHED    = r'ched'
t_JREB    = r'jreb'
t_RED    = r'red'
t_DUZ    = r'duz'
t_M3ROOF    = r'm3roof'
t_JIB    = r'jib'
t_MIN    = r'FROM'
t_KHREJ    = r'khrej'
t_KMEL    = r'kmel'
t_ZA2ID    = r'\+'
t_NA9ISS   = r'-'
t_DREB   = r'\*'
t_9SSEM  = r'/'
t_LIKUL   = r'likul'
t_FI   = r'fi'
t_DKHEL = r'dkhel'
t_KTEB = r'kteb'
t_IDAN = r'idan'
t_MADAM = r'madam'
t_DIR = r'dir'
t_MNGHIRDAKCHI = r'manghirdakchi'
t_OLA = r'ola'
t_ILA = r'if'
t_TUSSAWI = r'\='


tokens =tokens +list(reserved.values())
# A regular expression rule with some action code


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words

    return t
#this rule matches numbers and converts the string into a Python integer
# A regular expression rule with some action code
def t_RA9M(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t

def t_COMMENT(t):
    r'\#.*'
    pass
    # No return value. Token discarded

literals = [ '{', '}' ]

def t_lbrace(t):
    r'\{'
    t.type = '{'      # Set token type to the expected literal
    return t

def t_rbrace(t):
    r'\}'
    t.type = '}'      # Set token type to the expected literal
    return t


# Compute column.
#     input is the input text string
#     token is a token instance
def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1

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

    #more = input('saisir : ')
    #if more:
     #   lexer.input(more)
      #  return lexer.token()
    #return None
    print("\n ********************** end of file :)")



#to read the regular expression rules out of the calling context and build the lexer.
lexer = lex.lex(debug=True)


# Give the lexer some input
filename=sys.argv[1]
file_handle=open(filename,"r")
file_contents=file_handle.read()
lexer.input(file_contents)

# Tokenize
while True:
    # lexer.token() :Returns a special LexToken instance on success or None if the end of the input text has been reached.
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)

    #print(tok.type, tok.value, tok.lineno, tok.lexpos)
