# Лабораторная работа 2

Артунян Карина, 3-ИТМБ Вариант: октябрь 01-10 Тема: Платформа для изучения языков Сущности: Пользователи, языки, уроки, упражнения, прогресс, словари

### Описание проекта
Проект реализует Airflow DAG `language_learning_platform_dag.py` для обработки данных учебной платформы изучения языков. В DAG выделены этапы извлечения пользователей, языков, уроков, упражнений, преобразования прогресса и загрузки словарей.

### Что было сделано
1. Подготовила рабочую среду в WSL2:
   - активировала WSL2 через установку в Windows функции «Подсистема Windows для Linux»;
   - установила дистрибутив Ubuntu из Microsoft Store;
   - в Ubuntu установила Python (`sudo apt update && sudo apt install python3 python3-pip`).
2. Открыла проект в Linux-системе через VS Code.
3. Установила зависимости Airflow и подготовил окружение Python.
4. Написала DAG в `language_learning_platform_dag.py`:
   - задачи `extract_users`, `extract_languages`, `extract_lessons`, `extract_exercises`;
   - задачу `transform_progress`, которая связывает пользователей и уроки;
   - задачу `load_dictionaries`, создающую словари по языкам.
5. Запустила Airflow UI и добавила DAG в список.
6. В UI Airflow запустила DAG вручную и проверила успешное выполнение всех задач.

### Результат
- DAG выполнен без ошибок.
- В разделе Logs Airflow проверил, что все таблицы извлечения и загрузки отработали.
- В интерфейсе видно зависимость задач: users → languages → lessons → exercises → progress → dictionaries.

### Примечание
Файл `language_learning_platform_dag.py` находится в корневой папке проекта. 

### Скриншоты
<img width="1280" height="720" alt="LAB2_01" src="https://github.com/user-attachments/assets/114aec6c-915e-49d1-a89b-67b9201bebb8" />
<img width="1280" height="709" alt="LAB2_02" src="https://github.com/user-attachments/assets/d70f377f-86df-4c83-84dd-4d72f8dd9e58" />


