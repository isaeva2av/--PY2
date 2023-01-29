BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    def __init__(self, id_: int, name: str, pages: int):
        if not isinstance(id_, int):
            raise TypeError('Идентификатор книги должен быть типа int')
        if id_ <= 0:
            raise ValueError('Идентификатор книги должен быть положительным числом')
        self.id_ = id_

        if not isinstance(name, str):
            raise TypeError('Название книги должно быть типа str')
        self.name = name

        if not isinstance(pages, int):
            raise TypeError('Количество страниц в книге должно быть типа int')
        if pages <= 0:
            raise ValueError('Количество страниц в книге должно быть положительным числом')
        self.pages = pages
        
    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self):
        return f'{self.__class__.__name__}(id_={self.id_}, name={self.name!r}, pages={self.pages})'


class Library:
    def __init__(self, books=[]):
        """
        Создание и подготовка к работе объекта "Library"
        :param books: Список книг
        """
        if books is None:  # Если аргумент отсутствует, то библиотека инициализируется с пустым списком книг.
            self.books = []
        else:
            self.books = books
            
        if not isinstance(books, list):
            raise TypeError('Список книг должен быть типа list')

    def get_next_book_id(self):
        if len(self.books) == 0:  # Если книг в библеотеке нет, то возвращаем 1.
            return 1
        # Если книга есть, то возвращаем идентификатор последней книги увеличенный на 1.
        return self.books[-1].id_ + 1

    def get_index_by_book_id(self, id_: int) -> int:
        for index, book in enumerate(self.books):  # Если книга существует, то возвращаем индекс списка.
            if book.id_ == id_:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
