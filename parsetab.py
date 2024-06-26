
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ASSUMING ASSUMING BOOL BOOL CHAR CHAR CHAR_LITERAL COLON COMMA DIVIDE DOT EQ EQUAL FALSE FALSE FLOAT FLOAT FUNCTION FUNCTION GT GTE ID INT INT LBRACE LOOP LOOP LPAREN LT LTE MINUS NEQ NUMBER OTHERWISE OTHERWISE PLUS PRINT RBRACE RPAREN SEMICOLON STRING STRING STRING_LITERAL TIMES TRUE TRUEprogram : statement_liststatement_list : statement_list statement\n                      | statementstatement : declaration\n                 | function_definition\n                 | conditional\n                 | loop\n                 | print_statementdeclaration : type ID EQUAL expression SEMICOLONtype : INT\n            | FLOAT\n            | STRING\n            | CHAR\n            | BOOLboolean : TRUE\n               | FALSEfunction_definition : FUNCTION ID LPAREN RPAREN LBRACE statement_list RBRACEconditional : ASSUMING expression LBRACE statement_list RBRACE otherwise_blockotherwise_block : OTHERWISE LBRACE statement_list RBRACE\n                       | emptyloop : LOOP LPAREN expression RPAREN LBRACE statement_list RBRACEprint_statement : PRINT LPAREN expression RPAREN SEMICOLONexpression : ID\n                  | NUMBER\n                  | STRING_LITERAL\n                  | CHAR_LITERAL\n                  | boolean\n                  | binary_expressionbinary_expression : expression PLUS expression\n                         | expression MINUS expression\n                         | expression TIMES expression\n                         | expression DIVIDE expression\n                         | expression EQ expression\n                         | expression NEQ expression\n                         | expression GT expression\n                         | expression LT expression\n                         | expression GTE expression\n                         | expression LTE expressionempty :'
    
_lr_action_items = {'FUNCTION':([0,2,3,4,5,6,7,8,19,35,50,63,64,65,66,67,68,69,71,72,73,74,75,76,77,],[10,10,-3,-4,-5,-6,-7,-8,-2,10,10,-9,10,-39,10,-22,10,-18,-20,10,-17,10,-21,10,-19,]),'ASSUMING':([0,2,3,4,5,6,7,8,19,35,50,63,64,65,66,67,68,69,71,72,73,74,75,76,77,],[11,11,-3,-4,-5,-6,-7,-8,-2,11,11,-9,11,-39,11,-22,11,-18,-20,11,-17,11,-21,11,-19,]),'LOOP':([0,2,3,4,5,6,7,8,19,35,50,63,64,65,66,67,68,69,71,72,73,74,75,76,77,],[12,12,-3,-4,-5,-6,-7,-8,-2,12,12,-9,12,-39,12,-22,12,-18,-20,12,-17,12,-21,12,-19,]),'PRINT':([0,2,3,4,5,6,7,8,19,35,50,63,64,65,66,67,68,69,71,72,73,74,75,76,77,],[13,13,-3,-4,-5,-6,-7,-8,-2,13,13,-9,13,-39,13,-22,13,-18,-20,13,-17,13,-21,13,-19,]),'INT':([0,2,3,4,5,6,7,8,19,35,50,63,64,65,66,67,68,69,71,72,73,74,75,76,77,],[14,14,-3,-4,-5,-6,-7,-8,-2,14,14,-9,14,-39,14,-22,14,-18,-20,14,-17,14,-21,14,-19,]),'FLOAT':([0,2,3,4,5,6,7,8,19,35,50,63,64,65,66,67,68,69,71,72,73,74,75,76,77,],[15,15,-3,-4,-5,-6,-7,-8,-2,15,15,-9,15,-39,15,-22,15,-18,-20,15,-17,15,-21,15,-19,]),'STRING':([0,2,3,4,5,6,7,8,19,35,50,63,64,65,66,67,68,69,71,72,73,74,75,76,77,],[16,16,-3,-4,-5,-6,-7,-8,-2,16,16,-9,16,-39,16,-22,16,-18,-20,16,-17,16,-21,16,-19,]),'CHAR':([0,2,3,4,5,6,7,8,19,35,50,63,64,65,66,67,68,69,71,72,73,74,75,76,77,],[17,17,-3,-4,-5,-6,-7,-8,-2,17,17,-9,17,-39,17,-22,17,-18,-20,17,-17,17,-21,17,-19,]),'BOOL':([0,2,3,4,5,6,7,8,19,35,50,63,64,65,66,67,68,69,71,72,73,74,75,76,77,],[18,18,-3,-4,-5,-6,-7,-8,-2,18,18,-9,18,-39,18,-22,18,-18,-20,18,-17,18,-21,18,-19,]),'$end':([1,2,3,4,5,6,7,8,19,63,65,67,69,71,73,75,77,],[0,-1,-3,-4,-5,-6,-7,-8,-2,-9,-39,-22,-18,-20,-17,-21,-19,]),'RBRACE':([3,4,5,6,7,8,19,50,63,65,67,68,69,71,72,73,75,76,77,],[-3,-4,-5,-6,-7,-8,-2,65,-9,-39,-22,73,-18,-20,75,-17,-21,77,-19,]),'ID':([9,10,11,14,15,16,17,18,31,32,33,36,37,38,39,40,41,42,43,44,45,],[20,21,23,-10,-11,-12,-13,-14,23,23,23,23,23,23,23,23,23,23,23,23,23,]),'NUMBER':([11,31,32,33,36,37,38,39,40,41,42,43,44,45,],[24,24,24,24,24,24,24,24,24,24,24,24,24,24,]),'STRING_LITERAL':([11,31,32,33,36,37,38,39,40,41,42,43,44,45,],[25,25,25,25,25,25,25,25,25,25,25,25,25,25,]),'CHAR_LITERAL':([11,31,32,33,36,37,38,39,40,41,42,43,44,45,],[26,26,26,26,26,26,26,26,26,26,26,26,26,26,]),'TRUE':([11,31,32,33,36,37,38,39,40,41,42,43,44,45,],[29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'FALSE':([11,31,32,33,36,37,38,39,40,41,42,43,44,45,],[30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'LPAREN':([12,13,21,],[31,32,34,]),'EQUAL':([20,],[33,]),'LBRACE':([22,23,24,25,26,27,28,29,30,49,51,52,53,54,55,56,57,58,59,60,61,70,],[35,-23,-24,-25,-26,-27,-28,-15,-16,64,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,66,74,]),'PLUS':([22,23,24,25,26,27,28,29,30,46,47,48,51,52,53,54,55,56,57,58,59,60,],[36,-23,-24,-25,-26,-27,-28,-15,-16,36,36,36,36,36,36,36,36,36,36,36,36,36,]),'MINUS':([22,23,24,25,26,27,28,29,30,46,47,48,51,52,53,54,55,56,57,58,59,60,],[37,-23,-24,-25,-26,-27,-28,-15,-16,37,37,37,37,37,37,37,37,37,37,37,37,37,]),'TIMES':([22,23,24,25,26,27,28,29,30,46,47,48,51,52,53,54,55,56,57,58,59,60,],[38,-23,-24,-25,-26,-27,-28,-15,-16,38,38,38,38,38,38,38,38,38,38,38,38,38,]),'DIVIDE':([22,23,24,25,26,27,28,29,30,46,47,48,51,52,53,54,55,56,57,58,59,60,],[39,-23,-24,-25,-26,-27,-28,-15,-16,39,39,39,39,39,39,39,39,39,39,39,39,39,]),'EQ':([22,23,24,25,26,27,28,29,30,46,47,48,51,52,53,54,55,56,57,58,59,60,],[40,-23,-24,-25,-26,-27,-28,-15,-16,40,40,40,40,40,40,40,40,40,40,40,40,40,]),'NEQ':([22,23,24,25,26,27,28,29,30,46,47,48,51,52,53,54,55,56,57,58,59,60,],[41,-23,-24,-25,-26,-27,-28,-15,-16,41,41,41,41,41,41,41,41,41,41,41,41,41,]),'GT':([22,23,24,25,26,27,28,29,30,46,47,48,51,52,53,54,55,56,57,58,59,60,],[42,-23,-24,-25,-26,-27,-28,-15,-16,42,42,42,42,42,42,42,42,42,42,42,42,42,]),'LT':([22,23,24,25,26,27,28,29,30,46,47,48,51,52,53,54,55,56,57,58,59,60,],[43,-23,-24,-25,-26,-27,-28,-15,-16,43,43,43,43,43,43,43,43,43,43,43,43,43,]),'GTE':([22,23,24,25,26,27,28,29,30,46,47,48,51,52,53,54,55,56,57,58,59,60,],[44,-23,-24,-25,-26,-27,-28,-15,-16,44,44,44,44,44,44,44,44,44,44,44,44,44,]),'LTE':([22,23,24,25,26,27,28,29,30,46,47,48,51,52,53,54,55,56,57,58,59,60,],[45,-23,-24,-25,-26,-27,-28,-15,-16,45,45,45,45,45,45,45,45,45,45,45,45,45,]),'RPAREN':([23,24,25,26,27,28,29,30,34,46,47,51,52,53,54,55,56,57,58,59,60,],[-23,-24,-25,-26,-27,-28,-15,-16,49,61,62,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,]),'SEMICOLON':([23,24,25,26,27,28,29,30,48,51,52,53,54,55,56,57,58,59,60,62,],[-23,-24,-25,-26,-27,-28,-15,-16,63,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,67,]),'OTHERWISE':([65,],[70,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'statement_list':([0,35,64,66,74,],[2,50,68,72,76,]),'statement':([0,2,35,50,64,66,68,72,74,76,],[3,19,3,19,3,3,19,19,3,19,]),'declaration':([0,2,35,50,64,66,68,72,74,76,],[4,4,4,4,4,4,4,4,4,4,]),'function_definition':([0,2,35,50,64,66,68,72,74,76,],[5,5,5,5,5,5,5,5,5,5,]),'conditional':([0,2,35,50,64,66,68,72,74,76,],[6,6,6,6,6,6,6,6,6,6,]),'loop':([0,2,35,50,64,66,68,72,74,76,],[7,7,7,7,7,7,7,7,7,7,]),'print_statement':([0,2,35,50,64,66,68,72,74,76,],[8,8,8,8,8,8,8,8,8,8,]),'type':([0,2,35,50,64,66,68,72,74,76,],[9,9,9,9,9,9,9,9,9,9,]),'expression':([11,31,32,33,36,37,38,39,40,41,42,43,44,45,],[22,46,47,48,51,52,53,54,55,56,57,58,59,60,]),'boolean':([11,31,32,33,36,37,38,39,40,41,42,43,44,45,],[27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'binary_expression':([11,31,32,33,36,37,38,39,40,41,42,43,44,45,],[28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'otherwise_block':([65,],[69,]),'empty':([65,],[71,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statement_list','program',1,'p_program','parse.py',5),
  ('statement_list -> statement_list statement','statement_list',2,'p_statement_list','parse.py',9),
  ('statement_list -> statement','statement_list',1,'p_statement_list','parse.py',10),
  ('statement -> declaration','statement',1,'p_statement','parse.py',17),
  ('statement -> function_definition','statement',1,'p_statement','parse.py',18),
  ('statement -> conditional','statement',1,'p_statement','parse.py',19),
  ('statement -> loop','statement',1,'p_statement','parse.py',20),
  ('statement -> print_statement','statement',1,'p_statement','parse.py',21),
  ('declaration -> type ID EQUAL expression SEMICOLON','declaration',5,'p_declaration','parse.py',25),
  ('type -> INT','type',1,'p_type','parse.py',29),
  ('type -> FLOAT','type',1,'p_type','parse.py',30),
  ('type -> STRING','type',1,'p_type','parse.py',31),
  ('type -> CHAR','type',1,'p_type','parse.py',32),
  ('type -> BOOL','type',1,'p_type','parse.py',33),
  ('boolean -> TRUE','boolean',1,'p_boolean','parse.py',37),
  ('boolean -> FALSE','boolean',1,'p_boolean','parse.py',38),
  ('function_definition -> FUNCTION ID LPAREN RPAREN LBRACE statement_list RBRACE','function_definition',7,'p_function_definition','parse.py',42),
  ('conditional -> ASSUMING expression LBRACE statement_list RBRACE otherwise_block','conditional',6,'p_conditional','parse.py',46),
  ('otherwise_block -> OTHERWISE LBRACE statement_list RBRACE','otherwise_block',4,'p_otherwise_block','parse.py',50),
  ('otherwise_block -> empty','otherwise_block',1,'p_otherwise_block','parse.py',51),
  ('loop -> LOOP LPAREN expression RPAREN LBRACE statement_list RBRACE','loop',7,'p_loop','parse.py',55),
  ('print_statement -> PRINT LPAREN expression RPAREN SEMICOLON','print_statement',5,'p_print_statement','parse.py',59),
  ('expression -> ID','expression',1,'p_expression','parse.py',63),
  ('expression -> NUMBER','expression',1,'p_expression','parse.py',64),
  ('expression -> STRING_LITERAL','expression',1,'p_expression','parse.py',65),
  ('expression -> CHAR_LITERAL','expression',1,'p_expression','parse.py',66),
  ('expression -> boolean','expression',1,'p_expression','parse.py',67),
  ('expression -> binary_expression','expression',1,'p_expression','parse.py',68),
  ('binary_expression -> expression PLUS expression','binary_expression',3,'p_binary_expression','parse.py',72),
  ('binary_expression -> expression MINUS expression','binary_expression',3,'p_binary_expression','parse.py',73),
  ('binary_expression -> expression TIMES expression','binary_expression',3,'p_binary_expression','parse.py',74),
  ('binary_expression -> expression DIVIDE expression','binary_expression',3,'p_binary_expression','parse.py',75),
  ('binary_expression -> expression EQ expression','binary_expression',3,'p_binary_expression','parse.py',76),
  ('binary_expression -> expression NEQ expression','binary_expression',3,'p_binary_expression','parse.py',77),
  ('binary_expression -> expression GT expression','binary_expression',3,'p_binary_expression','parse.py',78),
  ('binary_expression -> expression LT expression','binary_expression',3,'p_binary_expression','parse.py',79),
  ('binary_expression -> expression GTE expression','binary_expression',3,'p_binary_expression','parse.py',80),
  ('binary_expression -> expression LTE expression','binary_expression',3,'p_binary_expression','parse.py',81),
  ('empty -> <empty>','empty',0,'p_empty','parse.py',85),
]
