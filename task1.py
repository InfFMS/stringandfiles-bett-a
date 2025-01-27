# Откройте текстовый файл для чтения task1.txt.
# Подсчитайте:
# Общее количество строк в файле. +
# Общее количество слов во всем тексте файла.
# Общее количество символов (включая пробелы).
# Выведите полученную статистику на экран.

lines = 0
words = 0
symbols = 0
l = []
with open('task1.txt', 'r', encoding='utf-8') as f:
    for line in f:
        lines += 1
        l.append(line)

s = l[0] + l[1] + l[2]
symbols = len(s)
new_s = s.replace('.', '').split()
for j in new_s:
    if j.isalpha():
        words += 1

print('Кол-во линий: ', lines)
print('Кол-во слов: ', words)
print('Кол-во символов: ', symbols)



