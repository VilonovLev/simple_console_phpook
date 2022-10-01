
def read_txt(path, delimiter):
    try:
        with open(path, "r", encoding="UTF8") as f:
            result = (i[:-1].split(delimiter) for i in f.readlines())
            return result
    except:
        print("Ошибка импорта!")
            

def write_txt(path, dir, delimiter):
    with open(path, "a", encoding="UTF8") as f:
        for row in dir:
            result = ""
            for i in row:
                result += str(i) + delimiter
            f.write(result[:-1] + '\n') 