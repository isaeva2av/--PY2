import datetime


class PublicTransport:
    """Базовый класс "Общественный транспорт"."""
    def __init__(self, manufacturer: str, model: str, year_: int, max_speed: int, number_of_passengers: int,
                 route_distance: int):
        """
        :param manufacturer: Изготовитель
        :param model: Модель транспорта
        :param year_: Год изготовления
        :param max_speed: Максимальная скорость
        :param number_of_passengers: Количество пассажиров
        :param route_distance: Дальность маршрута в км
        """
        self._manufacturer = manufacturer
        self._model = model
        if not isinstance(year_, int):
            raise TypeError('Год изготовления должен быть типа int')
        if year_ <= 0:
            raise ValueError('Год изготовления должен быть положительным числом')
        self.year_ = year_
        if not isinstance(max_speed, int):
            raise TypeError('Максимальная скорость должна быть типа int')
        if max_speed <= 0:
            raise ValueError('Максимальная скорость должна быть положительным числом')
        self.max_speed = max_speed
        if not isinstance(number_of_passengers, int):
            raise TypeError('Количество пассажиров должно быть типа int')
        if number_of_passengers <= 0:
            raise ValueError('Количество пассажиров должно быть положительным числом')
        self.number_of_passengers = number_of_passengers
        if not isinstance(route_distance, int):
            raise TypeError('Дальность маршрута должна быть типа float')
        if route_distance <= 0:
            raise ValueError('Дальность маршрута должна быть положительным числом')
        self.route_distance = route_distance

    # Защищаем атрибуты от изменений, так как информация о моделях и изготовителях транспорта определена единственна.
    @property
    def manufacturer(self) -> str:
        return self._manufacturer

    @property
    def model(self) -> str:
        return self._model

    def __str__(self) -> str:  # Определяет поведение функции str(), вызванной для экземпляра класса.
        return f"Изготовитель {self.manufacturer}. Модель {self.model}  {self.year_} года изготовления. " \
               f"Максимальная скорость - {self.max_speed} км/ч, вместимость - {self.number_of_passengers}, " \
               f"расход - {self.route_distance} л."

    def __repr__(self) -> str:  # Определяет поведение функции repr(), предназначен для машинно-ориентированного вывода.
        return f"{self.__class__.__name__}(manufacturer={self.manufacturer!r}, model={self.model!r}, " \
               f"route_distance = {self.route_distance}" \


    def term_of_use(self) -> int:
        """Метод определяет возраст использования транспорта."""
        return datetime.date.today().year - self.year_

    def passenger_traffic_per_shift(self) -> float:
        """Метод позволяет определить пассажиропоток за смену."""
        return 8 * self.number_of_passengers/(self.route_distance/self.max_speed)


class Bus(PublicTransport):
    """Дочерний класс "Автобус"."""

    def __init__(self, manufacturer: str, model: str, year_: int, max_speed: int, number_of_passengers: int,
                 route_distance: int, average_fuel_consumption: int):
        """
        :param manufacturer: Изготовитель
        :param model: Модель транспорта
        :param year_: Год изготовления
        :param max_speed: Максимальная скорость
        :param number_of_passengers: Количество пассажиров
        :param route_distance: Дальность маршрута в км
        :param average_fuel_consumption: Расход топлива на 100 км в л
        """
        super().__init__(manufacturer, model, year_, max_speed, number_of_passengers, route_distance)
        if not isinstance(average_fuel_consumption, int):
            raise TypeError('Расход топлива на 100 км должен быть типа int')
        if average_fuel_consumption <= 0:
            raise ValueError('Расход топлива на 100 км должен быть положительным числом')
        self.average_fuel_consumption = average_fuel_consumption

    def __str__(self) -> str:  # Определяет поведение функции str(), вызванной для экземпляра класса.
        return f"Изготовитель {self.manufacturer}. Модель {self.model}  {self.year_} года изготовления. " \
               f"Максимальная скорость - {self.max_speed} км/ч, вместимость - {self.number_of_passengers}. " \
               f"Cредний расход = {self.average_fuel_consumption} л."

    def __repr__(self) -> str:  # Определяет поведение функции repr(), предназначен для машинно-ориентированного вывода.
        return f"{self.__class__.__name__}(manufacturer={self.manufacturer!r}, model={self.model!r}, " \
               f"year={self.year_}, max_speed={self.max_speed}, number_of_passengers={self.number_of_passengers}," \
               f"average_fuel_consumption={self.average_fuel_consumption})"

    def fuel_consumption(self) -> float:
        """Метод определяет расход топлива за рейс."""
        return self.average_fuel_consumption * self.route_distance / 100


class Trolleybus(PublicTransport):
    """Дочерний класс "Троллейбус"."""
    def __init__(self, manufacturer: str, model: str, year_: int, max_speed: int, number_of_passengers: int,
                 route_distance: int, power_consumption: int):
        """
        :param manufacturer: Изготовитель
        :param model: Модель транспорта
        :param year_: Год изготовления
        :param max_speed: Максимальная скорость
        :param number_of_passengers: Количество пассажиров
        :param route_distance: Дальность маршрута в км
        :param power_consumption: Расход электроэнергии на 100 км в кВ*ч/км
        """
        super().__init__(manufacturer, model, year_, max_speed, number_of_passengers, route_distance)
        if not isinstance(power_consumption, int):
            raise TypeError('Расход электроэнергии на 100 км должен быть типа int')
        if power_consumption <= 0:
            raise ValueError('Расход электроэнергии на 100 км должен быть положительным числом')
        self.power_consumption = power_consumption

    def __str__(self) -> str:  # Определяет поведение функции str(), вызванной для экземпляра класса.
        return f"Изготовитель {self.manufacturer}. Модель {self.model}  {self.year_} года изготовления. " \
               f"Максимальная скорость - {self.max_speed} км/ч, вместимость - {self.number_of_passengers}. " \
               f"Cредний расход = {self.power_consumption} л."

    def __repr__(self) -> str:  # Определяет поведение функции repr(), предназначен для машинно-ориентированного вывода.
        return f"{self.__class__.__name__}(manufacturer={self.manufacturer!r}, model={self.model!r}, " \
               f"year={self.year_}, max_speed={self.max_speed}, number_of_passengers={self.number_of_passengers}, " \
               f"power_consumption={self.power_consumption})"

    def fuel_consumption(self) -> float:
        """Метод определяет расход электроэнергии за рейс."""
        return self.power_consumption * self.route_distance / 100

    def passenger_traffic_per_shift(self) -> float:
        """Метод позволяет определить пассажиропоток за смену. Перегружаем метод, так как в автобусе присутствует
        контроллер, который ранее не учитывался"""
        return 8 * self.number_of_passengers/(self.route_distance/self.max_speed) - 1


if __name__ == "__main__":
    public_transport = PublicTransport('ПАЗ', 'ПАЗ-4230 «Аврора»', 2001, 90, 54, 45)
    print(public_transport)
    public_transport.term_of_use()
    public_transport.passenger_traffic_per_shift()
    bus = Bus('ЛиАЗ', 'ЛиАЗ-5256', 2018, 90, 117, 75, 50)
    print(bus)
    bus.fuel_consumption()
    trolleybus = Trolleybus('ООО «ПК Транспортные системы»', 'ПКТС-6281', 2020, 80, 125, 65, 220)
    print(trolleybus)
    trolleybus.fuel_consumption()
    trolleybus.passenger_traffic_per_shift()

    pass
