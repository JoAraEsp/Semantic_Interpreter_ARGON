from lark import Transformer, Tree, Token
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
                self.mensaje_if = "La condición 'assuming' es verdadera.", true_results
            else:
                if false_block:
                    false_results = [self.transform(statement) for statement in false_block]
                    self.mensaje_if = "La condición 'assuming' es falsa.", false_results
                else:
                    self.mensaje_if = "La condición 'assuming' es falsa y no hay bloque 'otherwise'."

    def loop_declaration(self, items):
        condition = items[0]
        body_statements = items[1].children if len(items) > 1 else []

        self.mensaje_loop = "Evaluando bucle loop: "
        loop_count = 0  

        while self.evaluate_condition(condition) and loop_count < 100:
            for statement in body_statements:
                result = self.transform(statement)
                self.statements.append(result)
            self.mensaje_loop += f"Iteración {loop_count + 1} ejecutada. "
            loop_count += 1

        if loop_count == 0:
            self.mensaje_loop += "La condición inicial del bucle loop es falsa; no se ejecuta el cuerpo."
        else:
            self.mensaje_loop += f"Se ejecutaron {loop_count} iteraciones hasta que la condición fue falsa o se alcanzó el límite."

        return self.mensaje_loop

    def evaluate_condition(self, condition):
        if not condition.children:
            raise ValueError("Condición mal formada, faltan componentes.")
        
        identifier = condition.children[0]
        operator = condition.children[1]
        value = condition.children[2]

        identifier_value = self.variables.get(identifier.value)

        if identifier_value is None:
            print(f"Variable {identifier.value} no definida.")
            return False

        value_value = self.extract_value(value)

        if isinstance(identifier_value, (int, float)) and isinstance(value_value, (int, float)):
            return self.apply_comparator(float(identifier_value), operator.value, float(value_value))
        else:
            print(f"No se puede comparar {identifier_value} y {value_value} debido a incompatibilidad de tipos.")
            return False

    def extract_value(self, value):
        if isinstance(value, Tree) and value.data == 'INT_NUMBER':
            return int(value.children[0])
        elif isinstance(value, Tree) and value.data == 'FLOAT_NUMBER':
            return float(value.children[0])
        elif isinstance(value, Tree) and value.data == 'BOOLEAN':
            return value.children[0].lower() == 'true'
        return value.children[0]  

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
            raise ValueError(f"Unsupported operator: {operator}")
        