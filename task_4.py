# данная программа задает список из N элементов, заполненных числами из промежутка [-N, N],и находит произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
from random import randint
N = 100
lst = [] # список
comp = 1 # переменная для подсчета произведения чисел
for i in range(N):
   lst.append(randint(-N, N)) # заполняем список случайными числами 
print('список: ', lst)

# получаем данные из файла
with open("file.txt") as f:
   index = [] # массив для считывания элементов из файла
   for line in f:
      index.append(int(line)) # заполняем список элементами из файла, предварительно переводим данные в int
print('указанные позиции: ', index)

for i in range(len(index)): # перебираем элементы списка индексов
   j = index[i]    
   comp *= lst[j]  # перемножаем элементы с указанными индексами из файла      
print('произведение элементов на указанных позициях списка равно:', comp)