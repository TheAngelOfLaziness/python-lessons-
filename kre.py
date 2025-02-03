
class MyException(Exception):
    pass


def Rastoynie(Uskoreniy):
    def wrapper(v0,v,t):
        A=Uskoreniy(v0,v,t)
        s=v*t
        print(A)
        print(s)
    return wrapper

@Rastoynie
def Uskoreniy(v0,v,t):

    a=(v-v0)/t
    return a


try:
    v0=int(input('Введите начальную скорость->'))
    v=int(input('Введите конечную скорость->'))
    t=int(input('ввведите время->'))
    if t==0:
        raise MyException('Время не ддолжно = 0')

    print(Uskoreniy(v0,v,t))
except ValueError:
    print("Нельзя вводить строки")

