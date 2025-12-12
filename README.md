# Инструкция
1. Открываем задачу
2. Открываем панель разработчика
3. Переходим во вкладку "Network", добавляем фильтр Fetch/XHR
4. В задаче в разделе Activity переключаемся на "Comments", а потом обратно на "Work Log"
5. Создаем в директории resources файлы
    - input.html (сюда будем копировать текст для парсинга)
    - dev-set.json (сюда запишем список пользователей команды разработки) в формате ["user1", "user2"]
6. Копируем "Response" последнего запроса (browse/`<TASK-ID>`?page=com.atlassian.jira.plugin.system.issuetabpanels:worklog-tabpanel&_=`<PANEL-ID>`) в reosurces/input.html
7. Устанавливаем зависимости
    - Устанавливаем poetry глобально, если его нет: `pip install poetry`
    - Создаем окружение: `poetry install`
    - Запускаем окружение: `poetry shell`
8. Запускаем парсер: `python parser.py`