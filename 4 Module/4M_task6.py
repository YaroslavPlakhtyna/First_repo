"""
У нас є список показників студентів групи – це список з отриманими балами з тестування.
Необхідно поділити список на дві частини. Напишіть функцію split_list, яка приймає список (цілі числа),
знаходить середнє значення бала у списку та ділить його на два списки.
У перший потрапляють значення менше середнього, включаючи середнє значення,
тоді як у другий — строго більше від середнього. Функція повертає кортеж цих двох списків.
Для порожнього списку повертаємо два порожні списки.

list1 = >=50 
list2 = 51 >
"""
def split_list(grade):
    if not grade:
        return [], []
    middle_grade = sum(grade) / len(grade)
    below_middle = [grade for grade in grade if grade <= middle_grade]
    above_middle = [grade for grade in grade if grade > middle_grade]
    return below_middle, above_middle

