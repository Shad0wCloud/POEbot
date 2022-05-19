# Инструкция к установке
### 1) Скачиваем Python, желательно 3.10
<ul>https://www.python.org/downloads/</ul>
<ul>обязательно добавляем python в PATH</ul>

### 2) скачиваем Tesseract
<ol>
<li>Скачиваем https://github.com/UB-Mannheim/tesseract/wiki.</li>
<li>Устанавливаем в <b>C:\Program Files\Tesseract-OCR</b></li>
<li>Выбираем русский язык во время установки в дополнительных пакетах языка</li>
</ol>

### 3) устанавливаем пакеты питона
<ul>Открываем Cmd/PowerShell и прописываем команды ниже</ul>

```
pip install Pillow
pip install aiogram
pip install pytesseract
```

### 4) Создаем бота в телеге
<ol>
<li>Заходим в телегу</li>
<li>В поиск вбиваем @BotFather</li>
<li>Пишем ему /newbot</li>
<li>Пишите ему иму и никнейм</li>
<li>Он выдаст токен бота</li>
<li>Вписать токен бота вместо <b>TOKEN</b></li>
</ol>

### 5) запускаем бота
<ul>открываем в папке cmd/powershell (shift + пкм по пустому месту в папке)</ul>
<ul>пишем python ./main.py</ul>
<ul>Переходим к своему боту в телеграм и пишем /trade</ul>

Каждый раз придется выполнять пункт 5, чтобы запустить бота
