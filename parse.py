import ply.yacc as yacc
from lexer import tokens

def p_program(p):
    'program : statement_list'
    p[0] = ('program', p[1])

def p_statement_list(p):
    '''statement_list : statement_list statement
                      | statement'''
    if len(p) == 3:
        p[0] = p[1] + p[2]
    else:
        p[0] = [p[1]]

def p_statement(p):
    '''statement : declaration
                 | function_definition
                 | conditional
                 | loop
                 | print_statement'''
    p[0] = p[1]

def p_declaration(p):
    '''declaration : type COLON ID EQUAL expression SEMICOLON'''
    p[0] = ('declaration', p[1], p[3], p[5])

def p_type(p):
    '''type : INT
            | FLOAT
            | STRING
            | CHAR
            | BOOL'''
    p[0] = p[1]

def p_boolean(p):
    '''boolean : TRUE
               | FALSE'''
    p[0] = p[1]

def p_function_definition(p):
    'function_definition : FUNCTION ID LPAREN RPAREN LBRACE statement_list RBRACE'
    p[0] = ('function_definition', p[2], p[6])

def p_conditional(p):
    'conditional : ASSUMING expression LBRACE statement_list RBRACE otherwise_block'
    p[0] = ('conditional', p[2], p[4], p[6])

def p_otherwise_block(p):
    '''otherwise_block : OTHERWISE LBRACE statement_list RBRACE
                       | empty'''
    p[0] = p[3] if len(p) > 2 else ('otherwise',)

def p_loop(p):
    'loop : LOOP LPAREN expression RPAREN LBRACE statement_list RBRACE'
    p[0] = ('loop', p[3], p[6])

def p_print_statement(p):
    'print_statement : PRINT LPAREN expression RPAREN SEMICOLON'
    p[0] = ('print_statement', p[3])

def p_expression(p):
    '''expression : ID
                  | NUMBER
                  | STRING_LITERAL
                  | CHAR_LITERAL
                  | boolean
                  | binary_expression'''
    p[0] = p[1]

def p_binary_expression(p):
    '''binary_expression : expression PLUS expression
                         | expression MINUS expression
                         | expression TIMES expression
                         | expression DIVIDE expression
                         | expression EQ expression
                         | expression NEQ expression
                         | expression GT expression
                         | expression LT expression
                         | expression GTE expression
                         | expression LTE expression'''
    p[0] = ('binary_expression', p[2], p[1], p[3])

def p_empty(p):
    'empty :'
    pass

def stringify_ast(node, level=0):
    if isinstance(node, tuple):
        return f"{' ' * (level * 2)}{node[0]}\n" + "\n".join(stringify_ast(child, level+1) for child in node[1:])
    else:
        return f"{' ' * (level * 2)}{node}"

def p_error(p):
    print(f"Syntax error at {p.value!r}")

parser = yacc.yacc()