import numpy as np
from PIL import Image
import svgwrite
import math

DMC = {
    # Чёрные, серые, белые
    "3777": (0, 0, 0),          # чёрный
    "3776": (34, 34, 34),       # тёмно-серый
    "413": (68, 68, 68),        # серый
    "414": (102, 102, 102),     # серо-голубой
    "415": (136, 136, 136),     # светло-серый
    "745": (163, 73, 164),      # фиолетовый (оставлен из вашего списка)
    "310": (187, 187, 187),     # очень светлый серый
    "776": (255, 255, 255),     # белый

    # Красные и розовые
    "150": (237, 28, 36),       # ярко-красный
    "321": (218, 41, 28),       # красный
    "320": (180, 24, 12),       # тёмно-красный
    "3801": (255, 102, 102),    # светло-красный
    "921": (255, 174, 201),     # розовый
    "3716": (255, 153, 153),    # нежно-розовый
    "3713": (204, 102, 153),    # розово-фиолетовый
    "3802": (255, 204, 204),    # очень светлый розовый

    # Оранжевые
    "970": (255, 127, 39),      # оранжевый
    "971": (255, 165, 79),      # светло-оранжевый
    "720": (204, 85, 0),        # тёмно-оранжевый
    "721": (230, 126, 34),      # тыквенный
    "972": (255, 204, 153),     # персиковый

    # Жёлтые
    "928": (255, 242, 0),       # ярко-жёлтый
    "444": (255, 215, 0),       # золотистый
    "725": (255, 229, 153),     # светло-жёлтый
    "726": (255, 247, 204),     # очень светлый жёлтый
    "727": (255, 255, 229),     # кремовый

    # Зелёные
    "823": (181, 230, 29),      # ярко-зелёный
    "822": (144, 198, 0),       # зелёный
    "821": (102, 153, 0),       # тёмно-зелёный
    "820": (76, 115, 0),        # оливково-зелёный
    "824": (204, 255, 153),     # светло-зелёный
    "825": (230, 255, 204),     # очень светлый зелёный
    "907": (153, 204, 153),     # серо-зелёный
    "906": (128, 179, 128),     # приглушённый зелёный

    # Голубые и синие
    "336": (0, 168, 243),       # ярко-голубой
    "335": (0, 136, 187),       # голубой
    "334": (0, 102, 153),       # тёмно-голубой
    "333": (0, 68, 102),        # очень тёмно-голубой
    "3808": (112, 146, 190),    # серо-голубой
    "3809": (153, 187, 221),    # светло-серо-голубой
    "3810": (204, 221, 238),    # очень светлый серо-голубой
    "809": (0, 0, 153),         # тёмно-синий
    "808": (51, 51, 204),       # синий
    "807": (102, 102, 255),     # светло-синий
    "806": (153, 153, 255),     # бледно-синий

    # Фиолетовые и сиреневые
    "550": (102, 0, 102),       # тёмно-фиолетовый
    "552": (153, 51, 153),      # фиолетовый
    "553": (204, 102, 204),     # светло-фиолетовый
    "554": (230, 153, 230),     # нежно-фиолетовый
    "3838": (179, 143, 194),    # сиреневый
    "3839": (217, 191, 229),    # светло-сиреневый

    # Коричневые и бежевые
    "304": (185, 122, 87),      # коричневый
    "300": (102, 51, 0),        # тёмно-коричневый
    "838": (153, 102, 51),      # кофейный
    "839": (204, 153, 102),     # светло-коричневый
    "840": (230, 191, 153),     # бежевый
    "841": (247, 224, 191),     # кремово-бежевый
    "834": (128, 96, 64),       # тёплый коричневый
    "832": (179, 143, 107),     # золотисто-коричневый

    # Пастельные и нейтральные
    "3822": (239, 228, 176),    # светло-бежевый (песочный)
    "3823": (255, 248, 220),    # очень светлый беж
    "3824": (210, 180, 140),    # загар
    "3825": (160, 120, 90),     # тёмный загар
    "3826": (190, 160, 120),    # тёплый беж

    # Дополнительные популярные цвета
    "734": (102, 102, 102),     # графит
    "318": (204, 0, 0),         # кирпичный
    "322": (255, 153, 153),     # светло-красный (альтернатива)
    "938": (153, 204, 255),     # небесно-голубой
    "939": (204, 229, 255),     # очень светлый голубой
    "945": (102, 204, 153),     # бирюзовый
    "946": (153, 229, 179),     # светлая бирюза
    "947": (204, 255, 229),     # бледная бирюза
    "3850": (255, 201, 14),     # золотисто-оранжевый
    "3851": (255, 229, 153),    # светлый золотистый
    "3852": (255, 242, 204),    # очень светлый золотистый
    "3853": (236, 125, 141),    # коралловый
    "3854": (255, 179, 179),    # светлый коралл
    "3855": (255, 229, 229),    # бледный коралл
    "3857": (200, 191, 231),    # лавандовый
    "3858": (229, 221, 247),    # светлая лаванда
    "3859": (247, 242, 255),    # очень светлая лаванда
    "3860": (204, 153, 102),    # тёплый беж (альтернатива)
    "3861": (230, 191, 153),    # светлый загар
    "3862": (247, 224, 191),    # крем
    "3863": (185, 122, 87),     # коричневый (дубликат для удобства)
    "3864": (153, 102, 51),     # тёмный коричневый
    "3865": (128, 128, 128),    # серый (для контраста)
}

DMC_COLORS = np.array(list(DMC.values()))
DMC_NUMS = list(DMC.keys())

SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

def find_closest_dmc(rgb):
    rgb = np.array(rgb)
    distances = np.linalg.norm(DMC_COLORS - rgb, axis=1)
    idx = int(np.argmin(distances))
    return DMC_NUMS[idx], tuple(DMC_COLORS[idx])

def resize_to_max_pixels(img, max_pixels):
    w, h = img.size
    if w * h <= max_pixels:
        return img
    scale = math.sqrt(max_pixels / (w * h))
    new_w = int(w * scale)
    new_h = int(h * scale)
    return img.resize((new_w, new_h), Image.LANCZOS)

def image_to_dmc_grid(img, max_colors=10):
    w, h = img.size
    pixels = np.array(img)
    grid = []
    color_map = {}

    for y in range(h):
        row = []
        for x in range(w):
            r, g, b = pixels[y, x]
            dmc_code, _ = find_closest_dmc((r, g, b))
            row.append(dmc_code)
        grid.append(row)

    unique_colors = list(dict.fromkeys([code for row in grid for code in row]))
    if len(unique_colors) > max_colors:
        unique_colors = unique_colors[:max_colors]

    for i, code in enumerate(unique_colors):
        if i < len(SYMBOLS):
            color_map[code] = SYMBOLS[i]
        else:
            color_map[code] = "?"

    if len(unique_colors) < len(set([code for row in grid for code in row])):
        most_common = unique_colors[0]
        for y in range(h):
            for x in range(w):
                if grid[y][x] not in unique_colors:
                    grid[y][x] = most_common

    return grid, color_map

def save_svg(grid, color_map, filename):
    h, w = len(grid), len(grid[0])
    cell = 20
    margin = 30
    legend_width = 250

    dwg = svgwrite.Drawing(filename, size=(w * cell + margin * 2 + legend_width, h * cell + margin * 2))

    for y in range(h):
        for x in range(w):
            dmc = grid[y][x]
            rgb = DMC[dmc]
            hex_color = f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"
            symbol = color_map.get(dmc, "?")

            dwg.add(dwg.rect((margin + x * cell, margin + y * cell), (cell, cell),
                             fill=hex_color, stroke="black", stroke_width=0.5))

            text_color = "white" if sum(rgb) < 400 else "black"
            dwg.add(dwg.text(symbol,
                             insert=(margin + x * cell + cell / 2, margin + y * cell + cell / 2),
                             text_anchor="middle", dominant_baseline="middle",
                             font_size=10, fill=text_color))

    for i in range(0, w + 1):
        if i % 10 == 0:
            dwg.add(dwg.line((margin + i * cell, margin),
                             (margin + i * cell, margin + h * cell),
                             stroke="red", stroke_width=1, stroke_dasharray="4,2"))
    for j in range(0, h + 1):
        if j % 10 == 0:
            dwg.add(dwg.line((margin, margin + j * cell),
                             (margin + w * cell, margin + j * cell),
                             stroke="red", stroke_width=1, stroke_dasharray="4,2"))

    legend_x = margin + w * cell + 20
    for i, (dmc, sym) in enumerate(color_map.items()):
        y = margin + i * 25
        rgb = DMC[dmc]
        hex_color = f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"
        dwg.add(dwg.rect((legend_x, y), (20, 20), fill=hex_color, stroke="black"))
        dwg.add(dwg.text(f"{sym} — DMC {dmc}", insert=(legend_x + 25, y + 15), font_size=14))

    dwg.save()
    print(f"Схема сохранена: {filename}")


if __name__ == "__main__":
    input_path = "1.jpg"       
    max_colors = 80                   
    max_pixels = 25000                 
    output_path = "2.svg"

    img = Image.open(input_path).convert("RGB")
    img = resize_to_max_pixels(img, max_pixels)

    grid, color_map = image_to_dmc_grid(img, max_colors)

    save_svg(grid, color_map, output_path)