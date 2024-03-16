import csv


def main():
    """
    основная функция программы
    :return: None
    """

    artist_name = input()

    info = []
    with open("songs.txt", encoding="utf-8") as input_file:
        for i in input_file.readlines():
            i = i.strip().split("?")
            if i[1] == artist_name:
                info.append(i)

    with open("songs_artst.csv", mode="w", newline="", encoding="utf-8") as output_file:
        writer = csv.writer(output_file, delimiter=",")
        writer.writerow(["track_name", "streams", "date"])
        for t in info:
            writer.writerow([t[2], t[0], t[3]])


main()
