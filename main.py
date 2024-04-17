from src.get_api_hh import GetApiHH
from src.save_to_fromat_file import SaveToFormatFile


def user_interface():
    """
    Юзер
    :return: данные
    """

    user_input = input('Введите поисковой запрос: ')
    get_json = GetApiHH(user_input).get_vacancy()
    sort_list = sorted(get_json, reverse=True)
    user_input = int(input('Введите количество вакансий которое хотите увидеть: '))
    for i in range(user_input):
        print(f"{sort_list[i]}")

    input_save = input('Хотите сохранить файл? Строго введите "да" или "нет"!: ')
    match input_save:
        case 'да':
            SaveToFormatFile().save_vacancy_to_file(sort_list)
            print(f'Файл сохранён')
        case 'нет':
            print(f'Файл не будет сохранён')
        case _:
            print(f"неверный ввод для сохранения")

    input_del = input('Хотите очистить файл? Строго введите "да" или "нет"!: ')
    match input_del:
        case 'да':
            SaveToFormatFile().del_vacancy_from_file()
            print(f'Файл чист')
        case 'нет':
            print(f'Файл не будет очищен')
        case _:
            print(f"неверный ввод для удаления")
    input_read = input('Хотите открыть файл? Строго введите "да" или "нет"!: ')
    match input_read:
        case 'да':
            SaveToFormatFile(sort_list).read_vacancy_from_file()
            print(f'Файл открыт')
        case 'нет':
            print(f'Ну и ладно')
        case _:
            print(f"Зачем вы это ввели?")


result = user_interface()

# read = SaveToFormatFile().find_operations_json("my_vacancy.json")
# print(read)