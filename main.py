from datetime import datetime, timezone

import pytz
from fastapi import FastAPI, HTTPException, Query
from pytz.exceptions import AmbiguousTimeError, NonExistentTimeError
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


@app.get("/time/convert")
def convert_time(
    time: str = Query(..., examples=["2026-06-15T14:30:00"]),
    from_timezone: str = Query(..., examples=["Europe/Moscow"]),
    to_timezone: str = Query(..., examples=["America/New_York"]),
):
    try:
        from_tz = pytz.timezone(from_timezone)
        to_tz = pytz.timezone(to_timezone)
    except pytz.UnknownTimeZoneError:
        raise HTTPException(status_code=400, detail="Unknown timezone")

    try:
        dt = datetime.fromisoformat(time.replace("Z", "+00:00"))
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid time format. Use ISO format, e.g. 2026-06-15T14:30:00")

    if dt.tzinfo is not None:
        dt = dt.replace(tzinfo=None)

    try:
        localized = from_tz.localize(dt)
    except (AmbiguousTimeError, NonExistentTimeError) as exc:
        raise HTTPException(status_code=400, detail=str(exc))

    converted = localized.astimezone(to_tz)

    return {
        "original_time": localized.isoformat(),
        "from_timezone": from_timezone,
        "converted_time": converted.isoformat(),
        "to_timezone": to_timezone,
    }
