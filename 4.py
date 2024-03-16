def main():
    """
    основная функция программы
    :return: None
    """

    with open("songs.txt", encoding="utf-8") as input_file:
        t = [i.strip().split("?") for i in input_file][1:]

    artst = dict()
    artst_1990 = []

    for i in t:
        if int(i[3].split(".")[-1]) < 1990:
            if i[1] not in artst_1990:
                artst_1990.append(i[1])
        if i[1] not in artst.keys():
            artst[i[1]] = [int(i[0]), 1]
        else:
            artst[i[1]][0] += int(i[0])
            artst[i[1]][1] += 1

    print(" ".join(artst_1990))

    artst = [[i, artst[i][0] // artst[i][1]] for i in artst.keys()]
    artst.sort(key=lambda x: x[1], reverse=True)

    with open("songs_average.txt", mode="w", encoding="utf-8") as output_file:
        output_file.write(f"{" ".join(artst_1990)}\n")
        for i in artst:
            print(f"{i[0]}: {i[1]}")
            output_file.write(f"{i[0]}: {i[1]}\n")


main()
