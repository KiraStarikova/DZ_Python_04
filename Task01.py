'''1 Вычислить число c заданной точностью d
Пример:
при d = 0.001, π = 3.141 10^(-1) ≤ d ≤10^(-10)'''

from math import pi

d =  int(input("До какого знака округлить число Пи: \n"))
print(f'число Пи с точностью {d} равно {round(pi, d)}')