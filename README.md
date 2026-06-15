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
| GET   | `/time/convert` | Конвертация времени между часовыми поясами |
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

### Пример запроса `/time/convert`

```
GET /time/convert?time=2026-06-15T14:30:00&from_timezone=Europe/Moscow&to_timezone=America/New_York
```

### Пример ответа `/time/convert`

```json
{
  "original_time": "2026-06-15T14:30:00+03:00",
  "from_timezone": "Europe/Moscow",
  "converted_time": "2026-06-15T07:30:00-04:00",
  "to_timezone": "America/New_York"
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

## CI/CD (GitHub Actions)

Workflow `.github/workflows/deploy.yml`:

1. **build** — multi-platform сборка (`amd64` + `arm64`), push в GHCR, кэш GitHub Actions.
2. **deploy** — SSH на сервер, pull образа и запуск контейнера.

Подробнее: [DEPLOYMENT.md](DEPLOYMENT.md)

### Триггеры

- Push в `main` / `master` — сборка + деплой
- Pull Request в `main` / `master` — только сборка

### Секреты репозитория

| Секрет | Описание |
|--------|----------|
| `HOST` | IP или домен сервера |
| `USERNAME` | Пользователь SSH |
| `SSH_KEY` | Приватный SSH-ключ |
| `PORT` | Порт SSH (обычно `22`) |

## Структура проекта

```
.
├── .github/
│   └── workflows/
│       └── deploy.yml  # CI/CD: сборка образа и деплой
├── DEPLOYMENT.md     # Инструкция по деплою
├── main.py           # Приложение FastAPI
├── requirements.txt  # Зависимости Python
├── Dockerfile        # Сборка Docker-образа
└── README.md
```
