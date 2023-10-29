name = input('Как вас зовут? ')
print('Здравствуйте', name)
age, mass, height = 0, 0, 0


while age < 11 or type(age) != int:
    try:
        age = int(input('Введите ваш возраст '))
    except ValueError:
        print('Нужно ввести целое число!')
while mass < 9 or type(mass) != int:
    try:
        mass = float(input('Введите число с точкой, например 72.4 '))
        break
    except ValueError:
        print('Нужно ввести число!')
while height < 11 or type(height) != float:
    try:
        height = float(input('Введите ваш рост '))
    except ValueError:
        print('Нужно ввести число!')

bmi = mass / (height / 100) ** 2

print('Ваш индекс массы тела:', round(bmi, 2))
if 17.11 > age < 24.11 and bmi < 19.0:
    print("Внимание - у вас недостаточная масса тела.")
elif 17 > age < 24 and 19.0 > bmi < 25.0:
    print("Отлично, у вас нормальная масса тела.")
elif 17 > age < 24 and bmi > 24.9:
    print("У вас избыточная масса тела!")
elif 24 > age < 35 and bmi < 19.0:
    print("Внимание - у вас недостаточная масса тела.")
elif 24 > age < 35 and 19.0 > bmi < 25.0:
    print("Отлично, у вас нормальная масса тела.")
elif 24 > age < 35 and bmi > 24.9:
    print("У вас избыточная масса тела!")
elif 34 > age < 45 and bmi < 19.0:
    print("Внимание - у вас недостаточная масса тела.")
elif 34 > age < 45 and 19.0 > bmi < 25.0:
    print("Отлично, у вас нормальная масса тела.")
elif 34 > age < 45 and bmi > 24.9:
    print("У вас избыточная масса тела!")
elif 44 > age < 55 and bmi < 19.0:
    print("Внимание - у вас недостаточная масса тела.")
elif 44 > age < 55 and 19.0 > bmi < 25.0:
    print("Отлично, у вас нормальная масса тела.")
elif 44 > age < 55 and bmi > 24.9:
    print("У вас избыточная масса тела!")
elif age > 54 and bmi < 19.0:
    print("Внимание - у вас недостаточная масса тела.")
elif age > 54 and 19.0 > bmi < 25.0:
    print("Отлично, у вас нормальная масса тела.")
elif age > 54 and bmi > 24.9:
    print("У вас избыточная масса тела!")