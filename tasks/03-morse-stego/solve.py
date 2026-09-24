#!/usr/bin/env python3
"""
INFO SEC LABS CTF - Task 3 Solver
Извлечение стеганографического WAV-файла из PNG-изображения,
автоматическое декодирование аудиосигнала Морзе и ответ на загадку Base32.
"""

import os
import sys
import wave
import base64
import numpy as np

BASE_DIR = os.path.dirname(__file__)
IMG_PATH = os.path.join(BASE_DIR, "task_image.jpg")
WAV_PATH = os.path.join(BASE_DIR, "morse.wav")
MARKER = b"---CTF_MORSE_SPLIT_MARKER---"

MORSE_CODE_DICT = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
    '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3',
    '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8',
    '----.': '9', '.-.-.-': '.', '--..--': ',', '..--..': '?', '-.-.--': '!',
    '-....-': '-', '-..-.': '/', '.--.-.': '@', '---...': ':', '-...-': '='
}

def extract_wav():
    if not os.path.exists(IMG_PATH):
        print(f"[-] Файл {IMG_PATH} не найден!")
        sys.exit(1)

    with open(IMG_PATH, 'rb') as f:
        data = f.read()

    pos = data.find(MARKER)
    if pos == -1:
        print("[-] Маркер разделителя не найден в файле изображения!")
        sys.exit(1)

    wav_bytes = data[pos + len(MARKER):]
    with open(WAV_PATH, 'wb') as f:
        f.write(wav_bytes)
    print(f"[+] Извлечен аудиофайл: {WAV_PATH} ({len(wav_bytes)} байт)")

def decode_morse():
    print("[*] Анализируем огибающую аудиосигнала...")
    with wave.open(WAV_PATH, 'rb') as w:
        frames = w.readframes(w.getnframes())
        samples = np.frombuffer(frames, dtype=np.uint8).astype(np.float32) - 128

    # Считаем среднюю амплитуду окнами по 10мс (80 сэмплов при 8000 Гц)
    chunk_size = 80
    envelope = np.array([np.mean(np.abs(samples[i:i+chunk_size])) for i in range(0, len(samples), chunk_size)])

    thresh = 30
    binary = (envelope > thresh).astype(int)

    # Run-length кодирование
    rle = []
    curr = binary[0]
    count = 0
    for b in binary:
        if b == curr:
            count += 1
        else:
            rle.append((curr, count))
            curr = b
            count = 1
    rle.append((curr, count))

    # Сборка символов: точка ~60мс (6 чанков), тире ~180мс (18 чанков)
    current_char = ''
    words = []
    current_word = []

    for state, dur in rle:
        if state == 1:  # Тон
            if dur < 11:
                current_char += '.'
            else:
                current_char += '-'
        else:  # Пауза
            if dur >= 30:  # Пробел между словами
                if current_char:
                    current_word.append(MORSE_CODE_DICT.get(current_char, f'[{current_char}]'))
                    current_char = ''
                if current_word:
                    words.append(''.join(current_word))
                    current_word = []
            elif dur >= 11:  # Пауза между буквами
                if current_char:
                    current_word.append(MORSE_CODE_DICT.get(current_char, f'[{current_char}]'))
                    current_char = ''

    if current_char:
        current_word.append(MORSE_CODE_DICT.get(current_char, f'[{current_char}]'))
    if current_word:
        words.append(''.join(current_word))

    morse_result = ''.join(words)
    print(f"[+] Распознанная строка Морзе: {morse_result}")

    # Декодируем Base32
    print("[*] Декодируем Base32...")
    decoded_question = base64.b32decode(morse_result).decode('utf-8', errors='ignore')
    print(f"[+] Вопрос / загадка: \"{decoded_question}\"")

    # Ответ на вопрос: Ryuk из Death Note одержим яблоками (apple)
    answer = "apple"
    final_flag = f"Flag_{{1c3aa737eac3.png_japan_{answer}_}}"

    print("\n[+] Итоги Задачи №3:")
    print(f"    Ответ на вопрос:        {answer}")
    print(f"    Итоговый флаг CTF:      {final_flag}")
    print(f"    (Этот флаг открывает TSARKA COURSE.rar)")

def solve():
    if not os.path.exists(WAV_PATH):
        extract_wav()
    decode_morse()

if __name__ == "__main__":
    solve()
