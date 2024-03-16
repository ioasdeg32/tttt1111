def main():
    """
    основная функция программы
    :return: None
    """

    with open("songs.txt", encoding="utf-8") as input_file:
        t = [i.strip().split("?") for i in input_file][1:]

    table = dict()
    track_names = []

    for i in t:
        track_name = i[2]
        track_names.append(track_name)
        i.remove(track_name)
        count = track_names.count(track_name)

        table[track_name + f"_{count}"] = [{"streams": i[0], "artist": i[1], "date": i[2]}]

    track_name = input()
    for i in range(1, track_names.count(track_name) + 1):
        print(f'{track_name}: {table[track_name + f"_{i}"]}')


main()
