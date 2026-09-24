#!/usr/bin/env python3
"""
INFO SEC LABS CTF - Task 1 Solver
Поиск изображения с логотипом IITU среди 10 000 зашумленных PNG-файлов.
"""

import sys
import os
import zipfile
import io
from PIL import Image

ZIP_PATH = os.path.join(os.path.dirname(__file__), "iitu_10000.zip")

def solve():
    if not os.path.exists(ZIP_PATH):
        print(f"[-] Файл {ZIP_PATH} не найден!")
        sys.exit(1)

    print("[*] Анализируем структуру архива без распаковки на диск...")
    with zipfile.ZipFile(ZIP_PATH, 'r') as zf:
        infolist = zf.infolist()
        total = len(infolist)
        print(f"[+] Всего файлов в архиве: {total}")

        # Быстрый поиск аномалии по размеру блока сжатых данных IDAT:
        # В 9999 файлах пиксели перемешаны в белый шум (плохо сжимаются zlib).
        # В настоящем файле связный текст/логотип (высокая степень локальной корреляции -> малый IDAT).
        min_idat_len = float('inf')
        target_entry = None

        for item in infolist:
            raw = zf.read(item.filename)
            # Ищем чанк IDAT
            pos = 8
            while pos < len(raw):
                l = int.from_bytes(raw[pos:pos+4], 'big')
                ct = raw[pos+4:pos+8]
                if ct == b'IDAT':
                    if l < min_idat_len:
                        min_idat_len = l
                        target_entry = item
                    break
                pos += 12 + l

        print(f"[+] Найдена аномалия сжатия: {target_entry.filename}")
        print(f"    Размер IDAT: {min_idat_len} байт (у остальных ~3500-3760 байт)")

        folder_id, filename = target_entry.filename.split('/')
        folder_num = int(folder_id)

        # Отрисуем превью в ASCII
        img_data = zf.read(target_entry.filename)
        im = Image.open(io.BytesIO(img_data))
        w, h = im.size
        pixels = im.load()

        print("\n[+] Отрисовка найденного изображения (IITU):")
        print("-" * 60)
        for y in range(0, h, 2):
            line = "".join(" " if pixels[x, y] > 250 else "█" for x in range(0, w, 2))
            if "█" in line:
                print(line)
        print("-" * 60)

        # Вычисляем флаг и пароль к следующей задаче
        flag_part1 = f"Flag_{{{filename}_}}"
        task2_pass = folder_num ** 3

        print(f"\n[+] Итоги Задачи №1:")
        print(f"    Папка ID:               {folder_num}")
        print(f"    Имя файла:              {filename}")
        print(f"    Флаг части 1:           {flag_part1}")
        print(f"    Пароль к Task2.rar:     {task2_pass} ({folder_num}^3)")

if __name__ == "__main__":
    solve()
