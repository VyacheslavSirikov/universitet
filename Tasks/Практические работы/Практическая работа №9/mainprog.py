import os

import handler
from conver import convert_pdf_to_docx, convert_docx_to_pdf
from imag import image_resize


def incorrect_command() -> None: print('Неверная команда\n----------')


def change_dir(new_dir: str) -> str:
    if os.path.isdir(new_dir):
        os.chdir(new_dir)
    else:
        return 'Неверный путь'

    return new_dir


def main():
    while True:
        print('Текущий каталог: ' + os.getcwd())
        print('Выберите действие: \n')
        print('0. Сменить рабочий каталог\n'
              '1. Преобразовать PDF в Docx\n'
              '2. Преобразовать Docx в PDF\n'
              '3. Произвести сжатие изображений\n'
              '4. Удалить группу файлов\n'
              '5. Выход')

        try:
            command = int(input())
            if command == 0:
                print(change_dir(input('Введите путь: ')))
            elif command == 1:
                convert_pdf_to_docx()
            elif command == 2:
                convert_docx_to_pdf()
            elif command == 3:
                image_resize()
            elif command == 4:
                print('Выберите действие: \n')
                print('1. Удалить все файлы начинающиеся на определенную подстроку \n'
                      '2. Удалить все файлы заканчивающиеся на определенную подстроку \n'
                      '3. Удалить все файлы содержащие определенную подстроку \n'
                      '4. Удалить все файлы по расширению')

                subcommand = int(input('Введите номер действия: '))
                key = input('Введите подстроку: ')

                if subcommand == 1:
                    handler.delete_files_starts_with(key)
                elif subcommand == 2:
                    handler.delete_files_ends_with(key)
                elif subcommand == 3:
                    handler.delete_files_with(key)
                elif subcommand == 4:
                    handler.delete_files_with_ext(key)
                else:
                    incorrect_command()
            elif command == 5:
                break
            else:
                incorrect_command()
        except ValueError:
            incorrect_command()


main()