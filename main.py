import tkinter as tk
from tkinter import scrolledtext, messagebox
from lexer import lexer
from parse import parser, stringify_ast
from interpreter import interpret

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
    lexer.input(code)
    ast = parser.parse(code, lexer=lexer)
    result = interpret(ast)
    txt_input.delete("1.0", tk.END)  
    txt_input.insert("1.0", result)  
    
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

btn_semantic = tk.Button(frame, text="Análisis Semántico", command=semantic_analysis)
btn_semantic.pack(side=tk.LEFT, padx=10)

app.mainloop()
