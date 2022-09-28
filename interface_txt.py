
def read_txt(path, delimiter):
    with open(path, "r", encoding="UTF8") as f:
        result = [i[:-1].split(delimiter) for i in f.readlines()]
        return result

def write_txt(path, dir, delimiter=';'):
    with open(path, "a", encoding="UTF8") as f:
        for row in dir:
            f.write(str(delimiter).join(row) + '\n') 