file = open('text.txt', 'r')
read = file.read()
# – прочитать входной файл, считать все символы;
print('все символы: ' + read)

list1 = list()
for i in read:
    if i.isdigit():
        list1 += i
print('цифры в файле, с сохранением порядка: ' + str(list1))  # – вывести те символы из файла, которые обозначают цифры от 0 до 9, в том порядке, как они встречаются в файле;
print('цифры по убыванию: ' + str(sorted(list1, reverse=True)))  # – вывести эти символы, упорядочив их по убыванию кода символа;


list2 = list()
for i in read:
    if i.isdigit():
        if i not in list2 and i !=' ':
            list2 += i
print(list2)  # – вывести каждый символ не более одного раза;
