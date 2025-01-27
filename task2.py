# Откройте текстовый файл task2.txt для чтения.
# Считайте его содержимое в строку.
# Найдите и замените все вхождения слова "Python" на слово "Питон" (регистр учитывать).
# Запишите обновленный текст в новый файл с другим именем.
# Выведите на экран сообщение о количестве произведённых замен.

with open('task2.txt', 'r', encoding='utf-8') as f:
    file = f.read()

changes = file.count('Python')
file = file.replace('Python', 'Питон')
with open('edited_task2.txt', 'w', encoding='utf-8') as d:
    d.write(file)

print('Замен произведено: ', changes)
#print(file)