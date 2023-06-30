# Списки
fruits = ['яблоко','банан','апельсин']
print("Первый фрукт: ", fruits[0])
fruits.append("груша")
print("Все фрукты: ", fruits)

# Кортежи
point = (2, 3)
print("Координаты точки: ", point)

# Множества
numbers = {1, 2, 3, 4, 5}
even_numbers = {2, 4, 6, 8, 10}
odd_numbers = numbers - even_numbers
print('Нечетные числа: ', odd_numbers)

# Словари
person = {'имя': 'Иван', 'возраст': 28, 'город': 'Казань'}
print("Имя:", person['имя'])
person['пол'] = "мужской"
print("Вся информация о персоне: ", person)