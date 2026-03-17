import csv

filename = "resource/products.csv"

products = []

# Чтение
try:
    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            products.append(row)
except FileNotFoundError:
    pass


def add_product():
    name = input("Название: ")
    price = int(input("Цена: "))
    qty = int(input("Количество: "))
    products.append([name, price, qty])


def search_product():
    name = input("Введите название товара: ")
    for product in products:
        if product[0].lower() == name.lower():
            print("Найден:", product)


def total_cost():
    total = 0
    for product in products[1:]:  # пропускаем первую строку
        total += int(product[1]) * int(product[2])
    print("Общая стоимость:", total)


def save():
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(products)


while True:
    print("\n1 Добавить товар")
    print("2 Поиск товара")
    print("3 Общая стоимость")
    print("4 Сохранить и выйти")

    choice = input("Выбор: ")

    if choice == "1":
        add_product()
    elif choice == "2":
        search_product()
    elif choice == "3":
        total_cost()
    elif choice == "4":
        save()
        break