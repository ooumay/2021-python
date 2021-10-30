# 1. Создать словарь из пар ключ-значение, где ключи - это буквы своей фамилии, а значения - это порядковый номер буквы в алфавите, от которого взят:
# a) факториал (если вы родились весной);
# b) число Фиббоначи (осень);
# c) возведение в третью степень (зима);
# d) основание натурального логарифма e^x (лето).
# 2. Отсортировать его по ключу в алфавитном порядке и сохранить в файл.
# 3. Отсортировать по значениям от меньшего к большему и сохранить в файл.
# 4. Для задания 1(а-г) написать функцию-генератор.
# 5. Создать список из значений словаря и разделить его на два: один из значений меньше среднего по списку, второй - среднее и выше.

dict = {'P': 16,'L': 12,'E': 5,'N': 14,'K': 11,'I': 9,'N': 14}
dict_spring = {'P': 3,'L': 2,'E': 5,'N': 1,'K': 4,'I': 7,'N': 1}

# Выводим факториалы значений библиотеки
def fact(a):
    if a == 0:
        return 1 
    return fact(a-1) * a

for i in dict_spring:
    dict_spring[i] = fact(dict_spring[i])

# Сортируем значения по алфовитному порядку ключей
sort1 = sorted(dict.values())
sorted_dict_1 = {}
for i in sort1:
    for k in dict.keys():
        if dict[k]==i:
            sorted_dict_1[k]= dict_spring[k]
            break

with open('sorted_1.txt','w') as out:   # Записываем отсортированный словарь в файл
    for key,val in sorted_dict_1.items():
        out.write('{}:{}\n'.format(key,val))

# Сортируем значения от меньшего к большему
sort2 = sorted(dict_spring.values())
sorted_dict_2 = {}
for i in sort2:
    for k in dict_spring.keys():
        if dict_spring[k]==i:
            sorted_dict_2[k]= dict_spring[k]
            break

with open('sorted_2.txt','w') as out:   # Записываем отсортированный словарь в файл
    for key,val in sorted_dict_2.items():
        out.write('{}:{}\n'.format(key,val))




