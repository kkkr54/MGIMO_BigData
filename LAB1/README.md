# Лабораторная работа 1

Артунян Карина, 3-ИТМБ
Вариант: октябрь 01-10
Тема: Платформа для изучения языков
Сущности: Пользователи, языки, уроки, упражнения, прогресс, словари


# 1. Установка Apache Kafka

С официального сайта скачана бинарная версия дистрибутива Apache Kafka 2.7.1 с поддержкой zookeper. Дистрибутив распакован в корневую папку (при извлечении в папки с длинным путем возникала ошибка "Слишком длинная входная строка"). 
Далее последовательно введены команды:

Запуск zookeper
> .\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties

Далее в новом окне запуск брокера
> .\bin\windows\kafka-server-start.bat .\config\server.properties

Создание тестового топика
> .\bin\windows\kafka-topics.bat --create --topic test-topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1

Далее тестировался Producer:
> .\bin\windows\kafka-console-producer.bat --topic test-topic --bootstrap-server localhost:9092

И Consumer:
> .\bin\windows\kafka-console-consumer.bat --topic test-topic --bootstrap-server localhost:9092 --from-beginning

## 2. Написание скриптов

Скрипты написаны в среде VS Code. Предварительно установлена библиотека
> pip install kafka-python faker

Создан отдельный модуль message_generator.py для генерации сообщений и написаны скрипты producer.py и consumer.py. 

Для валидации используется только один критерий:
> 0  <=  data["progress_percent"] <=  100

Т.е. если сущность "Прогресс" (в процентах) находится в диапазоне от 0 до 100. Этот и остальные атрибуты сообщения генерируются рандомно из массива значений в модуле message_generator.py 


## 3. Запуск

В двух отдельных терминалах средствами VS Code запускаются скрипты Consumer и Producer соответственно. Для примера генерируется три рандомных сообщения. Пример вывода представен ниже
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/908979a2-5485-4ec4-9ecf-f32669c8f840" />
