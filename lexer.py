import ply.lex as lex

tokens = (
    'INT', 'FLOAT', 'STRING', 'CHAR', 'BOOL', 'FUNCTION',
    'ASSUMING', 'OTHERWISE', 'LOOP', 'TRUE', 'FALSE',
    'ID', 'NUMBER', 'STRING_LITERAL', 'CHAR_LITERAL',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'EQUAL', 'COMMA', 'SEMICOLON',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'COLON', 'DOT',
    'EQ', 'NEQ', 'GT', 'LT', 'GTE', 'LTE'
)

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUAL = r'='
t_COMMA = r','
t_SEMICOLON = r';'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COLON = r':'
t_DOT = r'\.'
t_EQ = r'=='
t_NEQ = r'!='
t_GT = r'>'
t_LT = r'<'
t_GTE = r'>='
t_LTE = r'<='

t_STRING_LITERAL = r'\"([^\\\n]|(\\.))*?\"'
t_CHAR_LITERAL = r"\'([^\\\n]|(\\.))*?\'"

reserved = {
    'int': 'INT', 'float': 'FLOAT', 'string': 'STRING', 'char': 'CHAR', 'bool': 'BOOL',
    'function': 'FUNCTION', 'assuming': 'ASSUMING', 'otherwise': 'OTHERWISE', 'loop': 'LOOP',
    'true': 'TRUE', 'false': 'FALSE', 'print': 'PRINT'
}

tokens += tuple(reserved.values())

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()