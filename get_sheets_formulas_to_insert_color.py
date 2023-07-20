import webcolors
import pandas as pd

"""
Чтобы визиуализировать палитру внутри гугл таблицы, я буду 
использовать фукнцию IMAGE, которая вставляет в ячейку изобрвжение по его URL.
"""

def get_sheets_formula(color_name):
    hex = webcolors.name_to_hex(color_name).replace("#", "")
    # Сформируем URL, по которому можно найти картинку цвета на сайте colorhexa.com
    url = 'https://www.colorhexa.com/' + hex + '.png' 
    formula =  f'=IMAGE("{url}"; 2)'
    return formula