from datetime import datetime

SUPPORTED_DATE_FORMATS = (
    "%d.%m.%Y %H:%M",
    "%d.%m.%Y",
    "%Y-%m-%d %H:%M",
    "%Y-%m-%d",
)

def date_service(date_str):
    value = date_str.strip()
    if not value:
        return None

    for fmt in SUPPORTED_DATE_FORMATS:
        try:
            return datetime.strptime(value, fmt)
        except ValueError:
            continue
    return None
