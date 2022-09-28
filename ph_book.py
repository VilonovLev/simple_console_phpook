from operator import index
from turtle import color
from interface_txt import *
from interface_csv import *
from logger import write_log

action_list = ["", '1 - Список команд', '2 - Найти запись', '3 - Вывести весь список',
               '4 - Удалить запись', '5 - Добавить запись', '6 - Импорт из txt файла',
               '7 - Экспорт в txt файл', '8 - Завершение работы']


def start():
    print('\033[93mТелефонный справочник\033[0m')
    write_log(['Начало работы', True])
    help()
    while True:
        print('\033[93m-\033[0m'*70)
        act = action()
        if act == action_list.index('1 - Список команд'):
            help()
            write_log([action_list[act][4:], True])
        elif act == action_list.index('2 - Найти запись'):
            flag = print_dir(search_row(input('Что ищем? ')))
            write_log([action_list[act][4:], flag])
        elif act == action_list.index('3 - Вывести весь список'):
            flag = print_dir(read_rows())
            write_log([action_list[act][4:], flag])
        elif act == action_list.index('4 - Удалить запись'):
            flag = reset_row(input('Укажите id записи, для удаления: '))
            write_log([action_list[act][4:], flag])
        elif act == action_list.index('5 - Добавить запись'):
            flag = appdir()
            write_log([action_list[act][4:], flag])
        elif act == action_list.index('6 - Импорт из txt файла'):
            flag = import_txt()
            write_log([action_list[act][4:], flag])
        elif act == action_list.index('7 - Экспорт в txt файл'):
            flag = export_txt()
            write_log([action_list[act][4:], flag])
        elif act == action_list.index('8 - Завершение работы'):
            print('\033[93mДо встречи в Play маркетах! )\033[0m')
            write_log([action_list[act][4:], True])
            break


def action():
    while True:
        act = input("Что вы хотите сделать? ")
        if not act.isdigit():
            print("Неверный запрос!")
        elif int(act) > len(action_list) - 1 or int(act) == 0:
            print("Такой команды пока нет(")
        else:
            return int(act)


def help():
    print('\033[92mДоступные команды:\033[0m')
    for i in action_list[1:]:
        print(i)


def appdir():
    app_dir = read_rows()
    new_person = [input(f'Введите {app_dir[0][i]}: ')
                  for i in range(len(app_dir[0]))]
    write_row(new_person)
    return True


def print_dir(dir):
    if len(dir) < 2:
        print("Запись не найдена!")
        return False
    else:
        for i in range(len(dir)):
            if i == 0:
                row = "ID  "
            else:
                row = f'{i}{" "*(4-len(str(i)))}'
            for j in range(len(dir[i])):
                temp = (dir[i])[j]
                row += f'|{temp}{" "*(16-len(temp))}'
            print(row)
        return True


def reset_row(ind):
    if not ind.isdigit():
        print("Некорректный ввод!")
        return False
    else:
        ind = int(ind)
    dir = read_rows()
    if ind < 1 or ind > len(dir):
        print("Запись не найдена")
        return False
    else:
        dir.pop(ind)
        reset_dir(dir)
    return True


def import_txt():
    try:
        path = input('Введите имя файла: ')
    except:
        print('Файл не найден!')
        return False
    delimiter = input('Укажите разделитель: ')
    exp_list = read_txt(path, delimiter)
    for person in exp_list:
        write_row(person)
    return True


def export_txt():
    path = input('Введите имя файла: ')
    delimiter = input('Укажите разделитель: ')
    dir = read_rows()
    write_txt(path, dir, delimiter)
    return True
