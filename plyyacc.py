#a regular language, a language that is recognizable by a finite automaton and formally expressible using regular expressions



# Yacc example
from typing import Any

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

def p_assignement_error(p):
    'assignement : ID TUSSAWI expression_string error'
    print("Khass tkemel b ; f ster %s%s%s !!!." % (p[1], p[2], p[3]))

def p_assignement_plusaff(p):
    'assignement : ID ZIDFIH expression NO9TAFASSILA'
    variables.update({p[1]: variables[p[1]] + p[3]})

def p_assignement_plusaff_error(p):
    'assignement : ID ZIDFIH expression error'
    print("Khass tkemel b ; f ster %s%s%s !!!." % (p[1], p[2], p[3]))

def p_assignement_moinsaff(p):
    'assignement : ID N9ESSFIH expression NO9TAFASSILA'
    variables.update({p[1]: variables[p[1]] - p[3]})

def p_assignement_moinsaff_error(p):
    'assignement : ID N9ESSFIH expression error'
    print("Khass tkemel b ; f ster %s%s%s !!!." % (p[1], p[2], p[3]))

def p_assignement_timessaff(p):
    'assignement : ID DREBFIH expression NO9TAFASSILA'
    variables.update({p[1]: variables[p[1]] * p[3]})

def p_assignement_timessaff_error(p):
    'assignement : ID DREBFIH expression error'
    print("Khass tkemel b ; f ster %s%s%s !!!." % (p[1], p[2], p[3]))

def p_assignement_divsaff(p):
    'assignement : ID 9SSEMFIH expression NO9TAFASSILA'
    variables.update({p[1]: variables[p[1]] * p[3]})

def p_assignement_divsaff_error(p):
    'assignement : ID 9SSEMFIH expression error'
    print("Khass tkemel b ; f ster %s%s%s !!!." % (p[1], p[2], p[3]))

def p_assignement_incrementation(p):
    'assignement : ID ZIDWA7ED NO9TAFASSILA'
    variables.update({p[1]: variables[p[1]] + 1})

def p_assignement_incrementation_error(p):
    'assignement : ID ZIDWA7ED error'
    print("Khass tkemel b ; f ster %s%s !!!." % (p[1], p[2]))

def p_assignement_decrementation(p):
    'assignement : ID N9ESSWA7ED NO9TAFASSILA'
    variables.update({p[1]: variables[p[1]] - 1})

def p_assignement_decrementation_error(p):
    'assignement : ID N9ESSWA7ED error'
    print("Khass tkemel b ; f ster %s%s !!!." % (p[1], p[2]))

def p_printing(p):
    'printing : KTEB 7EL9AWESS expression_string SED9AWESS NO9TAFASSILA'
    p[0] = p[3]

def p_printing_error(p):
    'printing : KTEB 7EL9AWESS expression_string SED9AWESS error'
    print("Khass tkemel b ; f ster %s  !!!." % (p[1]))
def p_printing_error(p):
    'printing : KTEB 7EL9AWESS expression_string error NO9TAFASSILA'
    print("Khass tssed l9awess  f ster %s  !!!." % (p[1]))

def p_expression_string(p):
    #'assignement : expression TUSSAWI expression| expression_string '
    ''' expression_string : expression
                            | STRING
                            | boolean'''
    p[0] = p[1]

def p_string(p):
    '''string : STRING
                '''

################################################## PARTIE IF ##############################"
#racine elif
def p_elif2(p):
    '''olas : olas ola
              | ola
              | olas ola2'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

#elif
def p_elif(p):
    'ola : OLA 7EL9AWESS booleans SED9AWESS 7ELLAMA statements SEDLAMA'
    if p[3]:
        p[0]=p[6]


#if tanya elif else
def p_elif3(p):
    'ola2 : OLA 7EL9AWESS booleans SED9AWESS 7ELLAMA statements SEDLAMA MANGHIRDAKCHI 7ELLAMA statements SEDLAMA'
    if p[3]:
        p[0]=p[6]
    else:
        p[0]=p[10]

def p_statement_if(p):
    '''statement : ILA 7EL9AWESS booleans SED9AWESS 7ELLAMA statements SEDLAMA
                   | ILA 7EL9AWESS booleans SED9AWESS 7ELLAMA statements SEDLAMA olas
                   '''
    if len(p) == 8:
        if p[3]:
            p[0] = p[6]
    else:
        if p[3]:
            p[0] = p[6]
        else:
            p[0] = p[8]

def p_statement_else(p):
    '''statement : ILA 7EL9AWESS booleans SED9AWESS 7ELLAMA statements SEDLAMA MANGHIRDAKCHI 7ELLAMA statements SEDLAMA
                | ILA 7EL9AWESS booleans SED9AWESS 7ELLAMA statements SEDLAMA ola2
                 '''

    if len(p) == 12:
        if p[3]:
            p[0] = p[6]

        else:
            if p[10] is not None:
                p[0] = p[10]
    else:
        if p[3]:
            p[0] = p[6]
        else:
            p[0] = p[8]
################################################## FIN PARTIE IF ##############################"

def p_statement_while(p):
    'statement : loop_while'
    p[0]=p[1]

def p_loop_while(p):
    'loop_while : MADAM 7EL9AWESS boolean SED9AWESS 7ELLAMA statements  SEDLAMA'

    i=0
    ret=[]
    while(p[3]):
        #print("true")
        ret.append(p[6])
        i=i+1
        if (i==10):
            print("ereur : boucle infini")
            print(variables)
            break
    p[0] = ret
#na9ISSSS------------------------------------------------
precedence = (
    ('left', 'ZA2ID', 'NA9ISS'),
    ('left', 'DREB', '9SSEM'),
    ('right', 'UMINUS'),            # Unary minus operator
)

def p_expr_uminus(p):
    'RA9M_salib : NA9ISS RA9M %prec UMINUS'
    p[0] = -p[2]
def p_term_RA9M_salib(p):
    'factor : RA9M_salib'
    p[0] = p[1]
#FINNA9ISS-!-----------------------6------------
#tableau----------------------------------------
def p_assignement_change_element_array(p):
    ' assignement : change_element_array '
    p[0] = p[1]

def p_change_element_array(p):
    ''' change_element_array : ID array_index TUSSAWI element NO9TAFASSILA
                                | ID array_index array_index TUSSAWI element NO9TAFASSILA
    '''
    if(len(p)==6):
        print(variables[p[1]][p[2]])
        variables[p[1]][p[2]]=p[4]
    else:
        variables[p[1]][p[2]][p[3]]=p[5]


def p_array_index(p):
    ' array_index : 7ELM39UFA expression SEDM39UFA'
    p[0] = p[2]
def p_element_return(p):
    ''' expression_string : ID array_index
                            | ID  array_index array_index
    '''
    if(len(p)==3):
        p[0] = variables[p[1]][p[2]]
    else:

        p[0] = variables[p[1]][p[2]][p[3]]


def p_element_exp_str(p):
    ''' element : expression_string
                | array_content
    '''
    p[0] = p[1]
def p_elements(p):
    ''' elements : element FASSILA elements
                    | element
    '''
    ret=[]
    if (len(p) == 2):
        ret.append(p[1])
    else:
        ret.append(p[1])
        ret.extend(p[3])

    p[0] = ret
def p_assignement_array(p):
    ' assignement : array'
    p[0] = p[1]

def p_array_content(p):
    ' array_content : 7ELM39UFA elements SEDM39UFA'
    p[0] = p[2]
def p_array(p):
    ''' array : ID TUSSAWI 7ELM39UFA SEDM39UFA NO9TAFASSILA
        | ID TUSSAWI array_content NO9TAFASSILA
    '''
    if(len(p)==6):
        variables.update({p[1]: []})
    else:

        variables.update({p[1]: p[3]})



def p_expression_paren(p):
    'expression : 7EL9AWESS expression SED9AWESS'
    p[0] = p[2]

def p_expression_plus(p):
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
    'term : term BA9IL9ISSMA term'
    p[0] = p[1] % p[3]

def p_term_times(p):
    'term : term DREB term'
    p[0] = p[1] * p[3]

def p_term_div(p):
    'term : term 9SSEM term'
    if p[3] == 0:
        print('Maymkench l9issma 3la 0!!!.')
        raise ZeroDivisionError('Maymkench l9issma 3la 0!!!.')
    else:
        p[0] = p[1] / p[3]

def p_term_factor(p):
    '''term : factor
            '''
    p[0] = p[1]

def p_term_ID(p):
    'term : ID'
    p[0] = variables[p[1]]




def p_factor_num(p):
    'factor : RA9M'
    p[0] = p[1]

def p_boolean(p):
    ''' boolean : S7I7
                | GHALAT
    '''
    p[0] = p[1]

def p_comparison2(p):
    r'''booleans :            booleans WA boolean
                              | booleans AW boolean
                              | boolean
                              | 7EL9AWESS booleans SED9AWESS

                              '''
    if len(p) == 2:
        p[0] = p[1]
    elif p[2]=="wa":
        p[0] = p[1] and p[3]
    elif p[2]=="aw":
        p[0] = p[1] or p[3]
    elif p[1]=='(':
        p[0] = p[2]


def p_comparison(p):
    '''boolean :            boolean YUSSAWI2 boolean
                          | boolean MAKAYSSAWICH boolean

                          | ID YUSSAWI2 boolean
                          | ID MAKAYSSAWICH boolean

                          | boolean YUSSAWI2 ID
                          | boolean MAKAYSSAWICH ID

                          | ID YUSSAWI2 ID
                          | ID MAKAYSSAWICH ID
                          | ID KTERMN ID
                          | ID 9ELMN ID
                          | ID KTERYUSSAWI ID
                          | ID 9ELYUSSAWI ID

                          | expression YUSSAWI2 ID
                          | expression MAKAYSSAWICH ID
                          | expression KTERMN ID
                          | expression 9ELMN ID
                          | expression KTERYUSSAWI ID
                          | expression 9ELYUSSAWI ID

                          | ID YUSSAWI2 expression
                          | ID MAKAYSSAWICH expression
                          | ID KTERMN expression
                          | ID 9ELMN expression
                          | ID KTERYUSSAWI expression
                          | ID 9ELYUSSAWI expression

                          | expression YUSSAWI2 expression
                          | expression MAKAYSSAWICH expression
                          | expression KTERMN expression
                          | expression 9ELMN expression
                          | expression KTERYUSSAWI expression
                          | expression 9ELYUSSAWI expression
                          '''
    if p[2] == '==':
        if variables.get(p[1]) != None and variables.get(p[3]) == None:
            p[0] = variables[p[1]] == p[3]
        elif variables.get(p[1]) == None and variables.get(p[3]) != None:
            p[0] = p[1] == variables[p[3]]
        elif variables.get(p[1]) != None and variables.get(p[3]) != None:
            p[0] = variables[p[1]] == variables[p[3]]
        else:
            p[0] = p[1] == p[3]
    elif p[2] == '!=':
        if variables.get(p[1]) != None and variables.get(p[3]) == None:
            p[0] = variables[p[1]] != p[3]
        elif variables.get(p[1]) == None and variables.get(p[3]) != None:
            p[0] = p[1] != variables[p[3]]
        elif variables.get(p[1]) != None and variables.get(p[3]) != None:
            p[0] = variables[p[1]] != variables[p[3]]
        else:
            p[0] = p[1] != p[3]
    elif p[2] == '>':
        if variables.get(p[1]) != None and variables.get(p[3]) == None:
            p[0] = variables[p[1]] > p[3]
        elif variables.get(p[1]) == None and variables.get(p[3]) != None:
            p[0] = p[1] > variables[p[3]]
        elif variables.get(p[1]) != None and variables.get(p[3]) != None:
            p[0] = variables[p[1]] > variables[p[3]]
        else:
            p[0] = p[1] > p[3]
    elif p[2] == '<':

        if variables.get(p[1]) != None and variables.get(p[3]) == None:
            p[0] = variables[p[1]] < p[3]
        elif variables.get(p[1]) == None and variables.get(p[3]) != None:
            p[0] = p[1] < variables[p[3]]
        elif variables.get(p[1]) != None and variables.get(p[3]) != None:
            p[0] = variables[p[1]] < variables[p[3]]
        else:
            p[0] = p[1] < p[3]
    elif p[2] == '>=':
        if variables.get(p[1]) != None and variables.get(p[3]) == None:
            p[0] = variables[p[1]] >= p[3]
        elif variables.get(p[1]) == None and variables.get(p[3]) != None:
            p[0] = p[1] >= variables[p[3]]
        elif variables.get(p[1]) != None and variables.get(p[3]) != None:
            p[0] = variables[p[1]] >= variables[p[3]]
        else:
            p[0] = p[1] >= p[3]
    elif p[2] == '<=':
        if variables.get(p[1]) != None and variables.get(p[3]) == None:
            p[0] = variables[p[1]] <= p[3]
        elif variables.get(p[1]) == None and variables.get(p[3]) != None:
            p[0] = p[1] <= variables[p[3]]
        elif variables.get(p[1]) != None and variables.get(p[3]) != None:
            p[0] = variables[p[1]] <= variables[p[3]]
        else:
            p[0] = p[1] <= p[3]

def p_command_for(p):
    '''statement : LIKUL 7EL9AWESS ID TUSSAWI expression TAL expression FASSILA KHETWA TUSSAWI expression SED9AWESS 7ELLAMA statements SEDLAMA'''
   # p[0] = ('likul', p[3], p[5], p[7], p[10])
    ret = []
    if p[7] > p[5]:
        i = 0
        while i < p[7]-p[5]:
            ret.append(p[14])
            i = i+int(p[11])
        p[0] = ret
    else:
        print("erreur index")

def p_command_for_nostep(p):
    '''statement : LIKUL 7EL9AWESS ID TUSSAWI expression TAL expression SED9AWESS 7ELLAMA statements SEDLAMA'''
# p[0] = ('likul', p[3], p[5], p[7], p[10])
    ret = []
    if p[7] > p[5]:
         for i in range(p[7]-p[5]):
             ret.append(p[10])
         p[0] = ret
    else:
          print("erreur index")

# Error rule for syntax errors
def p_error(p):
    print("Khata2 f ktaba !!!")

# Build the parser
parser = yacc.yacc()

#data = open('file.txt').read().replace('\n', '')
filename=sys.argv[1]
file_handle=open(filename,"r")
file_contents=file_handle.read()
result = parser.parse(file_contents)
# Tokenize
'''calclex.lexer.input(file_contents)
while True:
    # lexer.token() :Returns a special LexToken instance on success or None if the end of the input text has been reached.
    tok =calclex.lexer.token()
    if not tok:
        break      # No more input
    print(tok)'''
if result is not None:
    for r in result:
        if r == None:
            continue;
        else:
            print(r)


