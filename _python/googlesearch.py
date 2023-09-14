from webbrowser import open as wopen


def search(typesearch: str, textsearch: str) -> None:
    if typesearch == "П" or typesearch == "п":
        wopen("https://www.google.com/search?q=" + textsearch)
    elif typesearch == "К" or typesearch == "к":
        wopen("https://www.google.com/search?tbm=isch&q=" + textsearch)


def main() -> None:
    while 1:
        textsearch = input(
            'Введите запрос в формате: "Ид: Запрос"\nИдентификаторы: П - Стандартный поиск, К - Поиск картинок\n> '
        )
        if textsearch == "":
            break

        identifier, request = [t.strip() for t in textsearch.split(":", 1)]

        if identifier.strip() in "ПпКк" and request:
            search(identifier, request)
        else:
            print("~ Технические шоколадки! Неверно введены данные")


if __name__ == "__main__":
    main()
