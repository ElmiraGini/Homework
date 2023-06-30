print('Выберите операцию:')
print('1. Сложение')
print('2. Вычитание')
print('3. Умножение')
print('4. Деление')
while True:
    choice = input('Введите номер операции: ')
    if choice == '1':
        num1 = int(input('Введите первое число: '))
        num2 = int(input('Введите второе число: '))
        result = num1 + num2
        print('Результат сложения: ', result)
    elif choice == '2':
        num1 = int(input('Введите первое число: '))
        num2 = int(input('Введите второе число: '))
        result = num1 - num2
        print('Результат вычитания: ', result)
    elif choice == '3':
        num1 = int(input('Введите первое число: '))
        num2 = int(input('Введите второе число: '))
        result = num1 * num2
        print('Результат умножения: ', result)
    elif choice == '4':
        num1 = int(input('Введите первое число: '))
        num2 = int(input('Введите второе число: '))
        if num2 != 0:
            result = num1 / num2
            print('Результат деления: ', result)
        else:
            print('Ошибка! На ноль делить нельзя!')
    elif choice == '0':
        break
    else: print('Ошибка. Неверный выбор операции')
    print('Если хотите выйти из программы нажмите 0')
