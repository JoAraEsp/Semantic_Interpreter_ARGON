import tkinter as tk
from lark import Lark
from tkinter import scrolledtext, messagebox
from grammar import argon_grammar
from lexer import lexer
from parse import parser, stringify_ast
from ATransformer import MyTransformer

def lexical_analysis():
    code = txt_input.get("1.0", tk.END)
    lexer.input(code)
    tokens = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens.append(str(tok))
    messagebox.showinfo("Análisis Léxico", "\n".join(tokens))

def syntactic_analysis():
    code = txt_input.get("1.0", tk.END)
    lexer.input(code)
    ast = parser.parse(code, lexer=lexer)
    formatted_ast = stringify_ast(ast)
    messagebox.showinfo("Análisis Sintáctico", formatted_ast)

def semantic_analysis():
    code = txt_input.get("1.0", tk.END)
    transformer = MyTransformer()
    parser2 = Lark(argon_grammar, start='start', parser='earley')
    tree = parser2.parse(code)
    transformer.transform(tree)
    print(transformer.mensaje_funcion)
    print(transformer.mensaje_if)
    print(transformer.mensaje_loop)
    print(transformer.mensaje_variable)

app = tk.Tk()
app.title("ARGON Language IDE")

frame = tk.Frame(app)
frame.pack(padx=20, pady=20)

txt_input = scrolledtext.ScrolledText(frame, height=10, width=60)
txt_input.pack()

btn_lexical = tk.Button(frame, text="Análisis Léxico", command=lexical_analysis)
btn_lexical.pack(side=tk.LEFT, padx=10)

btn_syntactic = tk.Button(frame, text="Análisis Sintáctico", command=syntactic_analysis)
btn_syntactic.pack(side=tk.LEFT, padx=10)

btn_semantic = tk.Button(frame, text="Intérprete Semántico", command=semantic_analysis)
btn_semantic.pack(side=tk.LEFT, padx=10)

app.mainloop()
