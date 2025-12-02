#Кешко Маргарита
with open(r"C:\Users\User\OneDrive\Desktop\іпо\лр5\task_6\text.txt", 'r', encoding='utf-8') as file1: #открываем файл text.txt в режиме чтения ('r') и сохраняем в переменную file1
    with open(r"C:\Users\User\OneDrive\Desktop\іпо\лр5\task_6\output.txt", 'w', encoding='utf-8') as file2: #открываем файл output.txt в режиме записи ('w') и сохраняем его в переменную file2
        for line in file1:#создаем цикл с перебором
            file2.write(line.replace('о',"а"))#записываем во второй файл текст с измененными буквами