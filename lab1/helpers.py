def is_relatively_prime(a, b):
    """
    Проверяет, являются ли числа a и b взаимно простыми.

    Args:
        a (int): Первое число для проверки.
        b (int): Второе число для проверки.

    Returns:
        bool: True, если числа взаимно простые; False в противном случае.
    """
    a = abs(a)
    b = abs(b)
    if a == 0 or b == 0:
        return False
    if a == 1 and b == 1:
        return True
    while b != 0:
        a, b = b, a % b
    return a == 1


def load_keyword_list(file_path):
    """
    Метод загрузки слов в массив
    :param file_path: Путь до файла со словами
    :return: Массив слов
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f]
