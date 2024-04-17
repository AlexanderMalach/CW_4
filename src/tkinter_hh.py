from tkinter import *

from src.get_api_hh import GetApiHH
from src.save_to_fromat_file import SaveToFormatFile


def get_api():
    user_input = hh_api.get()
    get_json = GetApiHH(user_input).get_vacancy()
    sort_list = sorted(get_json, reverse=True)
    user_input = list_vacancy.get()
    for i in range(int(user_input)):
        output_text.insert(END, f"{sort_list[i]}" + "\n")


def save_file():
    user_input = hh_api.get()
    get_json = GetApiHH(user_input).get_vacancy()
    sort_list = sorted(get_json, reverse=True)
    user_input = list_vacancy.get()
    SaveToFormatFile(sort_list).save_vacancy_to_file()


root = Tk()
root.title("Курсовой проект №4")
root.geometry('1200x640')
root.resizable(width=False, height=False)
root['bg'] = 'black'

label_find = Label(root, text='Введите поисковой запрос: ', font='Arial 15 bold', fg='white', bg='grey', width=100,
                   height=1)
label_find.pack(pady=10, padx=0)
hh_api = Entry(root, font='Arial 15 bold')
hh_api.pack()
label_quantity_vacancy = Label(root, text='Введите количество вакансий которое хотите увидеть: ', font='Arial 15 bold',
                               fg='white', bg='grey', width=100, height=1)
label_quantity_vacancy.pack()
list_vacancy = Entry(root, font='Arial 15 bold')
list_vacancy.pack()

btn_vacancy = Button(root, text='Запуск', font='Arial 15 bold', command=get_api)
btn_vacancy.pack()

btn_save = Button(root, text='Сохранить в файл', font='Arial 15 bold', command=save_file)
btn_save.pack()

output_text = Text(root, width=130, height=50)
output_text.pack(side=BOTTOM)
root.mainloop()

# SaveToFormatFile(sort_list).del_vacancy_from_file()
