# Функция без аргументов
def function_name_1(): # ОПРЕДЕЛЕНИЕ ФУНКЦИИ
    print(a)

# Функция с одним аргументом
def function_name_2(num): 
    print(num)

# Функция с несколькими аргументами
def function_name_3(num, res = 10): 
    res += num
    print(res)

# Функция с несколькими аргументами когда не знаешь количество
def function_name_4(*args):  # любое количество неименованных аргументов принимается как список
    for i in args:
        print(i)

# Функция с несколькими аргументами когда не знаешь количество
def function_name_5(**kwargs):  # любое количество именованных аргументов принимается как словарь
    for key, value in kwargs.items():
        print(key, ':', value)

def add(a, b):
    a += b
    return a 

print("Глобальная область")

# function_name_3(b, c)                                     # вызов функциии. num = b
# function_name_2([1,2,3,4])      
# function_name_4(1,2,3,4,5)                                # вызов функциии c неизвестным числом аргументов (в список)
# function_name_5(first='Geeks', mid='for', last='Geeks')   # вызов функциии c неизвестным числом именованных аргументов (в словарь)

num1 = 10
num2 = 20
a = add(num1, num2)  # после return внутри функции a = return [значение / выражение]
print(a)