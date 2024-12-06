def calculate(expression):  # Принимает строку с выражением, пытается вычислить его.
    try:
        return str(evaluate_expression(expression))  # Пытается вычислить выражение и возвращает результат в виде строки.
    except Exception as e:
        return f"Error: {e}"  # Возвращает любые ошибки, возникшие во время вычисления.


def evaluate_expression(expression):  # Организует процесс вычисления.
    tokens = tokenize(expression)  # Разбивает входную строку на токены
    postfix = infix_to_postfix(tokens)  # Преобразует выражение из инфиксной нотации в постфиксную.
    return evaluate_postfix(postfix)  # Вычисляет постфиксное выражение и возвращает результат.

def tokenize(expression):  # Разделяет строку выражения на отдельные токены
    tokens = []
    current_token = ""
    for char in expression: # Цикл перебирает каждый символ в входной строке.
        if char.isdigit() or char == ".": # Проверяет, является ли символ цифрой или точкой.
            current_token += char # Если да, то добавляет символ к текущему токену.
        else: # Если не пустой, то добавляет его в список токенов.
            if current_token:  # Если не пробел, то добавляет символ как отдельный токен.
                tokens.append(current_token)
                current_token = ""
            if char != " ": # Проверяет, не пустой ли текущий токен после цикла
                tokens.append(char)
    if current_token:
        tokens.append(current_token)
    return tokens


def infix_to_postfix(tokens):  # Преобразует выражение из инфиксной нотации в постфиксную (обратную польскую нотацию).
    output = []
    stack = []
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2}  # Словарь приоритетов операторов.

    for token in tokens:
        if token.replace(".", "", 1).isdigit():
            output.append(token)
        elif token == "(":
            stack.append(token)
        elif token == ")":
            while (stack and stack[-1] != "("):  # Извлекаем операторы из стека, пока не найдём открывающую скобку.
                output.append(stack.pop())
            stack.pop()  # Извлекаем открывающую скобку.
        else:
            while (
                stack
                and stack[-1] != "("
                and precedence[token] <= precedence[stack[-1]]):  # Извлекаем операторы с более высоким или равным приоритетом из стека.
                output.append(stack.pop())
            stack.append(token)  # Помещаем текущий оператор в стек.

    while stack:
        output.append(stack.pop())  # Добавляем оставшиеся операторы из стека в выходные данные.

    return output


def evaluate_postfix(tokens):  # Вычисляет постфиксное выражение.
    stack = []
    for token in tokens:
        if token.replace(".", "", 1).isdigit():
            stack.append(float(token))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if token == "+":
                stack.append(operand1 + operand2)  # Выполняем операцию и помещаем результат.
            elif token == "-":
                stack.append(operand1 - operand2)
            elif token == "*":
                stack.append(operand1 * operand2)
            elif token == "/":
                stack.append(operand1 / operand2)
    return stack.pop()  # Возвращаем окончательный результат.


expression = input("Введите выражение: ")
result = calculate(expression)
if result[-4:] == "zero":
    print("Результат равен нулю")
elif result[:5] == "Error":  # Проверяет, была ли ошибка
    print("Некорректное выражение")
else:
    print(f"Результат: {result}")
