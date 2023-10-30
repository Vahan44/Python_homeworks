import re

def calculate(expression):
    expression = re.sub(r'\s', '', expression)

    precedence = {'+': 1, '-': 1, '/': 2, '*': 2, '^': 3}

    def apply_operator(operators, values):
        operator = operators.pop()
        right = values.pop()
        left = values.pop()
        if operator == '+':
            values.append(left + right)
        elif operator == '-':
            values.append(left - right)
        elif operator == '*':
            values.append(left * right)
        elif operator == '/':
            if right == 0:
                raise ValueError("Division by zero")
            values.append(left / right)
        elif operator == '^':
            values.append(left ** right)

    operators = []
    values = []
    i = 0
    while i < len(expression):
        if expression[i] in '0123456789':
            j = i
            while j < len(expression) and expression[j] in '0123456789.':
                j += 1
            values.append(float(expression[i:j]))
            i = j
        elif expression[i] in "+-*/^":
            while (
                operators
                and operators[-1] in "+-*/^"
                and precedence[operators[-1]] >= precedence[expression[i]]
            ):
                apply_operator(operators, values)
            operators.append(expression[i])
            i += 1
        elif expression[i] == '(':
            operators.append(expression[i])
            i += 1
        elif expression[i] == ')':
            while operators[-1] != '(':
                apply_operator(operators, values)
            operators.pop()
            i += 1
        else:
            raise ValueError("Invalid character in the expression")

    while operators:
        apply_operator(operators, values)

    return values[0]

expression = "2 + 3 + 8 / 2 * 6"
result = calculate(expression)
print("Result:", result)
