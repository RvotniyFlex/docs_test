# script_4.py

import math

def hypotenuse(a: float, b: float) -> float:
    """Вычисляет гипотенузу прямоугольного треугольника по теореме Пифагора.

    Args:
        a (float): Длина одного катета.
        b (float): Длина другого катета.

    Returns:
        float: Длина гипотенузы.
    """
    return math.sqrt(a**2 + b**2)

def circle_area(radius: float) -> float:
    """Вычисляет площадь круга.

    Args:
        radius (float): Радиус круга.

    Returns:
        float: Площадь круга.
    """
    return math.pi * radius**2