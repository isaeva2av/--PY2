# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
import math


class Building:
    def __init__(self, number_of_floors: int, width: (int, float), length: (int, float), floor_height: (int, float)):
        """
                Создание и подготовка к работе объекта "Здание"
                :param number_of_floors: Количество этажей в доме
                :param width: Ширина дома
                :param length: Длина дома
                :param floor_height: Высота этажа в доме
                Примеры:
                >>> building = Building(3, 25, 10, 3)  # Инициализация экземпляра класса
                """

        if not isinstance(number_of_floors, int):
            raise TypeError('Количество этажей должно быть типа int')
        if number_of_floors <= 0:
            raise ValueError('Количество этажей должно быть положительным числом')
        self.number_of_floors = number_of_floors

        if not isinstance(width, (int, float)):
            raise TypeError('Ширина дома должна быть типа int или типа float')
        if width <= 0:
            raise ValueError('Ширина дома должна быть положительным числом')
        self.width = width

        if not isinstance(length, (int, float)):
            raise TypeError('Длина дома должна быть типа int или типа float')
        if length <= 0:
            raise ValueError('Длина дома должна быть положительным числом')
        self.length = length

        if not isinstance(floor_height, (int, float)):
            raise TypeError('Высота этажа в доме должна быть типа int или типа float')
        if floor_height <= 0:
            raise ValueError('Высота этажа в доме должна быть положительным числом')
        self.floor_height = floor_height

    def building_height(self):
        """
        Функция, которая вычисляет высоту здания
        >>> building = Building(3, 25, 10, 3)
        >>> building.building_height()
        9
        """
        return self.number_of_floors * self.floor_height

    def floor_area(self):
        """
        Функция, которая вычисляет площадь этажа
        >>> building = Building(3, 25, 10, 3)
        >>> building.floor_area()
        250
        """
        return self.width * self.length

    def building_area(self):
        """
        Функция, которая вычисляет суммарную площадь здания
        >>> building = Building(3, 25, 10, 3)
        >>> building.building_area()
        750
        """
        return self.width * self.length * self.number_of_floors


class Parking:
    def __init__(self,  width_: (int, float), length_: (int, float), width_of_parking_space: (int, float),
                 length_of_parking_space: (int, float)):
        """
        Создание и подготовка к работе объекта "Парковка"
        :param width_: Ширина парковки
        :param length_: Длина парковки
        :param width_of_parking_space: Ширина парковочного места
        :param length_of_parking_space: Длина парковочного места
        Примеры:
        >>> parking = Parking(35, 45, 2.5, 5.2)  # Инициализация экземпляра класса
        """
        if not isinstance(width_, (int, float)):
            raise TypeError('Ширина парковки должна быть типа int или типа float')
        if width_ <= 0:
            raise ValueError('Ширина парковки должна быть положительным числом')
        self.width_ = width_

        if not isinstance(length_, (int, float)):
            raise TypeError('Длина парковки должна быть типа int или типа float')
        if length_ <= 0:
            raise ValueError('Длина парковки должна быть положительным числом')
        self.length_ = length_

        if not isinstance(width_of_parking_space, (int, float)):
            raise TypeError('Ширина парковочного места должна быть типа int или типа float')
        if width_of_parking_space <= 0:
            raise ValueError('Ширина парковочного места должна быть положительным числом')
        self.width_of_parking_space = width_of_parking_space

        if not isinstance(length_of_parking_space, (int, float)):
            raise TypeError('Длина парковочного места должна быть типа int или типа float')
        if length_of_parking_space <= 0:
            raise ValueError('Длина парковочного места должна быть положительным числом')
        self.length_of_parking_space = length_of_parking_space

    def number_of_parking_space(self, number: int):
        """
        Функция, которая вычисляет количество машиномест на парковке
        >>> parking = Parking(35, 45, 2.5, 5.2)
        >>> parking.number_of_parking_space(121)
        121
        """

        if not isinstance(number, int):
            raise TypeError('Количество этажей должно быть типа int')
        if number <= 0:
            raise ValueError('Количество этажей должно быть положительным числом')
        self.number = number

        number = math.floor((self.width_ * self.length_) / (self.width_of_parking_space * self.length_of_parking_space))
        return number

    def places_for_the_disabled(self, number_for_the_disabled: int):
        """
        Функция, которая вычисляет количество машиномест на парковке для инвалидов
        >>> parking = Parking(35, 45, 2.5, 5.2)
        >>> parking.places_for_the_disabled(12)
        12
        """

        if not isinstance(number_for_the_disabled, int):
            raise TypeError('Количество этажей должно быть типа int')
        if number_for_the_disabled <= 0:
            raise ValueError('Количество этажей должно быть положительным числом')
        self.number_for_the_disabled = number_for_the_disabled

        number_for_the_disabled = math.floor((self.width_ * self.length_) / (self.width_of_parking_space *
                                                                             self.length_of_parking_space) * 10 / 100)
        return math.floor(number_for_the_disabled)


class Bucket:
    def __init__(self, bucket_height:  (int, float), upper_diameter: (int, float), lower_diameter: (int, float),
                 forming: (int, float)):
        """
        Создание и подготовка к работе объекта "Ведро"
        :param bucket_height: Высота ведра
        :param upper_diameter: Диаемтр нижнего основания ведра
        :param lower_diameter: Диаметр вехней части ведра
        :param forming: Длина образуещей (длина боковой поверхности от основания до верхушки ведра)
        Примеры:
        >>> bucket = Bucket(0.45, 0.20, 0.35, 0.474)  # Инициализация экземпляра класса
        """

        if not isinstance(bucket_height, (int, float)):
            raise TypeError('Высота ведра должна быть типа int или типа float')
        if bucket_height <= 0:
            raise ValueError('Высота ведра должна быть положительным числом')
        self.bucket_height = bucket_height

        if not isinstance(upper_diameter, (int, float)):
            raise TypeError('Диаемтр нижнего основания ведра должна быть типа int или типа float')
        if upper_diameter <= 0:
            raise ValueError('Диаемтр нижнего основания ведра должна быть положительным числом')
        self.upper_diameter = upper_diameter

        if not isinstance(lower_diameter, (int, float)):
            raise TypeError('Диаметр вехней части ведра должна быть типа int или типа float')
        if lower_diameter <= 0:
            raise ValueError('Диаметр вехней части ведра должна быть положительным числом')
        self.lower_diameter = lower_diameter

        if not isinstance(forming, (int, float)):
            raise TypeError('Длина образуещей должна быть типа int или типа float')
        if forming <= 0:
            raise ValueError('Длина образуещей должна быть положительным числом')
        self.forming = forming

    def bucket_volume(self):
        """
        Функция, которая вычисляет объем ведра в кубических метрах
        >>> bucket = Bucket(0.45, 0.20, 0.35, 0.474)
        >>> bucket.bucket_volume()
        0.10956
        """
        return round((1/3) * math.pi * self.bucket_height * (self.upper_diameter ** 2 + self.lower_diameter ** 2 +
                                                             self.upper_diameter * self.lower_diameter), 5)

    def bucket_surface_area(self):
        """
        Функция, которая вычисляет площадь поверхности ведра в  кубических метрах
        Примеры:
        >>> bucket = Bucket(0.45, 0.20, 0.35, 0.474)
        >>> bucket.bucket_surface_area()
        1.32952
        """
        return round(math.pi * self.upper_diameter * (self.upper_diameter + self.forming) + math.pi *
                     self.lower_diameter * (self.lower_diameter + self.forming), 5)


if __name__ == "__main__":
    doctest.testmod()
