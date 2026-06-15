from datetime import datetime, timezone

from fastapi import FastAPI

app = FastAPI(title="Time API", description="Простой тестовый бэкенд")


@app.get("/")
def root():
    return {"message": "Time API", "docs": "/docs"}


@app.get("/time")
def get_server_time():
    now = datetime.now(timezone.utc)
    return {
        "utc": now.isoformat(),
        "timestamp": now.timestamp(),
    }


@app.get("/date")
def get_server_date():
    today = datetime.now(timezone.utc).date()
    return {
        "utc": today.isoformat(),
        "year": today.year,
        "month": today.month,
        "day": today.day,
        "weekday": today.strftime("%A"),
    }


@app.get("/date/local")
def get_local_server_date():
    now = datetime.now().astimezone()
    today = now.date()
    return {
        "date": today.isoformat(),
        "timezone": now.tzname(),
        "year": today.year,
        "month": today.month,
        "day": today.day,
        "weekday": today.strftime("%A"),
    }
