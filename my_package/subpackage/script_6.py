# script_5.py

class Geometry:
    """Класс для работы с геометрическими фигурами."""

    @staticmethod
    def triangle_area(base: float, height: float) -> float:
        """Вычисляет площадь треугольника.

        Args:
            base (float): Основание треугольника.
            height (float): Высота треугольника.

        Returns:
            float: Площадь треугольника.
        """
        return 0.5 * base * height

    @classmethod
    def square_area(cls, side: float) -> float:
        """Вычисляет площадь квадрата.

        Args:
            side (float): Длина стороны квадрата.

        Returns:
            float: Площадь квадрата.
        """
        return side ** 2
