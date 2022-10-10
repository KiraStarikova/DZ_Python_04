'''4 Задана натуральная степень k. 
Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
 и записать в файл многочлен степени k.
Пример:
k=2 => 2*x^2 + 4*x + 5 = 0 или x^2 + 5 = 0 или 10*x^2 = 0'''


import random


def file(file_name): 
    make_file(file_name)  
    f = open(file_name, 'a')
    f.write(solution())  
    f.close()


def make_file(file_name):       
    f = open(file_name, 'w')
    f.close()


def solution():   
    n = int(input("вводим степень многочлена "))
    equa = ''
    for i in range(n, -1, -1):
        k = kf(i)  
        if k != 0:
            if i > 1:
                el = str(k)+'*x^'+str(i)
            elif i == 1:
                el = str(k)+'*x'
            else:
                el = str(k)
        
        equa = equa + "+" + el
    equa = equa[1:]  
    print(equa)
    return equa


def kf(n): 
    k = random.randint(0, 101)
    return k


if __name__ == '__main__':
    file_name = 'text.txt' 
    file(file_name)
    file_name = 'text1.txt' 
    file(file_name)
