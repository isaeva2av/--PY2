class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        """
        Создание и подготовка к работе объекта "Книга"
        :param name: Название книги
        :param author: Автор книги
        """
        self._name = name
        self._author = author

    # Защищаем атрибуты от изменений.
    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author

    def __str__(self) -> str:
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook:
    def __init__(self, name: str, author: str, pages: int):
        """
        Создание и подготовка к работе объекта "Бумажная книга"
        :param name: Название книги
        :param author: Автор книги
        :param pages: Количество страниц книги
        """
        super().__init__(name, author)  # Применяем наследование.
        self._pages = pages

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, new_pages: int) -> None:
        if not isinstance(new_pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if not new_pages > 0:
            raise ValueError("Количество страниц не может иметь отрицательное значение")
        self._pages = new_pages

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self._pages})"


class AudioBook:
    def __init__(self, name: str, author: str, duration: float):
        """
        Создание и подготовка к работе объекта "Аудиокнига"
        :param name: Название книги
        :param author: Автор книги
        :param duration: Продолжительность книги
        """
        super().__init__(name, author)  # Применяем наследование.
        self._duration = duration

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, new_duration: float) -> None:
        if not isinstance(new_duration, float):
            raise TypeError("Продолжительность должна быть типа float")
        if not new_duration >= 0:
            raise ValueError("Продолжительность не может иметь отрицательное значение")
        self._duration = new_duration

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self._duration})"
