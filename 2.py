def bubble_sort(n):
    """
    сортировка матрицы пузырьком по первому столбцу (сложность n ** 2)
    :param n: Матрица, которую необходимо отсортировать
    :return: Отсортированная матрица
    """

    for i in range(len(n) - 1):
        for o in range(i + 1, len(n)):
            if int(n[i][0]) < int(n[o][0]):
                n[i], n[o] = n[o], n[i]

    return n


def main():
    """
    основная функция программы
    :return: None
    """

    with open("songs.txt", encoding="utf-8") as input_file:
        t = [i.strip().split("?") for i in input_file][1:]

    t = bubble_sort(t)[:5]
    for i in t:
        print(f"{i[2]}, {i[1]}, {i[3]}")


main()
