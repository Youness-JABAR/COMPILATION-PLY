
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = '7EL9AWESS 7ELLAMA 7ELM39UFA 9ELMN 9ELYUSSAWI 9SSEM 9SSEMFIH BA9IL9ISSMA CHED DIR DKHEL DREB DREBFIH DUZ FASSILA FI GHALAT ID IDAN ILA JIB JREB JUJNO9AT KHREJ KMEL KTEB KTERMN KTERYUSSAWI LIKUL M3ROOF MADAM MAKAYSSAWICH MIN MNGHIRDAKCHI MSSE7 N9ESSFIH N9ESSWA7ED NA9ISS NO9TA NO9TAFASSILA OLA RA9M RED S7I7 SED9AWESS SEDLAMA SEDM39UFA SENF STRING TUSSAWI WALO YUSSAWI2 ZA2ID ZIDFIH ZIDWA7ED statements : statements statement\n                   | statement\n    statement : assignement\n                | printingassignement : ID TUSSAWI expression_string NO9TAFASSILAassignement : ID ZIDFIH expression NO9TAFASSILAassignement : ID N9ESSFIH expression NO9TAFASSILAassignement : ID DREBFIH expression NO9TAFASSILAassignement : ID 9SSEMFIH expression NO9TAFASSILAassignement : ID ZIDWA7ED NO9TAFASSILAassignement : ID N9ESSWA7ED NO9TAFASSILA expression_string : expression\n                            | STRING\n                            | booleanprinting : KTEB 7EL9AWESS expression_string SED9AWESS NO9TAFASSILAexpression : NA9ISS expression statement : ILA 7EL9AWESS boolean SED9AWESS 7ELLAMA statements SEDLAMA\n                    | ILA 7EL9AWESS boolean SED9AWESS statement MNGHIRDAKCHI statementstatement : MADAM 7EL9AWESS boolean SED9AWESS 7ELLAMA statements SEDLAMAexpression : 7EL9AWESS expression SED9AWESSexpression : expression ZA2ID termexpression : expression NA9ISS termexpression : termterm : term BA9IL9ISSMA factorterm : term DREB factorterm : term 9SSEM factorterm : IDterm : factorfactor : 7EL9AWESS expression SED9AWESSfactor : RA9M boolean : S7I7\n                | GHALAT\n    boolean : ID YUSSAWI2 boolean\n                          | ID MAKAYSSAWICH boolean\n                          | boolean YUSSAWI2 ID\n                          | boolean MAKAYSSAWICH ID\n                          | ID YUSSAWI2 ID\n                          | ID MAKAYSSAWICH ID\n                          | boolean YUSSAWI2 boolean\n                          | boolean MAKAYSSAWICH boolean\n                          | expression YUSSAWI2 expression\n                          | expression MAKAYSSAWICH expression\n                          | expression KTERMN expression\n                          | expression 9ELMN expression\n                          | expression KTERYUSSAWI expression\n                          | expression 9ELYUSSAWI expression'
    
_lr_action_items = {'ILA':([0,1,2,3,4,9,40,41,44,62,63,64,65,66,69,91,92,93,94,96,97,98,100,],[5,5,-2,-3,-4,-1,-10,-11,5,-5,-6,-7,-8,-9,5,5,-15,5,5,5,-17,-18,-19,]),'MADAM':([0,1,2,3,4,9,40,41,44,62,63,64,65,66,69,91,92,93,94,96,97,98,100,],[6,6,-2,-3,-4,-1,-10,-11,6,-5,-6,-7,-8,-9,6,6,-15,6,6,6,-17,-18,-19,]),'ID':([0,1,2,3,4,9,10,11,12,13,14,15,16,19,20,26,40,41,44,45,46,47,48,49,50,51,52,53,54,55,56,62,63,64,65,66,69,86,91,92,93,94,96,97,98,100,],[7,7,-2,-3,-4,-1,24,24,24,35,35,35,35,24,35,35,-10,-11,7,72,74,75,77,35,35,35,35,35,35,35,35,-5,-6,-7,-8,-9,7,35,7,-15,7,7,7,-17,-18,-19,]),'KTEB':([0,1,2,3,4,9,40,41,44,62,63,64,65,66,69,91,92,93,94,96,97,98,100,],[8,8,-2,-3,-4,-1,-10,-11,8,-5,-6,-7,-8,-9,8,8,-15,8,8,8,-17,-18,-19,]),'$end':([1,2,3,4,9,40,41,62,63,64,65,66,92,97,98,100,],[0,-2,-3,-4,-1,-10,-11,-5,-6,-7,-8,-9,-15,-17,-18,-19,]),'SEDLAMA':([2,3,4,9,40,41,62,63,64,65,66,92,93,96,97,98,100,],[-2,-3,-4,-1,-10,-11,-5,-6,-7,-8,-9,-15,97,100,-17,-18,-19,]),'MNGHIRDAKCHI':([3,4,40,41,62,63,64,65,66,70,92,97,98,100,],[-3,-4,-10,-11,-5,-6,-7,-8,-9,94,-15,-17,-18,-19,]),'7EL9AWESS':([5,6,8,10,11,12,13,14,15,16,19,20,26,45,46,47,48,49,50,51,52,53,54,55,56,58,59,60,86,],[10,11,19,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,86,86,86,86,86,20,]),'TUSSAWI':([7,],[12,]),'ZIDFIH':([7,],[13,]),'N9ESSFIH':([7,],[14,]),'DREBFIH':([7,],[15,]),'9SSEMFIH':([7,],[16,]),'ZIDWA7ED':([7,],[17,]),'N9ESSWA7ED':([7,],[18,]),'S7I7':([10,11,12,19,45,46,47,48,],[22,22,22,22,22,22,22,22,]),'GHALAT':([10,11,12,19,45,46,47,48,],[23,23,23,23,23,23,23,23,]),'NA9ISS':([10,11,12,13,14,15,16,19,20,24,25,26,27,28,29,32,35,36,37,38,39,43,45,46,47,48,49,50,51,52,53,54,57,68,72,74,75,77,79,80,81,82,83,84,85,86,87,88,89,90,95,99,],[26,26,26,26,26,26,26,26,26,-27,56,26,-23,-28,-30,56,-27,56,56,56,56,56,26,26,26,26,26,26,26,26,26,26,56,-20,-27,-27,-27,-27,56,56,56,56,56,56,-21,26,-22,-24,-25,-26,56,-29,]),'RA9M':([10,11,12,13,14,15,16,19,20,26,45,46,47,48,49,50,51,52,53,54,55,56,58,59,60,86,],[29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'STRING':([12,19,],[33,33,]),'NO9TAFASSILA':([17,18,22,23,24,27,28,29,31,32,33,34,35,36,37,38,39,57,67,68,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,87,88,89,90,99,],[40,41,-31,-32,-27,-23,-28,-30,62,-12,-13,-14,-27,63,64,65,66,-16,92,-20,-39,-35,-40,-36,-37,-33,-38,-34,-41,-42,-43,-44,-45,-46,-21,-22,-24,-25,-26,-29,]),'SED9AWESS':([21,22,23,24,27,28,29,30,32,33,34,35,42,43,57,68,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,87,88,89,90,95,99,],[44,-31,-32,-27,-23,-28,-30,61,-12,-13,-14,-27,67,68,-16,-20,-39,-35,-40,-36,-37,-33,-38,-34,-41,-42,-43,-44,-45,-46,-21,-22,-24,-25,-26,99,-29,]),'YUSSAWI2':([21,22,23,24,25,27,28,29,30,32,34,35,57,68,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,87,88,89,90,99,],[45,-31,-32,47,49,-23,-28,-30,45,49,45,-27,-16,-20,45,47,45,47,47,45,47,45,-41,-42,-43,-44,-45,-46,-21,-22,-24,-25,-26,-29,]),'MAKAYSSAWICH':([21,22,23,24,25,27,28,29,30,32,34,35,57,68,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,87,88,89,90,99,],[46,-31,-32,48,50,-23,-28,-30,46,50,46,-27,-16,-20,46,48,46,48,48,46,48,46,-41,-42,-43,-44,-45,-46,-21,-22,-24,-25,-26,-29,]),'BA9IL9ISSMA':([24,27,28,29,35,68,72,74,75,77,85,87,88,89,90,99,],[-27,58,-28,-30,-27,-29,-27,-27,-27,-27,58,58,-24,-25,-26,-29,]),'DREB':([24,27,28,29,35,68,72,74,75,77,85,87,88,89,90,99,],[-27,59,-28,-30,-27,-29,-27,-27,-27,-27,59,59,-24,-25,-26,-29,]),'9SSEM':([24,27,28,29,35,68,72,74,75,77,85,87,88,89,90,99,],[-27,60,-28,-30,-27,-29,-27,-27,-27,-27,60,60,-24,-25,-26,-29,]),'KTERMN':([24,25,27,28,29,32,35,57,68,72,74,75,77,85,87,88,89,90,99,],[-27,51,-23,-28,-30,51,-27,-16,-20,-27,-27,-27,-27,-21,-22,-24,-25,-26,-29,]),'9ELMN':([24,25,27,28,29,32,35,57,68,72,74,75,77,85,87,88,89,90,99,],[-27,52,-23,-28,-30,52,-27,-16,-20,-27,-27,-27,-27,-21,-22,-24,-25,-26,-29,]),'KTERYUSSAWI':([24,25,27,28,29,32,35,57,68,72,74,75,77,85,87,88,89,90,99,],[-27,53,-23,-28,-30,53,-27,-16,-20,-27,-27,-27,-27,-21,-22,-24,-25,-26,-29,]),'9ELYUSSAWI':([24,25,27,28,29,32,35,57,68,72,74,75,77,85,87,88,89,90,99,],[-27,54,-23,-28,-30,54,-27,-16,-20,-27,-27,-27,-27,-21,-22,-24,-25,-26,-29,]),'ZA2ID':([24,25,27,28,29,32,35,36,37,38,39,43,57,68,72,74,75,77,79,80,81,82,83,84,85,87,88,89,90,95,99,],[-27,55,-23,-28,-30,55,-27,55,55,55,55,55,55,-20,-27,-27,-27,-27,55,55,55,55,55,55,-21,-22,-24,-25,-26,55,-29,]),'7ELLAMA':([44,61,],[69,91,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statements':([0,69,91,],[1,93,96,]),'statement':([0,1,44,69,91,93,94,96,],[2,9,70,2,2,9,98,9,]),'assignement':([0,1,44,69,91,93,94,96,],[3,3,3,3,3,3,3,3,]),'printing':([0,1,44,69,91,93,94,96,],[4,4,4,4,4,4,4,4,]),'boolean':([10,11,12,19,45,46,47,48,],[21,30,34,34,71,73,76,78,]),'expression':([10,11,12,13,14,15,16,19,20,26,45,46,47,48,49,50,51,52,53,54,86,],[25,25,32,36,37,38,39,32,43,57,25,25,25,25,79,80,81,82,83,84,95,]),'term':([10,11,12,13,14,15,16,19,20,26,45,46,47,48,49,50,51,52,53,54,55,56,86,],[27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,85,87,27,]),'factor':([10,11,12,13,14,15,16,19,20,26,45,46,47,48,49,50,51,52,53,54,55,56,58,59,60,86,],[28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,88,89,90,28,]),'expression_string':([12,19,],[31,42,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statements","S'",1,None,None,None),
  ('statements -> statements statement','statements',2,'p_statements','plyyacc.py',20),
  ('statements -> statement','statements',1,'p_statements','plyyacc.py',21),
  ('statement -> assignement','statement',1,'p_statement','plyyacc.py',31),
  ('statement -> printing','statement',1,'p_statement','plyyacc.py',32),
  ('assignement -> ID TUSSAWI expression_string NO9TAFASSILA','assignement',4,'p_assignement','plyyacc.py',36),
  ('assignement -> ID ZIDFIH expression NO9TAFASSILA','assignement',4,'p_assignement_plusaff','plyyacc.py',40),
  ('assignement -> ID N9ESSFIH expression NO9TAFASSILA','assignement',4,'p_assignement_moinsaff','plyyacc.py',44),
  ('assignement -> ID DREBFIH expression NO9TAFASSILA','assignement',4,'p_assignement_timessaff','plyyacc.py',48),
  ('assignement -> ID 9SSEMFIH expression NO9TAFASSILA','assignement',4,'p_assignement_divsaff','plyyacc.py',52),
  ('assignement -> ID ZIDWA7ED NO9TAFASSILA','assignement',3,'p_assignement_incrementation','plyyacc.py',56),
  ('assignement -> ID N9ESSWA7ED NO9TAFASSILA','assignement',3,'p_assignement_decrementation','plyyacc.py',60),
  ('expression_string -> expression','expression_string',1,'p_expression_string','plyyacc.py',64),
  ('expression_string -> STRING','expression_string',1,'p_expression_string','plyyacc.py',65),
  ('expression_string -> boolean','expression_string',1,'p_expression_string','plyyacc.py',66),
  ('printing -> KTEB 7EL9AWESS expression_string SED9AWESS NO9TAFASSILA','printing',5,'p_printing','plyyacc.py',72),
  ('expression -> NA9ISS expression','expression',2,'p_expression_negatif','plyyacc.py',76),
  ('statement -> ILA 7EL9AWESS boolean SED9AWESS 7ELLAMA statements SEDLAMA','statement',7,'p_statement_if','plyyacc.py',80),
  ('statement -> ILA 7EL9AWESS boolean SED9AWESS statement MNGHIRDAKCHI statement','statement',7,'p_statement_if','plyyacc.py',81),
  ('statement -> MADAM 7EL9AWESS boolean SED9AWESS 7ELLAMA statements SEDLAMA','statement',7,'p_statement_while','plyyacc.py',89),
  ('expression -> 7EL9AWESS expression SED9AWESS','expression',3,'p_expression_paren','plyyacc.py',96),
  ('expression -> expression ZA2ID term','expression',3,'p_expression_plus','plyyacc.py',99),
  ('expression -> expression NA9ISS term','expression',3,'p_expression_minus','plyyacc.py',104),
  ('expression -> term','expression',1,'p_expression_term','plyyacc.py',108),
  ('term -> term BA9IL9ISSMA factor','term',3,'p_term_modulo','plyyacc.py',112),
  ('term -> term DREB factor','term',3,'p_term_times','plyyacc.py',116),
  ('term -> term 9SSEM factor','term',3,'p_term_div','plyyacc.py',120),
  ('term -> ID','term',1,'p_term_ID','plyyacc.py',128),
  ('term -> factor','term',1,'p_term_factor','plyyacc.py',132),
  ('factor -> 7EL9AWESS expression SED9AWESS','factor',3,'p_factor_expr','plyyacc.py',136),
  ('factor -> RA9M','factor',1,'p_factor_num','plyyacc.py',140),
  ('boolean -> S7I7','boolean',1,'p_boolean','plyyacc.py',144),
  ('boolean -> GHALAT','boolean',1,'p_boolean','plyyacc.py',145),
  ('boolean -> ID YUSSAWI2 boolean','boolean',3,'p_comparison','plyyacc.py',151),
  ('boolean -> ID MAKAYSSAWICH boolean','boolean',3,'p_comparison','plyyacc.py',152),
  ('boolean -> boolean YUSSAWI2 ID','boolean',3,'p_comparison','plyyacc.py',153),
  ('boolean -> boolean MAKAYSSAWICH ID','boolean',3,'p_comparison','plyyacc.py',154),
  ('boolean -> ID YUSSAWI2 ID','boolean',3,'p_comparison','plyyacc.py',155),
  ('boolean -> ID MAKAYSSAWICH ID','boolean',3,'p_comparison','plyyacc.py',156),
  ('boolean -> boolean YUSSAWI2 boolean','boolean',3,'p_comparison','plyyacc.py',157),
  ('boolean -> boolean MAKAYSSAWICH boolean','boolean',3,'p_comparison','plyyacc.py',158),
  ('boolean -> expression YUSSAWI2 expression','boolean',3,'p_comparison','plyyacc.py',159),
  ('boolean -> expression MAKAYSSAWICH expression','boolean',3,'p_comparison','plyyacc.py',160),
  ('boolean -> expression KTERMN expression','boolean',3,'p_comparison','plyyacc.py',161),
  ('boolean -> expression 9ELMN expression','boolean',3,'p_comparison','plyyacc.py',162),
  ('boolean -> expression KTERYUSSAWI expression','boolean',3,'p_comparison','plyyacc.py',163),
  ('boolean -> expression 9ELYUSSAWI expression','boolean',3,'p_comparison','plyyacc.py',164),
]