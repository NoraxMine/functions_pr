"""""a = int(input())
b = int(input())

def calculations(v, m):
    n = a + b
    return a + b

pl = calculations(a, b)
print(str(pl))"""""






"""""def adder(*args):
    sum = 0
    
    for n in args:
        sum += n

    print("Sum: ", sum)

adder(3, 5)
adder(4, 5, 6, 7)
adder(1, 2, 3, 5, 6)
"""""





"""def function(*args):
    for i in args:
        print(i)
 
function(1, 2, 3, 4)"""






"""b = input()

def search(b):
    vow = set('aeiyou')
    found = vow.intersection(set(b))
    for vow in found:
        print(vow)


a = search(b)
print(a)"""




b = input()

def search(b):
    vow = set('aeiyou')
    found = vow.intersection(set(b))
    for vow in found:
        print(vow)


a = search(b)
print(a)



num1 = int(input())
num2 = int(input())



def calculationsm(c , d):
    mi = int(c) - int(d)
    return mi

mi = calculationsm(num1, num2)
print('Результат min: ' + str(mi))





def calculationsumn(c , d):
    umn = int(c) * int(d)
    return umn

umn = calculationsumn(num1, num2)
print('Результат umn: ' + str(umn))