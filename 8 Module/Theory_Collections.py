#Collections
#У Python є пакет з додатковими колекціями, які можуть дуже знадобитися розробнику-початківцю
# і сильно розширяти його арсенал.

#Використання кортежів у Python для передачі даних між обробниками — це хороша та поширена практика. 
# Але є одна незручність у кортежів, вам необхідно пам'ятати індексацію елементів у кортежі 
# і не плутати їх порядок. Це не завжди зручно і для ситуацій, коли в кортежі є 2 або більше елементів, 
# такий підхід ускладнює читабельність коду:

person = ('Mick', 'Nitch', 35, 'Boston', '01146')


#Після створення person там, де ви його використовуєте, вам потрібно пам'ятати, що ім'я на першому місці,
# а вік — на третьому. Щоб не плутатися, доведеться постійно повертатися до коду, де створюється person. 
# Це незручно і спеціально для таких випадків додали іменовані кортежі:

import collections

Person = collections.namedtuple('Person', ['name', 'last_name', 'age', 'birth_place', 'post_index'])
person = Person('Mick', 'Nitch', 35, 'Boston', '01146')
person.name         # 'Mick'
person.post_index   # '01146'
person.age          # 35
person[3]           # 'Boston'

#Тепер, використовуючи Person, ви можете створювати кортежі,
# які обов'язково повинні містити 5 елементів і у таких кортежів, окрім індексів, є атрибути. 
# Звертатися до елементів такого кортежу можна як за індексом, так і за ім'ям. 
# За такого підходу вам достатньо один раз визначити Person і більше не повертатися до нього, щоб згадати, 
# який елемент за що відповідає.

#Часто вам потрібно підрахувати кількість елементів у певній послідовності. 
# Для цього зручно скористатися словником.
student_marks = [4, 2, 4, 6, 7, 4, 2 , 3, 4, 5, 6, 6, 7, 1, 1, 1, 3, 5]
mark_counts = {}
for mark in student_marks:
    if mark in mark_counts:
        mark_counts[mark] += 1
    else:
        mark_counts[mark] = 1
print(mark_counts)  # {4: 4, 2: 2, 6: 3, 7: 2, 3: 2, 5: 2, 1: 3}


#Таке завдання зустрічається досить часто і, щоб не писати одні й ті самі 6 рядків коду постійно,
# у collections додали спеціальний словник Counter:
import collections

student_marks = [4, 2, 4, 6, 7, 4, 2 , 3, 4, 5, 6, 6, 7 , 1, 1, 1, 3, 5]
mark_counts = collections.Counter(student_marks)
print(mark_counts)  # Counter({4: 4, 6: 3, 1: 3, 2: 2, 7: 2, 3: 2, 5: 2})

#Але на цьому корисні властивості Counter не закінчуються. Він може вивести елементи за частотою появи:
import collections

student_marks = [4, 2, 4, 6, 7, 4, 2 , 3, 4, 5, 6, 6, 7 , 1, 1, 1, 3, 5]
mark_counts = collections.Counter(student_marks)
print(mark_counts.most_common(1))  # [(4, 4)]
print(mark_counts.most_common(2))  # [(4, 4), (6, 3)]


#Ще Counter може відняти кількість елементів одного Counter від другого поелементно:
from collections import Counter

c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(a=1, b=2, c=3, d=4)
c.subtract(d)
print(c)    # Counter({'a': 3, 'b': 0, 'c': -3, 'd': -6})


#Це спеціальний словник, який створює значення для ключів, яких в словнику не було за запитом. 
# Наприклад, у вас є список слів і ви хочете розбити його на декілька списків, залежно від першої літери слова.
words = ['apple', 'zoo', 'lion', 'lama', 'bear', 'bet', 'wolf', 'appendix']
grouped_words = {}

for word in words:
    char = word[0]
    if char not in grouped_words:
        grouped_words[char] = []
    grouped_words[char].append(word)

print(grouped_words)
#У консолі ми побачимо:
{
    'a': ['apple', 'appendix'],
    'z': ['zoo'],
    'l': ['lion', 'lama'],
    'b': ['bear', 'bet'],
    'w': ['wolf']
}

#Таким чином ми можемо отримати всі слова із words, що починаються на якусь літеру.
# Подібні завдання зустрічаються досить часто. Щоб не перевіряти, 
# чи є список на цю літеру в словнику grouped_words, ми можемо скористатися defaultdict із collections 
# та задати значенням за замовчуванням порожній список:
from collections import defaultdict

words = ['apple', 'zoo', 'lion', 'lama', 'bear', 'bet', 'wolf', 'appendix']
grouped_words = defaultdict(list)

for word in words:
    char = word[0]
    grouped_words[char].append(word)

#Результат виконання буде ідентичний. defaultdict приймає у якості аргументу функцію, 
# яка буде використовуватися для створення значення за замовчуванням. В цьому прикладі ми використали list, 
# але ви можете передати будь-яку функцію, яка викликається без аргументів.

#Списки у Python реалізовані таким чином, що вибір елемента за індексом відбувається 
# за константний час (дуже швидко) і додавання/видалення елементу в кінець списку теж відбувається дуже швидко. 
# Але ось додавання елементу в будь-яке інше місце в списку змушує Python перерахувати індекси 
# усіх елементів списку до кінця. Для великих списків це може бути дуже невигідно. 
# Щоб швидко додавати елементи на початок списку, в Python в пакеті collections є така колекція як deque:
from collections import deque

d = deque()
d.append('last')
d.appendleft('first')
d.insert(1, 'middle')
print(d)            # deque(['first', 'middle', 'last'])

print(d.pop())      # 'last'
print(d.popleft())  # 'first'
print(d)            # deque(['middle'])


#Окрім додавання на початок за допомогою appendleft, у deque є і швидке видалення першого елементу popleft.

#Ще однією особливістю deque є можливість обмежити розмір deque:
from collections import deque

d = deque(maxlen=5)
for i in range(10):
    d.append(i)

print(d)            # deque([5, 6, 7, 8, 9], maxlen=5)
# Як видно з прикладу, нові елементи витісняють старіші, але розмір залишається незмінним.
# В іншому deque веде себе точно як список Python.