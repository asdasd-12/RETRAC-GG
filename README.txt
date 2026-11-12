RETRAC.GG — локальный запуск и публикация

ЛОКАЛЬНЫЙ ЗАПУСК (Windows)
1. Установи Python 3.10+ с https://www.python.org/downloads/ (галочка Add Python to PATH).
2. Открой эту папку в терминале.
3. Выполни: python -m venv .venv
4. Выполни: .venv\Scripts\activate
5. Выполни: python -m pip install -r requirements.txt
6. Выполни: python app.py
7. Открой http://127.0.0.1:5000

ПУБЛИКАЦИЯ НА RENDER
1. Создай новый публичный или приватный репозиторий GitHub.
2. Загрузи СОДЕРЖИМОЕ этой папки в корень репозитория (app.py, requirements.txt, render.yaml, папки static/templates и shop_items.json). Не загружай .venv.
3. В Render выбери New + -> Blueprint и подключи этот GitHub-репозиторий.
4. Render обнаружит render.yaml. Проверь настройки и нажми Apply.
5. После успешного Deploy открой адрес *.onrender.com в панели Render.

СТРАНИЦЫ
/      — главная
/shop  — каталог предметов Retrac

Каталог читает проверенные вручную записи из shop_items.json. Реальный магазин Retrac пока не подключён: не добавляй выдуманные предметы или цены. Для публикации не нужны пароли от Epic или Discord.
