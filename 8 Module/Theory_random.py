#Отримання випадкового цілого числа з рівномірного розподілу в інтервалі між 1 та 1000 включно:
import random

r = random.randint(1, 1000)
print (r)

#Якщо потрібно отримати випадкове число в інтервалі 0, 1 включно:
r = random.random()
print (r)

#Коли у вас є список об'єктів і вам потрібно перемішати порядок елементів в цьому списку на випадковий:
fruits = ['apple', 'banana', 'orange']
random.shuffle(fruits)
print(fruits)   # ['banana', 'orange', 'apple']


#Якщо потрібно вибрати випадковий елемент зі списку:
fruits = ['apple', 'banana', 'orange']
print(random.choice(fruits))   # 'banana'


#Щоб вибрати N випадкових елементів зі списку:
fruits = ['apple', 'banana', 'orange']
print(random.choices(fruits, k=4))   # ['banana', 'orange', 'orange', 'orange']


#Щоб вибрати N елементів, що не повторюються, зі списку:
fruits = ['apple', 'banana', 'orange']
print(random.sample(fruits, k=2))   # ['banana', 'orange']

#Зверніть увагу, що k не може бути більше довжини fruits.

#Якщо вам потрібно скористатися відмінним від рівномірного розподілу,
# можете вибрати один із підтримуваних розподілів (https://docs.python.org/3/library/random.html#real-valued-distributions)