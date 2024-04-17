import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from lark import Lark
from tkinter import scrolledtext, messagebox
from grammar import argon_grammar
from lexer import lexer
from parse import parser, stringify_ast
from ATransformer import MyTransformer

def setup_ui(app):
    global txt_input, txt_output

    txt_input = scrolledtext.ScrolledText(app, height=10, width=60)
    txt_input.pack(padx=10, pady=10)

    button_frame = tk.Frame(app)
    button_frame.pack(padx=10, pady=5, fill=tk.X)

    btn_lexical = tk.Button(button_frame, text="Análisis Léxico", command=lexical_analysis)
    btn_lexical.pack(side=tk.LEFT, padx=10)

    btn_syntactic = tk.Button(button_frame, text="Análisis Sintáctico", command=syntactic_analysis)
    btn_syntactic.pack(side=tk.LEFT, padx=10)

    btn_semantic = tk.Button(button_frame, text="Intérprete Semántico", command=semantic_analysis)
    btn_semantic.pack(side=tk.LEFT, padx=10)

    txt_output = ScrolledText(app, height=10)
    txt_output.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

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

    full_message = ("\n".join([
        str(transformer.mensaje_funcion),
        str(transformer.mensaje_if),
        str(transformer.mensaje_loop),
        str(transformer.mensaje_loopdos),
        str(transformer.mensaje_variable)
    ]))

    txt_output.delete("1.0", tk.END)
    txt_output.insert(tk.END, full_message)
    txt_output.yview(tk.MOVETO, 0.0)

app = tk.Tk()
app.title("ARGON Language IDE")
setup_ui(app)
app.mainloop()

