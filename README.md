# Инструкция
1. Открываем задачу
2. Открываем панель разработчика
3. Переходим во вкладку "Network", добавляем фильтр Fetch/XHR
4. В задаче в разделе Activity переключаемся на "Comments", а потом обратно на "Work Log"
5. Создаем в директории resources файлы
    5.1. input.html (сюда будем копировать текст для парсинга)
    5.2. dev-set.json (сюда запишем список пользователей команды разработки) в формате ["user1", "user2"]
5. Копируем "Response" последнего запроса (browse/`<TASK-ID>`?page=com.atlassian.jira.plugin.system.issuetabpanels:worklog-tabpanel&_=`<PANEL-ID>`) в reosurces/input.html
6. Запускаем парсер: `python parser.py`