# INFO SEC LABS CTF: Full Writeups, Solvers & Open-Source Pentesting Course

Репозиторий с полным разбором трехэтапного CTF-квеста **INFO SEC LABS**, готовыми автоматическими скриптами-солверами, всеми исходными файлами тасок и **полноценным открытым курсом по пентесту**, заменяющим коммерческую программу ЦАРКА (TSARKA).

В корне репозитория также доступен интерактивный веб-портал: [`index.html`](index.html).

---

## 🏆 Цепочка флагов и прогресс прохождения

Все задачи логически связаны между собой: решение предыдущего этапа открывает доступ к следующему либо формирует кусочек итогового пароля.

```
┌─────────────────────────────────┐
│   Task 1: iitu_10000.zip        │ ──► Папка: 6741, Файл: 1c3aa737eac3.png
│   (10 000 зашумленных PNG)     │ ──► Флаг: Flag_{1c3aa737eac3.png_}
└────────────────┬────────────────┘
                 │ Пароль: 6741^3 = 306318327021
                 ▼
┌─────────────────────────────────┐
│   Task 2: Task2.rar             │ ──► Радужный QR (ROYGBIV) -> Fujii Kaze (Japan)
│   (7 полос цветного QR-кода)    │ ──► Флаг: Flag_{1c3aa737eac3.png_japan_}
└────────────────┬────────────────┘
                 │ Контекст страны
                 ▼
┌─────────────────────────────────┐
│   Task 3: task_image.jpg        │ ──► Аудио Морзе в хвосте PNG -> Base32 загадка Рюка -> apple
│   (Стеганография + Морзе)       │ ──► Итоговый флаг: Flag_{1c3aa737eac3.png_japan_apple_}
└────────────────┬────────────────┘
                 │ Пароль от архива курса
                 ▼
┌─────────────────────────────────┐
│   TSARKA COURSE.rar (33 МБ)     │ ──► Лежит в course/TSARKA COURSE.rar
│   (Оригинальный защищенный архив)│ ──► Пароль: Flag_{1c3aa737eac3.png_japan_apple_}
└─────────────────────────────────┘
```

---

## 📂 Структура задач и Writeups

Каждая задача вынесена в отдельную директорию со своим исходным файлом, готовым скриптом решения и подробнейшим разбором хода мыслей:

| № | Папка | Категория | Что делаем | Writeup & Код |
|---|---|---|---|---|
| **01** | [`tasks/01-iitu-10000/`](tasks/01-iitu-10000/) | Forensic / Stego | Поиск логотипа IITU среди 10 000 файлов по аномалии сжатия zlib | [📖 Читать Writeup](tasks/01-iitu-10000/README.md) · [`solve.py`](tasks/01-iitu-10000/solve.py) |
| **02** | [`tasks/02-rainbow-qr/`](tasks/02-rainbow-qr/) | Crypto / OSINT | Склейка 7 полосок QR по цветам радуги, сканирование и OSINT артиста | [📖 Читать Writeup](tasks/02-rainbow-qr/README.md) · [`solve.py`](tasks/02-rainbow-qr/solve.py) |
| **03** | [`tasks/03-morse-stego/`](tasks/03-morse-stego/) | Stego / Audio / Crypto | Извлечение WAV из-под `IEND`, декодирование Морзе и Base32 | [📖 Читать Writeup](tasks/03-morse-stego/README.md) · [`solve.py`](tasks/03-morse-stego/solve.py) |

---

## ⚡ Быстрый старт: запуск решений

Для запуска солверов нужен Python 3 и несколько базовых пакетов:

```bash
# 1. Клонируем репозиторий
git clone https://github.com/ValentinStars/INFO-SEC-LABS-CTF.git
cd INFO-SEC-LABS-CTF

# 2. Ставим зависимости
pip install pillow opencv-python numpy
sudo apt install -y p7zip-full

# 3. Запуск любого солвера в один клик:
python3 tasks/01-iitu-10000/solve.py
python3 tasks/02-rainbow-qr/solve.py
python3 tasks/03-morse-stego/solve.py
```

---

## 🎓 Открытый курс по практическому пентесту

Вместе с распаковкой лекций курса ЦАРКА сформирована открытая дорожная карта на базе лучших Open-Source проектов:

- **[course/TSARKA COURSE.rar](course/TSARKA%20COURSE.rar)** — Оригинальный архив с 14 лекциями ЦАРКА (распаковка: `7z x -p'Flag_{1c3aa737eac3.png_japan_apple_}' "course/TSARKA COURSE.rar"`).
- **[course/README.md](course/README.md)** — Текстовый справочник и карта открытого курса.
- **[index.html](index.html)** — Интерактивный веб-дашборд с фильтрами по темам, командами запуска полигонов в Docker и ссылками на репозитории:
  - **Recon & OSINT**: TCM Practical Ethical Hacking, OWASP WSTG.
  - **Web Security**: PayloadsAllTheThings, PortSwigger Burp Study Guide, OWASP Juice Shop.
  - **Wireless Wi-Fi Pentest**: `r4ulcl/WiFiChallengeLab-docker` (виртуализированная лаба без физических Wi-Fi карточек через `mac80211_hwsim`), Aircrack-ng.
  - **Privilege Escalation**: PEASS-ng (linPEAS / winPEAS), HackTricks, Linux Exploit Suggester.

---

## Лицензия

Материалы и скрипты решения распространяются в образовательных целях под лицензией MIT.
