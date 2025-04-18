def factorial(n):
    """
    Обчислює факторіал додатного числа n.
    Параметри:
        n (int): додатне ціле число
    Повертає:
        int: факторіал числа n
    """
    if n < 0:
        raise ValueError("Число повинно бути додатним")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    n = 5
    print(f"Факторіал числа {n} дорівнює {factorial(n)}")
