from fastapi import FastAPI, HTTPException, Header
from fetch_events import fetch_events_by_period
from datetime import date
import os
if os.path.isfile('env.py'):
    import env


app = FastAPI()

API_KEY = os.environ.get("API_KEY")


@app.get("/")
def root():
    return {"status": "ok"}


@app.get("/api/events")
def get_events(
    calendar_id: str, 
    start_date: date, 
    end_date: date,
    api_key: str = Header(None)
):
    """
    Fetches events from a Google Calendar.

    Parameters:
    - calendar_id: Google Calendar ID
    - start_date: Start date (YYYY-MM-DD)
    - end_date: End date (YYYY-MM-DD)

    Returns:
    - events: List of {id, title, start, end}
    """
    if api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")

    try:
        result = fetch_events_by_period(
            calendar_id=calendar_id,
            start_date=start_date.isoformat(),
            end_date=end_date.isoformat(),
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
