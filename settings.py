# general settings
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
}

_MAKESJSON = "makes.json"

# database settings
DB_NAME = "db.sqlite3"
CAR_TABLE_DATA = [
    ("url", "TEXT"),
    ("title", "TEXT"),
    ("price", "REAL"),
    ("registration", "REAL"),
    ("mileage", "REAL"),
    ("type", "TEXT"),
    ("fuel", "TEXT"),
    ("transmission", "TEXT"),
    ("color", "TEXT"),
    ("options", "TEXT"),
    ("score", "REAL"),
]
