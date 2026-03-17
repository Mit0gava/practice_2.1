from datetime import datetime

log_file = "calculator.log"


def show_last():
    try:
        with open(log_file, "r") as file:
            lines = file.readlines()
            print("Последние операции:")
            for line in lines[-5:]:
                print(line.strip())
    except FileNotFoundError:
        print("Лог пуст")


def clear_log():
    open(log_file, "w").close()
    print("Лог очищен")


show_last()



try:
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
except ValueError:
    print("Ошибка операции")
    exit()



op = input("Операция (+ - * /): ")
if op == "+":
    result = a + b
elif op == "-":
    result = a - b
elif op == "*":
    result = a * b
elif op == "/":
    result = a / b
else:
    print("Ошибка операции")
    exit()

print("Результат:", result)

log = f"[{datetime.now()}] {a} {op} {b} = {result}\n"

with open(log_file, "a") as file:
    file.write(log)

choice = input("Очистить лог? (y/n): ")

if choice.lower() == "y":
    clear_log()