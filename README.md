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

## Developer

Built by [Iliana Márquez](https://github.com/iliana-marquez)

Want to use, scale, or customise it? Feel free to contribute or contact me for a custom solution.