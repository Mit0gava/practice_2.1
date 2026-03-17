import json

file = "resource/library.json"


def load():
    try:
        with open(file, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []


def save(data):
    with open(file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


library = load()


def show_books():
    for book in library:
        print(book)


def add_book():
    id = input("ID: ")
    title = input("Название: ")
    author = input("Автор: ")

    library.append({
        "id": id,
        "title": title,
        "author": author,
        "available": True
    })

    save(library)


def search():
    text = input("Поиск: ").lower()

    for book in library:
        if text in book["title"].lower() or text in book["author"].lower():
            print(book)


def change_status():
    id = input("ID книги: ")

    for book in library:
        if book["id"] == id:
            book["available"] = not book["available"]
            print("Статус изменен")

    save(library)


def delete():
    id = input("ID книги: ")

    global library
    library = [b for b in library if b["id"] != id]

    save(library)


def export_available():
    with open("available_books.txt", "w", encoding="utf-8") as f:
        for book in library:
            if book["available"]:
                f.write(book["title"] + "\n")


while True:
    print("\n1 Показать книги")
    print("2 Добавить книгу")
    print("3 Поиск")
    print("4 Изменить статус")
    print("5 Удалить")
    print("6 Экспорт доступных")
    print("7 Выход")

    c = input("Выбор: ")

    if c == "1":
        show_books()
    elif c == "2":
        add_book()
    elif c == "3":
        search()
    elif c == "4":
        change_status()
    elif c == "5":
        delete()
    elif c == "6":
        export_available()
    elif c == "7":
        break