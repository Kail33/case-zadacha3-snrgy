import sys


def sum_negative_between(a):
    """Сумма отрицательных элементов между максимумом и минимумом."""
    if not a:
        raise ValueError("Массив не должен быть пустым")

    i_max = a.index(max(a))  # индекс первого максимального элемента
    i_min = a.index(min(a))  # индекс первого минимального элемента

    left, right = sorted((i_max, i_min))  # границы участка слева направо

    total = 0
    for x in a[left + 1:right]:  # элементы строго между границами
        if x < 0:
            total += x
    return total


def read_size():
    """Запрашивает размерность массива, пока не введено натуральное число."""
    while True:
        text = input("Введите размерность массива N: ").strip()
        try:
            n = int(text)
        except ValueError:
            n = 0
        if n > 0:
            return n
        print("Ошибка: N должно быть натуральным числом, например 8.")


def read_array(n):
    """Запрашивает элементы, пока не будет введено ровно n чисел."""
    a = []
    while len(a) < n:
        rest = n - len(a)
        line = input(f"Введите элементы массива (осталось {rest}): ")
        parts = line.replace(",", " ").replace(";", " ").split()
        try:
            numbers = [float(x) for x in parts]
        except ValueError:
            print("Ошибка: вводить нужно только числа. Повторите ввод.")
            continue
        if len(numbers) > rest:
            print(f"Ошибка: введено {len(numbers)} чисел, а нужно {rest}.")
            continue
        a.extend(numbers)
    return a


def main():
    n = read_size()
    a = read_array(n)

    result = sum_negative_between(a)
    print(f"Максимальный элемент: {max(a):g} (индекс {a.index(max(a))})")
    print(f"Минимальный элемент: {min(a):g} (индекс {a.index(min(a))})")
    print(f"Сумма отрицательных элементов между ними: {result:g}")


if __name__ == "__main__":
    main()
    if sys.stdin.isatty():  # чтобы окно не закрылось сразу после ответа
        input("Нажмите Enter, чтобы закрыть программу...")
