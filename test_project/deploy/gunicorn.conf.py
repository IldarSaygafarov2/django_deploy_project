import multiprocessing  # Модуль стандартной библиотеки Python для работы с количеством ядер процессора.

# Адрес, на котором Gunicorn будет принимать соединения.
# В данном случае используется Unix Socket.
# Nginx будет отправлять запросы именно в этот сокет.
# Для TCP можно использовать:
# bind = "0.0.0.0:8000"
bind = "unix:/run/gunicorn/gunicorn.sock"

# Количество рабочих процессов (workers).
# Каждый worker — отдельный процесс Python.
#
# Рекомендуемая формула:
# (Количество ядер CPU × 2) + 1
#
# Например:
# 2 ядра  -> 5 workers
# 4 ядра  -> 9 workers
# 8 ядер  -> 17 workers
workers = multiprocessing.cpu_count() * 2 + 1

# Количество потоков внутри каждого worker.
# Используется только с worker_class="gthread".
# Если workers = 5 и threads = 2,
# одновременно смогут выполняться до 10 запросов.
threads = 2

# Тип worker'ов.
# sync     - один запрос на процесс (по умолчанию)
# gthread  - несколько потоков внутри процесса
# gevent   - асинхронные greenlet
# eventlet - аналог gevent
# Для Django обычно рекомендуют gthread.
worker_class = "gthread"

# Максимальное время выполнения одного запроса (в секундах).
# Если запрос выполняется дольше,
# Gunicorn завершит процесс и создаст новый.
# Полезно для защиты от "зависших" запросов.
timeout = 60

# Сколько секунд ждать,
# пока worker корректно завершится после получения SIGTERM.
# После истечения времени процесс будет убит принудительно.
graceful_timeout = 30

# Сколько секунд держать HTTP-соединение открытым
# после обработки запроса.
# Позволяет браузеру использовать Keep-Alive.
keepalive = 5

# После обработки указанного количества запросов
# worker будет автоматически перезапущен.
# Это помогает бороться с утечками памяти.
max_requests = 1000

# Добавляет случайное число к max_requests.
# Например:
# max_requests = 1000
# max_requests_jitter = 100
# Тогда worker завершится после обработки
# случайного количества запросов от 1000 до 1100.
# Благодаря этому все workers
# не перезапустятся одновременно.
max_requests_jitter = 100

# Лог успешных HTTP-запросов.
# "-" означает вывод в stdout.
# При использовании systemd или Docker
# логи автоматически попадут в journalctl
# или docker logs.
accesslog = "-"

# Лог ошибок.
# "-" означает stderr.
errorlog = "-"

# Уровень логирования.
# Возможные значения:
# debug
# info
# warning
# error
# critical
# Для production обычно используют info.
loglevel = "info"

# Перехватывает print() и traceback
# из приложения Django и отправляет их
# в журнал Gunicorn.
capture_output = True

# Имя процесса Gunicorn.
# Удобно при просмотре процессов:
# ps aux
# htop
# Вместо gunicorn будет отображаться
# django-project.
proc_name = "django-project"

# Путь до WSGI-приложения Django.
# Формат:
# <папка_проекта>.wsgi:application
# Например:
# core.wsgi:application
# config.wsgi:application
# backend.wsgi:application
# Именно через этот объект Gunicorn
# начинает выполнение Django-приложения.
wsgi_app = "test_project.wsgi:application"