#Кешко Маргарита
with open('text.txt', 'r',encoding = 'itf-8') as file: # открываем файл
    text = file.read()#читаем весь текст с файла
words = text.split()#разбиваем текст на слова с пробелом как разделителем
print(f"Количество слов в текстовом файле: {len(words)}")#