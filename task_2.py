# данная программа принимает на вход число N и выдает набор произведений чисел от 1 до N.
N = int(input('Введите натуральное число N: '))
result = 1 # результат произведений чисел, задаем первичное значение = 1
for i in range(1,N+1):
   result *= i 
   print(result)