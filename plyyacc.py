#a regular language, a language that is recognizable by a finite automaton and formally expressible using regular expressions



# Yacc example
import parser
import sys
from ply import *


import ply.lex as lex
import ply.yacc as yacc
import calclex
tokens = calclex.tokens
variables={}
# Get the token map from the lexer.  This is required.
#from calclex import tokens

def p_statements(p):
    ''' statements : statements statement
                   | statement
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]



def p_statement(p):
    '''statement : assignement
                | printing'''
    p[0] = p[1]



def p_assignement(p):
    'assignement : ID TUSSAWI expression_string NO9TAFASSILA'
    variables.update({p[1] : p[3]})
    print(variables)
def p_expression_string(p):
    #'assignement : expression TUSSAWI expression| expression_string '
    ''' expression_string : expression
                            | STRING
                            | boolean'''
    p[0] = p[1]



def p_printing(p):
    'printing : KTEB 7EL9AWESS expression_string SED9AWESS NO9TAFASSILA'
    p[0] = p[3]

def p_statement_if(p):
    '''statement : ILA 7EL9AWESS boolean SED9AWESS statement
                    | ILA 7EL9AWESS boolean SED9AWESS statement MNGHIRDAKCHI statement'''
    if p[3]:
        p[0] = p[5]
    else:
        if p[7] is not None:
            p[0] = p[7]


def p_expression_plus(p):
    #'expression : RA9M ZA2ID RA9M'
    'expression : expression ZA2ID term'
    p[0] = p[1] + p[3]

def p_expression_minus(p):
    'expression : expression NA9ISS term'
    p[0] = p[1] - p[3]

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]
#MODULO
def p_term_modulo(p):
    'term : term BA9IL9ISSMA factor'
    p[0] = p[1] % p[3]

def p_term_times(p):
    'term : term DREB factor'
    p[0] = p[1] * p[3]

def p_term_div(p):
    'term : term 9SSEM factor'
    p[0] = p[1] / p[3]

def p_term_ID(p):
    'term : ID'
    p[0] = variables[p[1]]

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_expr(p):
    'factor : 7EL9AWESS expression SED9AWESS'
    p[0] = p[2]

def p_factor_num(p):
    'factor : RA9M'
    p[0] = p[1]

def p_boolean(p):
    ''' boolean : S7I7
                | GHALAT
    '''
    p[0] = p[1]

def p_comparison(p):
    '''boolean : expression YUSSAWI2 expression
                          | expression MAKAYSSAWICH expression
                          | expression KTERMN expression
                          | expression 9ELMN expression
                          | expression KTERYUSSAWI expression
                          | expression 9ELYUSSAWI expression'''
    if p[2] == '==':
        p[0] = p[1] == p[3]
    elif p[2] == '!=':
        p[0] = p[1] != p[3]
    elif p[2] == '>':
        p[0] = p[1] > p[3]
    elif p[2] == '<':
        p[0] = p[1] < p[3]
    elif p[2] == '>=':
        p[0] = p[1] >= p[3]
    elif p[2] == '<=':
        p[0] = p[1] <= p[3]

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

#data = open('file.txt').read().replace('\n', '')
filename=sys.argv[1]
file_handle=open(filename,"r")
file_contents=file_handle.read()
result = parser.parse(file_contents)
# Tokenize
calclex.lexer.input(file_contents)
while True:
    # lexer.token() :Returns a special LexToken instance on success or None if the end of the input text has been reached.
    tok =calclex.lexer.token()
    if not tok:
        break      # No more input
    print(tok)
for r in result:
    print(r)

while True:
   try:
       s = input('calc > ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)