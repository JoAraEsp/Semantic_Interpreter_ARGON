argon_grammar = """
start: instruction+

instruction: variable_declaration
           | function_declaration
           | conditional_declaration
           | loop_declaration

variable_declaration: type IDENTIFIER EQUAL value ";"
type: "int" | "float" | "string" | "char" | "bool"
value: INT_NUMBER | FLOAT_NUMBER | STRING | BOOLEAN

function_declaration: "function" IDENTIFIER "(" [parameter_list] ")" "{" [statement_list] "}"
conditional_declaration: "assuming"  condition  "{" [statement_list] "}" [else_block]
loop_declaration: "loop" "(" condition ")" "{" statement_list "}"

parameter_list: IDENTIFIER ("," IDENTIFIER)*
statement_list: (statement ";")+
statement: print_statement | variable_declaration | expression

print_statement: "print" "(" expression ")"
else_block: "otherwise" "{" statement_list "}"

condition: IDENTIFIER (COMPARATOR value)+
expression: value | value OPERATOR value | IDENTIFIER

INT_NUMBER: /[0-9]+/
FLOAT_NUMBER: /[0-9]*\.[0-9]+/
STRING: /'(?:\\.|[^\\'])*'/
BOOLEAN: "true" | "false"
IDENTIFIER: /[a-zA-Z_][a-zA-Z0-9_]*/
COMPARATOR: "==" | "!=" | ">=" | "<=" | ">" | "<"
OPERATOR: "+" | "-" | "*" | "/"
EQUAL: "="

%import common.WS
%import common.EQUAL
%ignore WS
"""

