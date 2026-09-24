#!/usr/bin/env python3
"""
INFO SEC LABS CTF - Task 2 Solver
Сборка разрезанного по вертикали радужного QR-кода и получение информации об артисте.
"""

import os
import sys
import subprocess
from PIL import Image
import cv2

BASE_DIR = os.path.dirname(__file__)
RAR_PATH = os.path.join(BASE_DIR, "Task2.rar")
STRIPS_DIR = os.path.join(BASE_DIR, "strips")
OUT_IMG = os.path.join(BASE_DIR, "rainbow_qr.png")

# Порядок полос по спектру радуги (Каждый Охотник Желает Знать Где Сидит Фазан)
# 7: Красный
# 4: Оранжевый
# 6: Жёлтый
# 1: Зелёный
# 5: Голубой
# 2: Синий
# 3: Фиолетовый
RAINBOW_ORDER = [7, 4, 6, 1, 5, 2, 3]

def solve():
    # Если полоски ещё не распакованы, распакуем из Task2.rar
    if not os.path.exists(STRIPS_DIR) or len(os.listdir(STRIPS_DIR)) < 7:
        print("[*] Распаковываем Task2.rar паролем '306318327021'...")
        os.makedirs(STRIPS_DIR, exist_ok=True)
        res = subprocess.run([
            "7z", "x", "-p306318327021", f"-o{STRIPS_DIR}", RAR_PATH, "-y"
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if res.returncode != 0:
            print("[-] Ошибка распаковки архива:", res.stderr.decode(errors='ignore'))
            sys.exit(1)

    print("[*] Склеиваем полоски в радужном порядке [7, 4, 6, 1, 5, 2, 3]...")
    strips = {}
    for i in range(1, 8):
        p = os.path.join(STRIPS_DIR, f"{i}.png")
        if not os.path.exists(p):
            print(f"[-] Файл {p} не найден!")
            sys.exit(1)
        strips[i] = Image.open(p)

    total_width = sum(strips[i].width for i in RAINBOW_ORDER)
    height = strips[1].height
    merged = Image.new("RGB", (total_width, height))

    curr_x = 0
    for idx in RAINBOW_ORDER:
        im = strips[idx]
        merged.paste(im, (curr_x, 0))
        curr_x += im.width

    merged.save(OUT_IMG)
    print(f"[+] QR-код сохранен в: {OUT_IMG} ({total_width}x{height})")

    # Декодирование QR-кода через OpenCV
    print("[*] Сканируем QR-код...")
    cv_img = cv2.imread(OUT_IMG)
    detector = cv2.QRCodeDetector()
    val, pts, qr = detector.detectAndDecode(cv_img)

    if not val:
        # Резервный порог для бинаризации
        gray = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)
        val, pts, qr = detector.detectAndDecode(thresh)

    print(f"[+] Декодированная ссылка: {val}")

    # Известные метаданные трека:
    # URL: https://www.youtube.com/watch?v=3zh9Wb1KuW8
    # Трек: Shinunoga E-Wa
    # Исполнитель: Fujii Kaze (藤井 風)
    # Страна: Japan (Япония)
    artist = "Fujii Kaze"
    track = "Shinunoga E-Wa"
    country = "japan"

    print("\n[+] Итоги Задачи №2:")
    print(f"    Артист:                 {artist}")
    print(f"    Трек:                   {track}")
    print(f"    Страна артиста:         {country} (Japan)")
    print(f"    Часть флага:            Flag_{{1c3aa737eac3.png_{country}_}}")

if __name__ == "__main__":
    solve()
