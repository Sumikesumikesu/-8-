import os
import pandas as pd
from tqdm import tqdm

from get_names_of_five_dominant_colors import get_names_of_five_dominant_colors
from get_sheets_formulas_to_insert_color import get_sheets_formula


def main():
    dominat_color_palette_data = [] 

    folder_path = 'Папка с фотографиями для разбора'
    image_list = os.listdir(folder_path)
    os.chdir(folder_path)
    
    # Составим таблицу Фото | Цвет 1 | ... | Цвет 5 | 5 формул для визуализации цветов 
    for i in tqdm(image_list):
        list_of_color_names = get_names_of_five_dominant_colors(i)
        dominat_color_palette_data.append(
                            [i] + \
                            list_of_color_names + \
                            [get_sheets_formula(name) for name in list_of_color_names])
    
    header = ['Фото','Цвет 1', 'Цвет 2', 'Цвет 3', 'Цвет 4', 'Цвет 5', '', '', '', '', '']
    df_palettes = pd.DataFrame(dominat_color_palette_data, columns=header)
    os.chdir(os.pardir) 
    
    # Сделаем частотный анализ и сохраним на другом листе
    df_frequency = df_palettes.iloc[:, 1:5].stack().value_counts().reset_index()
    
    with pd.ExcelWriter('fivedominantcolors.xlsx') as writer:
        df_palettes.to_excel(writer, sheet_name='Палитры', index=False)
        df_frequency.to_excel(writer, sheet_name='Частота цвета', header=['Цвет', 'Частота'], index=False)


if __name__ == '__main_':
    main()
