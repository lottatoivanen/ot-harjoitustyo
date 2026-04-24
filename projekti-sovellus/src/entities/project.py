import uuid
import json
from datetime import datetime

class Project:
    """Luokka projektia varten, jolla on nimi, kuvaus ja uniikki id."""
    def __init__(self, name, description, user, project_id=None, dates=None):
        self.name = name
        self.description = description
        self.user = user
        self.id = project_id if project_id else str(uuid.uuid4())
        self.dates = dates or []

    def dates_to_json(self):
        serialized = []
        for entry in self.dates:
            if isinstance(entry, dict):
                date_value = entry.get("date")
                if not date_value:
                    continue
                serialized.append({
                    "type": entry.get("type", "Practice"),
                    "date": date_value.isoformat()
                })
            else:
                serialized.append({
                    "type": "Practice",
                    "date": entry.isoformat()
                })
        return json.dumps(serialized)

    @staticmethod
    def dates_from_json(json_str):
        if not json_str:
            return []
        raw = json.loads(json_str)
        parsed = []

        for item in raw:
            if isinstance(item, dict):
                parsed.append({
                    "type": item.get("type", "Practice"),
                    "date": datetime.fromisoformat(item.get("date"))
                })
            else:
                parsed.append({
                    "type": "Practice",
                    "date": datetime.fromisoformat(item)
                })
        return parsed
