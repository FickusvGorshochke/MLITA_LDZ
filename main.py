def validate_expression(input_string):
    """
    Проверяет корректность строки вида 's(111)=1'.

    Аргументы:
        input_string (str): Строка для проверки.

    Возвращает:
        bool: True, если строка корректна, иначе False.
    """
    # Проверяем наличие необходимых частей строки
    if not input_string.startswith("s(") or "=" not in input_string or not input_string[-1].isdigit():
        return False

    try:
        # Шаг 1: Извлечь число внутри скобок
        start = input_string.index("(") + 1
        end = input_string.index(")")
        unary_input = input_string[start:end]

        # Шаг 2: Проверить, что внутри скобок только символы '1'
        if not unary_input or not all(char == '1' for char in unary_input):
            return False

        # Шаг 3: Извлечь результат после '='
        result_index = input_string.index("=") + 1
        result = input_string[result_index:]

        # Шаг 4: Проверить, что результат состоит только из '1' или "0"
        if not all(char == '1' for char in result) and result != "0":
            return False

        # Шаг 5: Вычислить длину входа и ожидаемый результат
        n = len(unary_input)
        expected_result = '1' * (n // 2)

        # Шаг 6: Сравнить ожидаемый результат с данным
        if result != expected_result:
            print(f"Ошибка: ожидаемый результат '{expected_result}', но получено '{result}'")
            return False

        return True
    except (IndexError, ValueError):
        # Ошибка при разборе строки
        return False





print("Добро пожаловать в анализатор функций в унарной системе.")
print("Введите выражение (пр., s(11)=11) или введите 'exit' для выхода из программы.")
while True:
    user_input = input("Ввод: ")
    if user_input.lower() == "exit":
        print("Выход из программы.")
        break
    message = validate_expression(user_input)
    print(message)
