def unit_to_int(unit):
    """Преобразует строку единичной системы в целое число."""
    return len(unit)


def int_to_unit(num):
    """Преобразует целое число в строку единичной системы."""
    return "1" * num if num > 0 else "0"


def parse_expression(expr):
    """Парсит выражение вида s(X) и вычисляет результат функции."""
    if not expr.startswith("s(") or not expr.endswith(")"):
        return False, "Неверный формат: Выражение должно быть в форме s(X), где X - число единичной системе счисления."
    try:
        # Извлекаем аргумент из выражения
        arg = expr[2:-1]

        # Проверяем, что аргумент представлен только единицами
        if not all(ch == "1" for ch in arg):
            return False, "Неверный ввод: Аргумент должен содержать только 1"

        # Вычисляем значение функции
        input_value = unit_to_int(arg)
        result = int_to_unit(input_value // 2)

        return True, f"Результат: {expr}={result}"
    except Exception as e:
        return False, str(e)


# Основной цикл ввода
print("Добро пожаловать в анализатор функций для d(x) = [x/2] в унарной системе.")
print("Введите выражение (пр., s(1111)) или введите 'exit' для выхода из программы.")
while True:
    user_input = input("Ввод: ")
    if user_input.lower() == "exit":
        print("Выход из программы.")
        break
    valid, message = parse_expression(user_input)
    print(message)
