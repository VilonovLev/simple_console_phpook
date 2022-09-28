import csv
from encodings import utf_8
from unittest import result


def read_rows(delimiter=';', path='directory.csv'):
    with open(path, "r", encoding="UTF8") as f:
        result = ""
        if delimiter != ';':
            result = list(csv.reader(f))
        else:
            result = [i[0].split(delimiter) for i in csv.reader(f)]
        return result


def write_row(person, path='directory.csv'):
    if person in read_rows():
        return False
    else:
        with open(path, "a", encoding="UTF8") as f:
            csv.writer(f, delimiter=';', lineterminator="\r").writerow(person)
            return True


def search_row(data):
    rows = read_rows()
    list_row = [rows[0]]
    for i in rows[1:]:
        t = False
        for j in i:
            if rf"{data}" in j:
                t = True
        if t:
            list_row.append(i)
    return list_row


def reset_dir(new_dir, path='directory.csv'):
    with open(path, "w", encoding="UTF8") as f:
        for row in new_dir:
            csv.writer(f, delimiter=';', lineterminator="\r").writerow(row)
        return
