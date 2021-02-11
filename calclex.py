# ------------------------------------------------------------
# calclex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------
import sys

from ply import lex

from ply import *

import ply.lex as lex

# List of token names.   This is always required
tokens = [
   'STRING',
   'RA9M',
   'ZA2ID',
   'NA9ISS',
   'DREB',
   '9SSEM',
   'BA9IL9ISSMA',
   'ZIDFIH',
    'N9ESSFIH',
    'DREBFIH',
    '9SSEMFIH',
    'ZIDWA7ED',
    'N9ESSWA7ED',
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

    '9ELMN',
    '9ELYUSSAWI',
    'KTERMN',
    'KTERYUSSAWI',
    'YUSSAWI2',
    'MAKAYSSAWICH',

    'WA',
    'AW',
    'STEP',
    'TO',
    'LIKUL',
    '9RA'
]


reserved = {
    'ila' : 'ILA',                              #IF
    '9ra' : '9RA',                              #IF
    'idan' : 'IDAN',                            #then
    'ola' : 'OLA',                              #if else
    'manghirdakchi' : 'MANGHIRDAKCHI',           #else
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
    'wa'  : 'WA',                               #AND
    'aw'  : 'AW',                               #OR
    'step'  : 'STEP',
    'to'  : 'TO',



}

#the name following the t_ must exactly match one of the names supplied in tokens
# Regular expression rules for simple tokens

t_9ELMN               = r'<'
t_KTERMN               = r'>'
t_9ELYUSSAWI               = r'<='
t_KTERYUSSAWI               = r'>='
t_YUSSAWI2               = r'=='
t_MAKAYSSAWICH               = r'!='
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
t_STEP    = r'step'
t_TO    = r'to'
t_9RA    = r'9ra'

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
t_BA9IL9ISSMA  = r'%'
t_ZIDFIH = r'\+='
t_N9ESSFIH = r'-='
t_DREBFIH = r'\*='
t_9SSEMFIH = r'/='
t_ZIDWA7ED = r'\+\+'
t_N9ESSWA7ED = r'--'
t_LIKUL   = r'likul'
t_FI   = r'fi'
t_DKHEL = r'dkhel'
t_KTEB = r'kteb'
t_IDAN = r'idan'
t_MADAM = r'madam'
t_DIR = r'dir'
t_MANGHIRDAKCHI = r'manghirdakchi'
t_OLA = r'ola'
t_ILA = r'ila'
t_TUSSAWI = r'\='

t_WA = r'wa'
t_AW = r'aw'




tokens =tokens +list(reserved.values())
# A regular expression rule with some action code

def t_S7I7(t):
    r's7i7'
    t.value = True
    return t

def t_GHALAT(t):
    r'ghalat'
    t.value = False
    return t

def t_STRING(t):
    r'"[^"]*"'
    t.value = t.value[1:len(t.value) - 1]
    return t

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

#literals = [ '{', '}' ]




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
    #print("\n ********************** end of file :)")
    print("")


#to read the regular expression rules out of the calling context and build the lexer.
lexer = lex.lex(debug=True)




    #print(tok.type, tok.value, tok.lineno, tok.lexpos)
