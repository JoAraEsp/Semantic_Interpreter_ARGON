from lark import Transformer, Tree, Token
import lark
class MyTransformer(Transformer):
    def __init__(self):
        self.variables = {}
        self.functions = {}
        self.statements = []
        self.tokens = []
        self.mensaje_variable = ""
        self.mensaje_funcion = ""
        self.mensaje_if = ""
        self.mensaje_loop = ""
        self.mensaje_loopdos = ""

    def variable_declaration(self, items):
        print(items)

        var_type = items[0].value.lower()

        var_name = items[1].value

        if items[2].children:
            raw_value = items[2].children[0].value
        else:
            raw_value = items[2].value

        print(f"Extracted values - Type: {var_type}, Name: {var_name}, Value: {raw_value}")

        try:
            if var_type == "int":
                var_value = int(raw_value)
            elif var_type == "float":
                var_value = float(raw_value)
            elif var_type == "string":
                var_value = raw_value.strip("'").strip('"')
            elif var_type == "char":
                var_value = raw_value[0] if raw_value else ''
            elif var_type == "bool":
                var_value = raw_value.lower() in ("true", "1")
            else:
                raise ValueError(f"Tipo no soportado: {var_type}")
        except ValueError as e:
            print(f"Error al convertir el valor: {e}")
            return None

        self.variables[var_name] = var_value

        mensaje = f"Variable '{var_name}' declarada con valor {var_value}\n"
        self.mensaje_variable += mensaje

        return (var_name, var_value)

    def function_declaration(self, items):
        func_name = items[0]  
        parameters = items[1] if len(items) > 1 and isinstance(items[1], Tree) and items[1].data == 'parameter_list' else None
        body = items[2] if len(items) > 2 else (items[1] if len(items) > 1 and not parameters else None)
 
        param_str = ", ".join(p.children[0].value for p in parameters.children) if parameters else "Sin parámetros"
        body_str = self._stringify_body(body.children) if body else "Cuerpo vacío"
        self.mensaje_funcion = f"Declaración de función '{func_name.value}' con parámetros ({param_str}) y cuerpo: {body_str}"
    
        self.functions[func_name.value] = {
            'parameters': [p.children[0].value for p in parameters.children] if parameters else [],
            'body': body.children if body else []
        }
        
        return func_name.value, [p.children[0].value for p in parameters.children] if parameters else [], body.children if body else []

    def _stringify_body(self, statements):
        if statements:
            return " ".join(f"{stmt.data}: {' '.join(child.value if isinstance(child, Token) else str(child) for child in stmt.children)}" for stmt in statements)
        return "Cuerpo vacío"

    def print_statement(self, items):
        expression = items[0]
        evaluated_expression = self.evaluate_expression(expression)
        print_output = f"print: {evaluated_expression}"
        return print_output

    def evaluate_expression(self, expression):
        if isinstance(expression, Token):
            return expression.value
        elif isinstance(expression, Tree):
            if expression.data == 'expression' and len(expression.children) == 3:
                left, op, right = expression.children
                left_val = self.evaluate_expression(left)
                right_val = self.evaluate_expression(right)
                return self.apply_operator(left_val, op.value, right_val)
            else:
                return self.evaluate_expression(expression.children[0])
        return str(expression)

    def apply_operator(self, left, operator, right):
        left = float(left) if '.' in left else int(left)
        right = float(right) if '.' in right else int(right)
        if operator == '+':
            return left + right
        elif operator == '-':
            return left - right
        elif operator == '*':
            return left * right
        elif operator == '/':
            return left / right

    def conditional_declaration(self, items):
        condition = items[0]
        true_block = items[1].children
        false_block = items[2].children if len(items) > 2 else None

        if self.evaluate_condition(condition):
            true_results = [self.transform(statement) for statement in true_block]
            true_results_str = "\n".join(map(str, true_results))
            self.mensaje_if = f"La condición 'assuming' es verdadera. Resultados:\n{true_results_str}"
        else:
            if false_block:
                false_results = [self.transform(statement) for statement in false_block]
                false_results_str = "\n".join(map(str, false_results))
                self.mensaje_if = f"La condición 'assuming' es falsa. Resultados:\n{false_results_str}"
            else:
                self.mensaje_if = "La condición 'assuming' es falsa y no hay bloque 'otherwise'."

    def loop_declaration(self, items):
        condition = items[0]
        body_statements = items[1].children if len(items) > 1 else []

        outputs = []  
        self.mensaje_loop = "Evaluando bucle loop: "
        loop_count = 0

        while self.evaluate_condition(condition) and loop_count < 100:
            iteration_outputs = []  
            for statement in body_statements:
                output = self.transform(statement)  
                if isinstance(output, Tree):
                    output = self.tree_to_string(output)  
                iteration_outputs.append(output)

            outputs.extend(iteration_outputs)
            self.increment_control_variable(condition)  
            loop_count += 1

        if loop_count == 0:
            self.mensaje_loop += "La condición inicial del bucle loop es falsa; no se ejecuta el cuerpo."
        else:
            self.mensaje_loop += f"Se ejecutaron {loop_count} iteraciones hasta que la condición fue falsa o se alcanzó el límite.\n" + "\n".join(map(str, outputs))

    def tree_to_string(self, tree):
        if isinstance(tree, Token):
            
            return tree.value
        elif isinstance(tree, Tree):
            
            parts = []
            for child in tree.children:
                if isinstance(child, Token):
                    
                    parts.append(child.value)
                elif isinstance(child, Tree):
                    
                    parts.append(self.tree_to_string(child))
                else:
                  
                    parts.append(str(child))
       
            return ' '.join(parts)
        return str(tree) 


    def increment_control_variable(self, condition):
        var_name = condition.children[0].value  
        if var_name in self.variables:
            self.variables[var_name] += 1  


    def evaluate_condition(self, condition):
        if not condition.children or len(condition.children) < 3:
            raise ValueError("Condición mal formada, faltan componentes.")
        
        identifier = condition.children[0].value  
        operator = condition.children[1].value   
        value_node = condition.children[2]      

        identifier_value = self.variables.get(identifier)

        if identifier_value is None:
            print(f"Variable {identifier} no definida.")
            return False

        comparison_value = self.extract_value(value_node.children[0] if isinstance(value_node, lark.Tree) else value_node)

        if type(identifier_value) != type(comparison_value):
            print(f"No se puede comparar {identifier_value} ({type(identifier_value)}) y {comparison_value} ({type(comparison_value)}) debido a incompatibilidad de tipos.")
            return False

        return self.apply_comparator(identifier_value, operator, comparison_value)


    def extract_value(self, node):
        if isinstance(node, lark.lexer.Token):
            if node.type == 'INT_NUMBER':
                return int(node.value)
            elif node.type == 'FLOAT_NUMBER':
                return float(node.value)
            elif node.type == 'STRING':
                return node.value.strip("'").strip('"')  
            elif node.type == 'BOOLEAN':
                return node.value.lower() in ['true', '1']  
            else:
                raise ValueError(f"No se puede manejar el tipo de token: {node.type}")
        else:
            raise TypeError(f"Se esperaba un Token, pero se obtuvo: {type(node)}")


    def apply_comparator(self, left, operator, right):
        if operator == "==":
            return left == right
        elif operator == "!=":
            return left != right
        elif operator == ">":
            return left > right
        elif operator == "<":
            return left < right
        elif operator == ">=":
            return left >= right
        elif operator == "<=":
            return left <= right
        else:
            raise ValueError(f"Operador no soportado: {operator}")
        