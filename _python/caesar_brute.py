from string import ascii_lowercase as lower_chars, ascii_uppercase as upper_chars

inp = input("~ Input your text: ")

for shift in range(26):  # Пробежка по английскому алфавиту (26 букв)
    output = ""  # Выходная строка

    for c in inp:  # Пробежка по каждой букве
        if (
            c in lower_chars
        ):  # Запись в выходную строку буквы малого регистра со сдвигом (по модулю 26)
            output = f"{output}{lower_chars[ (lower_chars.index(c)+shift)%26 ]}"
        elif (
            c in upper_chars
        ):  # Запись в выходную строку буквы большого регистра со сдвигом (по модулю 26)
            output = f"{output}{upper_chars[ (upper_chars.index(c)+shift)%26 ]}"
        else:  # Запись символа без сдвига, если буква не английская
            output = f"{output}{c}"

    print(f"#{shift}:  {output}")  # Вывод результата на каждой итерации
