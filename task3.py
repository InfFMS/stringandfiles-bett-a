# Откройте текстовый файл task3.txt для чтения.
# Извлеките все уникальные слова из файла (слова разделяются пробелами и знаками пунктуации).
# Подсчитайте, сколько раз каждое уникальное слово встречается в тексте.
# Запишите результаты в новый файл в формате:
# слово1: количество
# слово2: количество
#
# Убедитесь, что слова записаны в алфавитном порядке.

with open('task3.txt', 'r', encoding='utf-8') as f:
    file = f.read()

file = file.lower()
file = file.replace('.', '')
file = file.replace(',', '')
l = sorted(file.split())
lst = []
for i in l:
    if not i in lst:
        lst.append(i)

with open('result_task3.txt', 'w', encoding='utf-8') as d:
    for j in lst:
        s = '{}: {}\n'.format(j, l.count(j))
        d.write(s)
