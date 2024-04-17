import sys
from tkinter import *

from src.get_api_hh import GetApiHH
from src.save_to_fromat_file import SaveToFormatFile


def get_api():
    """
    Получает данные о вакансиях с помощью API HeadHunter и отображает их в окне приложения.
    """
    output_text.delete(1.0, END)  # Очищаем текстовое поле перед выводом новых данных
    user_input = hh_api.get()
    get_json = GetApiHH(user_input).get_vacancy()
    sort_list = sorted(get_json, reverse=True)
    user_input = (list_vacancy.get())
    if isinstance(user_input, int):
        for i in range(user_input):
            output_text.insert(END, f"{sort_list[i]}\n")
    else:
        user_input = 10
        for i in range(user_input):
            output_text.insert(END, f"{sort_list[i]}\n")


def save_file():
    """
    Получает данные о вакансиях с помощью API HeadHunter и сохраняет их в файл.
    """
    output_text.delete(1.0, END)  # Очищаем текстовое поле перед выводом новых данных
    user_input = hh_api.get()
    try:
        get_json = GetApiHH(user_input).get_vacancy()
        sort_list = sorted(get_json, reverse=True)
        SaveToFormatFile().save_vacancy_to_file(sort_list)
        output_text.insert(END, "Данные успешно сохранены в файл.\n")
    except Exception as e:
        error_message = f"Ошибка: {e}"
        output_text.insert(END, error_message)


def clear_file():
    """
    Очищает содержимое файла.
    """
    output_text.delete(1.0, END)  # Очищаем текстовое поле перед выводом новых данных
    SaveToFormatFile().del_vacancy_from_file()
    output_text.insert(END, "Содержимое файла успешно удалено.\n")


def read_file():
    """
    Открывает и читает содержимое файла.
    """
    output_text.delete(1.0, END)  # Очищаем текстовое поле перед выводом новых данных
    try:
        vacancies = SaveToFormatFile().read_vacancy_from_file()
        for vacancy in vacancies:
            output_text.insert(END, f"{vacancy}\n")
    except FileNotFoundError:
        output_text.insert(END, "Файл не найден.\n")


root = Tk()
root.title("Курсовой проект №4")
root.geometry('800x600')
root.resizable(width=False, height=False)
root.configure(bg='white')

input_frame = Frame(root, bg='white')
input_frame.pack(pady=20)

label_find = Label(input_frame, text='Введите поисковой запрос:', font=('Arial', 12), bg='white')
label_find.grid(row=0, column=0, padx=(10, 0))

hh_api = Entry(input_frame, font=('Arial', 12))
hh_api.grid(row=0, column=1, padx=10)

label_quantity_vacancy = Label(input_frame, text='Введите количество вакансий:', font=('Arial', 12), bg='white')
label_quantity_vacancy.grid(row=1, column=0, padx=(10, 0))

list_vacancy = Entry(input_frame, font=('Arial', 12))
list_vacancy.grid(row=1, column=1, padx=10)

btn_vacancy = Button(root, text='Запуск', font=('Arial', 12), command=get_api)
btn_vacancy.pack(pady=10)

btn_save = Button(root, text='Сохранить в файл', font=('Arial', 12), command=save_file)
btn_save.pack(pady=10)

btn_clear = Button(root, text='Очистить файл', font=('Arial', 12), command=clear_file)
btn_clear.pack(pady=10)

btn_read = Button(root, text='Открыть файл', font=('Arial', 12), command=read_file)
btn_read.pack(pady=10)

output_text = Text(root, width=80, height=20)
output_text.configure(state='normal')
output_text.pack(pady=20)

# Перенаправляем стандартный вывод ошибок в текстовое поле
sys.stderr = output_text

root.mainloop()
