# Time API

Простой тестовый бэкенд на FastAPI, который возвращает текущее время и дату сервера.

## Требования

- Python 3.12+
- Docker (опционально)

## Локальный запуск

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Сервер будет доступен по адресу: http://127.0.0.1:8000

## API

| Метод | Путь          | Описание                         |
|-------|---------------|----------------------------------|
| GET   | `/`           | Информация об API                |
| GET   | `/time`       | Текущее время сервера (UTC)      |
| GET   | `/date`       | Текущая дата сервера (UTC)       |
| GET   | `/date/local` | Текущая дата в локальном часовом поясе |
| GET   | `/docs`       | Swagger UI                       |

### Пример ответа `/time`

```json
{
  "utc": "2026-06-15T08:12:18.983990+00:00",
  "timestamp": 1781511138.98399
}
```

### Пример ответа `/date`

```json
{
  "utc": "2026-06-15",
  "year": 2026,
  "month": 6,
  "day": 15,
  "weekday": "Monday"
}
```

### Пример ответа `/date/local`

```json
{
  "date": "2026-06-15",
  "timezone": "MSK",
  "year": 2026,
  "month": 6,
  "day": 15,
  "weekday": "Monday"
}
```

## Docker

Сборка образа:

```bash
docker build -t time-api .
```

Запуск контейнера:

```bash
docker run -p 8000:8000 time-api
```

API будет доступен по адресу: http://localhost:8000

## Структура проекта

```
.
├── main.py           # Приложение FastAPI
├── requirements.txt  # Зависимости Python
├── Dockerfile        # Сборка Docker-образа
└── README.md
```
