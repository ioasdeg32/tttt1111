def bubble_sort(n):
    """
    сортировка матрицы пузырьком по третьему столбцу (сложность n ** 2)
    :param n: Матрица, которую необходимо отсортировать
    :return: Отсортированная матрица
    """

    for i in range(len(n) - 1):
        for o in range(i + 1, len(n)):
            if n[i][2] < n[o][2]:
                n[i], n[o] = n[o], n[i]

    return n


def binary_search(n, k):
    """
    двоичный поиск по третьему столбцу
    :param n: матрица, в которой необходимо значение k в третьем столбце
    :param k: значение, которое необходимо найти
    :return: строка матрицы, в которой найдено заданное значение
    """

    left = 0
    right = len(n)

    while left != right:
        mid = n[(left + right) // 2]

        if mid[2] == k:
            return mid
        elif mid[2] > k:
            left = (left + right) // 2 + 1
        else:
            right = (left + right) // 2

    return "К сожалению, ничего не удалось найти"


def main():
    """
    основная функция программы
    :return: None
    """

    track_name = input()

    with open("songs.txt", encoding="utf-8") as input_file:
        t = [i.strip().split("?") for i in input_file][1:]
    t = bubble_sort(t)

    while track_name != "0":
        st = binary_search(t, track_name)

        if type(st) is str:
            print(st)
        else:
            print(f"Песня {track_name} принадлежит {st[1]}")

        track_name = input()


main()
