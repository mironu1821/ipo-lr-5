#Кешко Маргарита
with open('C:\Users\User\OneDrive\Desktop\іпо\лр5\task_3\text.txt') as file: # открываем файл
    text = file.read()#читаем весь текст с файла
words = text.split()#разбиваем текст на слова с пробелом как разделителем
print(f"Количество слов в текстовом файле: {len(words)}")#
