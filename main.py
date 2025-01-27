def read_char():
    """Читает следующий символ"""
    global ind, ch, sequence
    ind += 1
    if ind < len(sequence):
        ch = sequence[ind]
    else:
        ch = None  

def CorrectSequence():

    global ch
    if ch == 'S':
        read_char()
        if ch == '(':
            read_char()
            Z()
        else:
            raise SyntaxError(f"Ошибка на позиции {ind + 1}: ожидалась '(' после 'S'")
    else:
        raise SyntaxError(f"Ошибка на позиции {ind + 1}: ожидался 'S'")

def Z():

    global ch
    if ch == '1':
        read_char()
        B()
    elif ch == ')':
        read_char()
        if ch == '=':
            read_char()
        else:
            raise SyntaxError(f"Ошибка на позиции {ind + 1}: ожидался '='")
    else:
        raise SyntaxError(f"Ошибка на позиции {ind + 1}: ожидался '1' или ')='")

def B():

    global ch
    if ch == '1':
        read_char()
        Z()
        if ch == '1':
            read_char()
        else:
            raise SyntaxError(f"Ошибка на позиции {ind + 1}: ожидалась '1'")
    elif ch == ')':
        read_char()
        if ch == '=':
            read_char()
        else:
            raise SyntaxError(f"Ошибка на позиции {ind + 1}: ожидался '='")
    else:
        raise SyntaxError(f"Ошибка на позиции {ind + 1}: ожидался '1' или ')='")

def parse(input_string):

    global ind, ch, sequence
    sequence = input_string.strip()
    ind = 0
    ch = sequence[ind] if sequence else None

    try:
        CorrectSequence()
        if ch is None:
            print("Выражение корректно!")
        else:
            raise SyntaxError(f"Ошибка на позиции {ind + 1}: лишние символы в конце")
    except SyntaxError as e:
        print(e)

sentence = input()
parse(sentence)
