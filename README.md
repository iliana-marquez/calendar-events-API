# calendar-events-API

Simple API to fetch Google Calendar events for HR tools, reports, or any system that needs calendar data.

## Endpoint

`GET /api/events`

### Headers
| Header  | Required | Description |
|---------|----------|-------------|
| api-key | Yes      | Authentication key |

### Parameters
| Parameter    | Format     | Example      |
|--------------|------------|--------------|
| calendar_id  | string     | xxx@group.calendar.google.com |
| start_date   | YYYY-MM-DD | 2025-01-01   |
| end_date     | YYYY-MM-DD | 2025-01-31   |

### Response
```json
{
  "events": [
    {
      "id": "google_event_id",
      "title": "Event Title",
      "start": "2025-01-08T09:00:00+01:00",
      "end": "2025-01-08T17:30:00+01:00"
    }
  ]
}
```

### Error Responses
| Status | Message |
|--------|---------|
| 401    | Invalid API key |
| 400    | Invalid request |


## Deployment

Live API: https://calendar-events-api-d5096b589023.herokuapp.com/docs

Hosted on Heroku with:
- Python 3.12
- FastAPI + Uvicorn

## Security

- API key authentication required (Header: `api-key`)


## Environment Variables

| Variable | Description |
|----------|-------------|
| `API_KEY` | Authentication key for API access |
| `CREDS` | Google Service Account credentials (JSON) |


---

Built by [Iliana Márquez](https://github.com/iliana-marquez)

Want to use, scale, or customise it? Feel free to contribute or contact me for a custom solution.