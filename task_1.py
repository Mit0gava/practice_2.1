# Создание файла и запись текста
lines = [
    "Hii!!!",
    "Hello!",
    "Helo....",
    ":(",
    "Это демка."
]

with open("text.txt", "w", encoding="utf-8") as file:
    for line in lines:
        file.write(line + "\n")


with open("text.txt", "r", encoding="utf-8") as file:
    data = file.readlines()


line_count = len(data)

word_count = sum(len(line.split()) for line in data)

longest_line = max(data, key=len)

print("Количество строк:", line_count)
print("Количество слов:", word_count)
print("Самая длинная строка:", longest_line.strip())