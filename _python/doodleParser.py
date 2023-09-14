import requests
import lxml.html
import os


def cleaner(
    inText,
):  # Чистит переданный текст от пробелов и переносов строки в начале и конце строки
    begPnt = 0
    extPnt = 0
    while inText[begPnt] == " " or inText[begPnt] == "\n":
        begPnt += 1
    while inText[extPnt] == " " or inText[extPnt] == "\n":
        extPnt -= 1

    return inText[begPnt: extPnt + 1]


def writer(
    wrText,
):  # Создает файл doodle.txt на рабочем столе и записывает туда переданные значение
    try:
        file = open(
            "C:/users/" + os.environ.get("USERNAME") +
            "/Desktop/doodle.txt", "a"
        )
        file.write(wrText + "\n")
        file.close
    except:
        return


def parse(
    url,
):  # Запрашивает данные последней даты и обрабатываает их [ связано с writer() и cleaner() ]
    try:
        api = requests.get(url)
    except:
        return
    tagText = lxml.html.document_fromstring(api.text).xpath(
        '//*[@id="latest-tag"]/text()'
    )
    titleText = lxml.html.document_fromstring(api.text).xpath(
        '//*[@id="latest-title"]/text()'
    )
    writer(cleaner(tagText[0]))
    writer("- " + cleaner(titleText[0]) + "\n")


def main():
    parse("https://google.com/doodles/")


if __name__ == "__main__":
    main()
