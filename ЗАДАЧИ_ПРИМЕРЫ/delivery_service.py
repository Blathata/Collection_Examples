# номер посылки: 114913011
from dataclasses import dataclass


@dataclass
class MovingCargoData:
    """Определяет минимальное количество транспортных платформ,
    необходимое для перевозки всех роботов, описанных в массиве.
    """
    units_weights: list[int]
    max_capacity_platform: int

    def count_platform(self) -> int:
        """Функция подсчета платформ для перевозки всех роботов.

        Returns:
            int: Возвращает количество платформ для транспортировки.
        """
        sorted_units = sorted(self.units_weights)
        lightest_pos, heaviest_pos = 0, len(sorted_units) - 1
        platforms = 0

        while lightest_pos <= heaviest_pos:
            if (sorted_units[lightest_pos] + sorted_units[heaviest_pos]
                    <= self.max_capacity_platform):
                lightest_pos += 1
            heaviest_pos -= 1
            platforms += 1

        return platforms


def main():
    units = [3, 5, 3, 4]
    plat = 4
    shipping = MovingCargoData(units, plat)
    print(shipping.count_platform())


if __name__ == "__main__":
    main()
