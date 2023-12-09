"""Нагадаємо, що у 4 модулі ми для кулінарного блогу писали функцію format_ingredients,
яка приймала на вхід список з інгредієнтами рецепта.

Ми продовжимо працювати в цьому напрямку та створимо функцію, яка шукатиме рецепт
у файлі та повертатиме знайдений рецепт у вигляді словника певної форми.

У вас є файл, який містить рецепти у вигляді:

60b90c1c13067a15887e1ae1,Herbed Baked Salmon,4 lemons,1 large red onion,2 tablespoons chopped fresh basil
60b90c2413067a15887e1ae2,Lemon Pancakes,2 tablespoons baking powder,1 cup vanilla-flavored almond milk,1 lemon
60b90c2e13067a15887e1ae3,Chicken and Cold Noodles,6 ounces dry Chinese noodles,1 tablespoon sesame oil,3 tablespoons soy sauce
60b90c3b13067a15887e1ae4,Watermelon Cucumber Salad,1 large seedless watermelon,12 leaves fresh mint,1 cup crumbled feta cheese
60b90c4613067a15887e1ae5,State Fair Lemonade,6 lemons,1 cups white sugar,5 cups cold water
Кожен рецепт записаний з нового рядка (не забуваємо під час вирішення завдання про кінець рядка). Кожен запис починається з первинного ключа бази даних MongoDB. Далі через кому, йде назва рецепта, а потім через кому, йде перелік інгредієнтів рецепта.

Вам необхідно реалізувати функцію, котра буде отримувати інформацію про рецепт
у вигляді словника для кожної страви що шукається. Створіть функцію get_recipe(path, search_id),
яка повертатиме словник для рецепта із зазначеним ідентифікатором MongoDB.

Де параметри функції:

path — шлях до файлу.
search_id — первинний ключ MongoDB для пошуку рецепта
Вимоги:

Використовуйте менеджер контексту with для читання з файлу
Якщо рецепта із зазначеним search_id у файлі немає, функція повинна повернути None
Приклад: для файлу, вказаного вище, виклик функції у вигляді

get_recipe("./data/ingredients.csv", "60b90c3b13067a15887e1ae4")
Повинен знайти у файлі рядок 60b90c3b13067a15887e1ae4,Watermelon Cucumber Salad,1 large seedless watermelon,12 leaves fresh mint,1 cup crumbled feta cheese і повернути результат у вигляді словника такої структури:

{
    "id": "60b90c3b13067a15887e1ae4",
    "name": "Watermelon Cucumber Salad",
    "ingredients": [
        "1 large seedless watermelon",
        "12 leaves fresh mint",
        "1 cup crumbled feta cheese",
    ],
}
"""
def get_recipe(path, search_id):
    with open(path, 'r') as fh:
        for line in fh:
            parts = line.strip().split(',')
            if len(parts) >= 4 and parts[0] == search_id:
                recipe_dict = {
                    "id": parts[0],
                    "name": parts[1],
                    "ingredients": parts[2:]
                }
                return recipe_dict
    return None

print(get_recipe("C:\\Users\\plakh\\OneDrive\\Documentos\\GitHub\\First_repo\\6 Module\\ingredients_for_6task.txt", "60b90c4613067a15887e1ae5"))