# Open-Source Pentesting & AppSec Syllabus
### Полный открытый эквивалент программы курса ЦАРКА (TSARKA)

В архиве `TSARKA COURSE.rar` находится коммерческий курс по практическому пентесту из 14 лекций. Ниже собрана его полноценная, открытая и актуальная альтернатива на базе репозиториев GitHub и бесплатных полигонов.

---

## 🗺 Карта модулей и репозиториев

```
                          ┌────────────────────────────────┐
                          │   Practical Ethical Hacking    │
                          │        (TCM Resources)         │
                          └───────────────┬────────────────┘
                                          │
       ┌──────────────────┬───────────────┴───────────────┬──────────────────┐
       │                  │                               │                  │
┌──────▼───────┐   ┌──────▼───────┐               ┌───────▼──────┐    ┌──────▼───────┐
│     OSINT    │   │  Web AppSec  │               │    Wi-Fi     │    │   PrivEsc    │
│   & Recon    │   │  (WSTG, PAtT)│               │  Challenge   │    │(PEASS, Linux/│
│              │   │              │               │  (Docker)    │    │ Windows OS)  │
└──────────────┘   └──────────────┘               └──────────────┘    └──────────────┘
```

---

## 1. Фундамент и методология пентеста

В курсе ЦАРКА это вводная лекция (`Lesson-1.pdf`) и разведка (`Lesson 2.pdf`).

* **[TCM-Course-Resources/Practical-Ethical-Hacking-Resources](https://github.com/TCM-Course-Resources/Practical-Ethical-Hacking-Resources)** (⭐ 6.1k)  
  Конспекты и практический трек легендарного курса PEH от Heath Adams (The Cyber Mentor). Дает цельное понимание процесса: от настройки сетевых адаптеров в Kali до составления финального отчёта заказчику.
* **[hmaverickadams/Beginner-Network-Pentesting](https://github.com/hmaverickadams/Beginner-Network-Pentesting)** (⭐ 6.4k)  
  Пошаговые конспекты по сканированию сетей, работе с nmap, поиску векторов первичного проникновения.
* **[OWASP/wstg (Web Security Testing Guide)](https://github.com/OWASP/wstg)** (⭐ 9.9k)  
  Золотой стандарт аудита веб-приложений. Каждая уязвимость описана по схеме: теория -> методы поиска -> чек-лист -> способы устранения.

---

## 2. Безопасность веб-приложений (Web Pentesting)

В курсе ЦАРКА: Уроки 4–8 (SQLi, XSS, CSRF, SSRF, LFI/RFI, RCE, File Upload). В домашних заданиях используются стенды PortSwigger Web Security Academy.

* **[swisskyrepo/PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings)** (⭐ 81k)  
  Крупнейшая база пейлоадов, техник обхода фильтраций (WAF bypass), реверс-шеллов и векторов атак. Обязательна к добавлению в закладки любого этичного хакера.
* **[botesjuan/Burp-Suite-Certified-Practitioner-Exam-Study-Guide](https://github.com/botesjuan/Burp-Suite-Certified-Practitioner-Exam-Study-Guide)** (⭐ 1.4k)  
  Полное руководство по прохождению всех тем и уровней сложности (Apprentice, Practitioner, Mystery Labs) на бесплатной платформе PortSwigger Web Security Academy.
* **[OWASP/juice-shop](https://github.com/juice-shop/juice-shop)** (⭐ 11.5k)  
  Полностью уязвимое современное веб-приложение (Node.js/Angular/Express), которое разворачивается в одну команду через Docker:
  ```bash
  docker run --rm -p 3000:3000 bkimminich/juice-shop
  ```
  Идеально для безопасной отработки XSS, SQLi, Broken Auth и NoSQL-инъекций.

---

## 3. Аудит беспроводных сетей (Wi-Fi Pentest)

В курсе ЦАРКА: Уроки 11–14 (WEP, WPA/WPA2, Handshake, PMKID, Enterprise-сети).

* **[r4ulcl/WiFiChallengeLab-docker](https://github.com/r4ulcl/WiFiChallengeLab-docker)** (⭐ 430+)  
  🔥 **Официальная Docker-версия полигона `wifichallengelab.com`, заданного в уроках ЦАРКА.**  
  Ключевое преимущество: лаборатория использует виртуальный драйвер ядра Linux `mac80211_hwsim`. Вам **не нужен физический USB Wi-Fi свисток** с поддержкой monitor mode. Виртуальные клиенты и точки доступа поднимаются прямо в контейнерах.
  ```bash
  git clone https://github.com/r4ulcl/WiFiChallengeLab-docker.git
  cd WiFiChallengeLab-docker
  sudo ./start.sh
  ```
* **[aircrack-ng/aircrack-ng](https://github.com/aircrack-ng/aircrack-ng)**  
  Репозиторий основного стека утилит (`airmon-ng`, `airodump-ng`, `aireplay-ng`, `aircrack-ng`).

---

## 4. Постэксплуатация и повышение привилегий (Privilege Escalation)

В курсе ЦАРКА: Уроки 15–18 (Linux: SUID, sudo, Cron wildcards, PATH; Windows: Unquoted Service Paths, Weak Registry, AlwaysInstallElevated).

* **[peass-ng/PEASS-ng](https://github.com/peass-ng/PEASS-ng)** (⭐ 14.5k)  
  Главный инструмент автоматизации разведки внутри захваченной системы (`linPEAS` под Linux и `winPEAS` под Windows). Находит ровно те же векторы, о которых рассказывается в презентациях курса.
* **[HackTricks-wiki/hacktricks](https://github.com/HackTricks-wiki/hacktricks)** (⭐ 12.4k)  
  Подробнейшие мануалы по ручной эскалации привилегий для обеих ОС:
  - [Linux Privilege Escalation Cheatsheet](https://book.hacktricks.xyz/linux-hardening/privilege-escalation)
  - [Windows Privilege Escalation Cheatsheet](https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation)
* **[mzet-/linux-exploit-suggester](https://github.com/mzet-/linux-exploit-suggester)**  
  Скрипт для сопоставления версии ядра Linux с известными эксплойтами (Dirty COW, PwnKit и др.).

---

## 5. Лабораторные комнаты для закрепления

| Тема | Рекомендуемая комната | Платформа |
|---|---|---|
| Linux PrivEsc (Cron, SUID) | [UltraTech 1](https://tryhackme.com/room/ultratech1) | TryHackMe |
| Linux PrivEsc (Практика) | [Linux PrivEsc Arena](https://tryhackme.com/room/linuxprivesc) | TryHackMe |
| Windows PrivEsc (Службы, реестр) | [Windows PrivEsc Arena](https://tryhackme.com/room/windowsprivesc20) | TryHackMe |
| Веб-уязвимости | [Web Security Academy](https://portswigger.net/web-security) | Бесплатно от PortSwigger |
| Wi-Fi атаки | [WiFiChallengeLab](https://github.com/r4ulcl/WiFiChallengeLab-docker) | Локально в Docker |
