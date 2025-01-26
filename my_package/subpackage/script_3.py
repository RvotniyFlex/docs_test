# script_3.py

def power(base: float, exponent: float) -> float:
    """Вычисляет степень числа.

    Args:
        base (float): Основание степени.
        exponent (float): Показатель степени.

    Returns:
        float: Результат возведения в степень.
    """
    return base ** exponent

def factorial(n: int) -> int:
    """Вычисляет факториал числа.

    Args:
        n (int): Число, для которого нужно вычислить факториал.

    Returns:
        int: Факториал числа n.

    Raises:
        ValueError: Если n отрицательное.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
