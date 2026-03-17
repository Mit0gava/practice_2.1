students = {}

with open("students.txt", "r", encoding="utf-8") as file:
    for line in file:
        name, grades = line.strip().split(":")
        grades = list(map(int, grades.split(",")))
        avg = sum(grades) / len(grades)
        students[name] = avg

# Запись в файл
with open("result.txt", "w", encoding="utf-8") as file:
    for name, avg in students.items():
        if avg > 4.0:
            file.write(f"{name}: {avg}\n")

# лучший студент
best_student = max(students, key=students.get)

print("Лучший студент:", best_student)
print("Средний балл:", students[best_student])