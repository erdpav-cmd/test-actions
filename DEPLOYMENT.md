# Деплой

Инструкция по настройке CI/CD через GitHub Actions.

## Секреты репозитория

Добавьте в **Settings → Secrets and variables → Actions**:

| Секрет | Описание |
|--------|----------|
| `HOST` | IP-адрес или домен сервера |
| `USERNAME` | Имя пользователя SSH |
| `SSH_KEY` | Приватный SSH-ключ |
| `PORT` | Порт SSH (по умолчанию `22`) |

`GITHUB_TOKEN` создаётся автоматически и используется для push/pull образа в GHCR.

## Workflow

Файл `.github/workflows/deploy.yml` выполняет два шага:

1. **build** — сборка multi-platform образа (`linux/amd64`, `linux/arm64`), push в `ghcr.io`, кэширование через GitHub Actions Cache.
2. **deploy** — SSH-подключение к серверу, pull образа из GHCR, перезапуск контейнера `time-api`.

## Триггеры

- Push в ветки `main` или `master` — сборка и деплой.
- Pull Request в `main` или `master` — только сборка образа (без деплоя).

## Требования к серверу

- Установлен Docker
- Открыт порт `8000` (или измените маппинг в workflow)
- SSH-доступ по ключу из секрета `SSH_KEY`

## Проверка после деплоя

```bash
curl http://<HOST>:8000/time
```

Образ в реестре: `ghcr.io/<owner>/<repo>:latest`
