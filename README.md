# Telegram News Bot / Telegram Новостной Бот

[English](#english) | [Русский](#русский)

---

## English

Telegram bot for getting news from various sources with integrated AI chatbot.

### Features

- **News**: Get news from different categories and sources
  - World news (Lenta.ru, BBC News)
  - Kazakhstan news (Tengri News, Sputnik KZ)
  - Space news (Tengri Space, Rambler)
  - Science news (Playground, New-science)
- **AI Chatbot**: Intelligent responses to user questions
- **Auto-publishing**: Send news to channel

### Installation

1. Clone the repository
2. Create virtual environment:
```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Replace bot token in `Бот.py` file on line 11:
```python
bot = telebot.TeleBot('YOUR_BOT_TOKEN', skip_pending=True)
```

### Usage

```bash
python Бот.py
```

### Project Structure

- `Бот.py` - Main bot file
- `test.py - test8.py` - News parsing modules
- `data/*.json` - News data files
- `текст/` - Additional files and documentation

### Bot Commands

- `/start` - Start bot and main menu
- **News** - Select news category
- **Chat-Bot** - Activate AI assistant
- **Help** - Bot information

---

## Русский

Telegram бот для получения новостей из различных источников с интегрированным AI чат-ботом.

### Функции

- **Новости**: Получение новостей из разных категорий и источников
  - Мировые новости (Lenta.ru, BBC News)
  - Новости Казахстана (Tengri News, Sputnik KZ)
  - Космические новости (Tengri Space, Rambler)
  - Новости науки (Playground, New-science)
- **AI Чат-бот**: Интеллектуальные ответы на вопросы пользователей
- **Автоматическая публикация**: Отправка новостей в канал

### Установка

1. Клонируйте репозиторий
2. Создайте виртуальное окружение:
```bash
python -m venv venv
venv\Scripts\activate
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

4. Замените токен бота в файле `Бот.py` на строке 11:
```python
bot = telebot.TeleBot('ВАШ_ТОКЕН_БОТА', skip_pending=True)
```

### Запуск

```bash
python Бот.py
```

### Структура проекта

- `Бот.py` - Основной файл бота
- `test.py - test8.py` - Модули парсинга новостей
- `data/*.json` - Файлы с данными новостей
- `текст/` - Дополнительные файлы и документация

### Команды бота

- `/start` - Запуск бота и главное меню
- **Новости** - Выбор категории новостей
- **Чат-Бот** - Активация AI помощника
- **Помощь** - Информация о боте