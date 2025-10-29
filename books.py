import csv

#1
def count_long_titles(books_file):
    books_file.seek(0)  # перемещаем курсор в начало файла
    reader = csv.reader(books_file)  # читаем построчно
    next(reader)  # пропускаем строку заголовков
    count = 0
    for row in reader:
        if len(row[0]) > 30:  # проверяем длину названия (первый столбец)
            count += 1
    return(count)

#2
def find_books_by_author(file_path, author_name):
    results = []
    with open(file_path, encoding='cp1251', newline='') as f:
        for row in csv.DictReader(f, delimiter=';'):
            if author_name.lower() in row['Book-Author'].lower():
                try:
                    price = float(row['Price'])
                    if price <= 150:
                        results.append(f"{row['Book-Author']} — {row['Book-Title']} — {price} руб.")
                except ValueError:
                    continue
    return results

#3
def generate_bibliography(books_file, max_records=20):
    books_file.seek(0)  # перемещаем курсор в начало файла
    reader = csv.reader(books_file, delimiter=';')  # читаем CSV построчно
    next(reader)  # пропускаем заголовки

    bibliography = []
    count = 0
    for row in reader:
        # <Автор>. <Название> - <Год>
        line = row[2].strip() + ". " + row[1].strip() + " - " + row[3].strip()
        bibliography.append(line)
        count += 1
        if count >= max_records:
            break  # только первые 20 записей
    return bibliography

def save_bibliography(bib_list, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        for i, line in enumerate(bib_list, 1):
            f.write(f"{i}. {line}\n")


if __name__ == '__main__': 
    with open("books-en.csv", encoding='cp1251') as books_file:
        print()
        print("Количество записей, у которых в поле Название строка длиннее 30 символов: ",count_long_titles(books_file))
        print()

        author = input("Введите имя автора: ")
        books = find_books_by_author("books-en.csv", author)
        if books:
         for i, book in enumerate(books, 1):
           print(f"{i}. {book}")
        else:
         print("Ничего не найдено.")

        bib_list = generate_bibliography(books_file, max_records=20)
        save_bibliography(bib_list, "bibliography.txt")
        print()
        print("Библиография из 20 записей сохранена в файле 'bibliography.txt'.")
        print()
