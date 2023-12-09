"""У минулому модулі ми працювали із системою оцінок ECTS. Напишіть функцію formatted_grades,
яка приймає на вхід словник оцінювання студентів за предмет наступного вигляду:

students = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}
І повертає список відформатованих рядків, щоб під час виведення наступного коду:

for el in formatted_grades(students):
    print(el)
Виходила наступна таблиця:

   1|Nick      |  A  |  5
   2|Olga      |  B  |  5
   3|Mike      | FX  |  2
   4|Anna      |  C  |  4
перший стовпець — ширина 4 символи, вирівнювання по правому краю
другий стовпець — ширина 10 символів, вирівнювання по лівому краю
третій та четвертий стовпець — ширина 5 символів, вирівнювання по центру
вертикальний символ | не входить у ширину стовпця"""

grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}

def get_grade(grade):
    grade_map = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}
    return grade_map.get(grade, 0)

def formatted_grades(students):
    formatted = []
    for i, (name, grade) in enumerate(students.items(), start=1):
         formatted.append(f"{i:>4}|{name:<10}|{grade:^5}|{get_grade(grade):^5}")
    return formatted


students = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}

for el in formatted_grades(students):
    print(el)