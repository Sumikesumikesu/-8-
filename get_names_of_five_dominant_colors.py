from colorthief import ColorThief
import webcolors

# функиция, которая извлекает 5 доминирующих цветов из изображения 
def get_five_dominant_colors_rgb(image):
    # Создаём объекта ct класса ColorThief и передаём ему изображение
    ct = ColorThief(image)
    # Получаем палитру из 5 цветов в формате RGB с помощью 
    # метода get_palette у объекта ct
    five_color_rgb_palette = ct.get_palette(color_count=5)

    return five_color_rgb_palette

# функция, которая находит ближайший цвет к исходному оттенку
def get_closest_color_to_shade(color_rgb):
    differences = {} # пустой словарь, который будет хранить разницы между цветами
    
    # расчитаем разницу между каждым цветом в словаре webcolors.CSS3_HEX_TO_NAMES,
    # который содержит 138 цветов в формате HEX и их названия
    for color_hex, color_name in webcolors.CSS3_HEX_TO_NAMES.items():
        r,g,b = webcolors.hex_to_rgb(color_hex)

        # вычисляем разницу между каждым цветом в словаре webcolors.CSS3_HEX_TO_NAMES
        # и исходным color_rgb, сохраняем в словарь
        differences[sum([(r - color_rgb[0]) ** 2,
                         (g - color_rgb[1]) ** 2,
                         (b - color_rgb[2]) ** 2])] = color_name
        
    # находим цвет с минимальной разницей с иходным и возращаем его RGB 
    closest_color_to_shade = differences[min(differences.keys())]
    return closest_color_to_shade 

# функция, которая получет название цвета по его RGB-коду 
def get_color_names(color_rgb): 
    try:
        cname = webcolors.rgb_to_name(color_rgb)
        return cname
    except ValueError:
        cname = get_closest_color_to_shade(color_rgb)
        return cname
    
# функция, которая получает названия 5 
def get_names_of_five_dominant_colors(image):
    list_of_color_names_in_palette = []

    palette = get_five_dominant_colors_rgb(image)

    for c_rgb in palette:
        list_of_color_names_in_palette.append(get_color_names(c_rgb))
    return list_of_color_names_in_palette    
