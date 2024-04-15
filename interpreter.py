import operator

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '==': operator.eq,
    '!=': operator.ne,
    '>': operator.gt,
    '<': operator.lt,
    '>=': operator.ge,
    '<=': operator.le,
}

def interpret(statements, context=None):
    if context is None:
        context = {}
    outputs = []
    for statement in statements:
        st_type = statement[0]
        if st_type == 'declaration':
            output = interpret_declaration(statement, context)
        elif st_type == 'function_definition':
            output = interpret_function_definition(statement, context)
        elif st_type == 'conditional':
            output = interpret_conditional(statement, context)
        elif st_type == 'loop':
            output = interpret_loop(statement, context)
        elif st_type == 'print_statement':
            output = interpret_print_statement(statement, context)
        else:
            raise ValueError(f"Unrecognized statement type: {st_type}")
        if output is not None:
            outputs.append(output)
    return "\n".join(outputs)

def interpret_declaration(statement, context):
    _, var_type, var_name, value = statement
    evaluated_value = evaluate_expression(value, context)
    if is_type_correct(var_type, evaluated_value):
        context[var_name] = evaluated_value
        return f"{var_type} {var_name} = {evaluated_value}"
    else:
        raise TypeError(f"Incorrect type for variable '{var_name}'. Expected {var_type}, got {type(evaluated_value).__name__}")

def interpret_function_definition(statement, context):
    _, func_name, func_body = statement
    context[func_name] = func_body
    return f"Function {func_name} defined."

def interpret_conditional(statement, context):
    _, condition, true_block, false_block = statement
    condition_result = evaluate_expression(condition, context)
    if condition_result:
        return interpret(true_block, context)
    elif false_block is not None:
        return interpret(false_block, context)
    return None

def interpret_loop(statement, context):
    _, condition, loop_block = statement
    loop_outputs = []
    while evaluate_expression(condition, context):
        loop_output = interpret(loop_block, context)
        if loop_output:
            loop_outputs.append(loop_output)
    return "\n".join(loop_outputs)

def interpret_print_statement(statement, context):
    _, expression = statement
    value = evaluate_expression(expression, context)
    return f"print: {value}"

def evaluate_expression(expr, context):
    if isinstance(expr, tuple):
        expr_type = expr[0]
        if expr_type == 'binary_expression':
            return evaluate_binary_expression(expr, context)
        elif expr_type == 'function_call':
            return evaluate_function_call(expr, context)
        else:
            raise ValueError(f"Unrecognized expression type: {expr_type}")
    elif isinstance(expr, str) and expr in context:
        return context[expr]
    elif isinstance(expr, (int, float, str, bool)):
        return expr
    else:
        raise ValueError(f"Unrecognized expression: {expr}")

def evaluate_binary_expression(expr, context):
    _, operator_symbol, left, right = expr
    left_val = evaluate_expression(left, context)
    right_val = evaluate_expression(right, context)
    return ops[operator_symbol](left_val, right_val)

def evaluate_function_call(expr, context):
    _, func_name, args = expr
    func_body = context.get(func_name)
    if func_body is None:
        raise ValueError(f"Function {func_name} not defined")
    func_outputs = []
    for body_statement in func_body[1]:
        func_outputs.append(interpret([body_statement], context))
    return "\n".join(func_outputs)

def is_type_correct(var_type, value):
    type_checks = {
        'int': lambda v: isinstance(v, int),
        'float': lambda v: isinstance(v, float) or isinstance(v, int),
        'string': lambda v: isinstance(v, str),
        'char': lambda v: isinstance(v, str) and len(v) == 1,
        'bool': lambda v: isinstance(v, bool),
    }
    check = type_checks.get(var_type)
    if check is None:
        raise ValueError(f"Unrecognized type: {var_type}")
    return check(value)

def interpret_print(expression, context):
    value = evaluate_expression(expression, context)
    return str(value)