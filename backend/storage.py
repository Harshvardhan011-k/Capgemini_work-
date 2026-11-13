import json
import uuid
from datetime import datetime
from config import USERS_FILE, REPORTS_FILE


def _read(path):
    with open(path, "r") as f:
        return json.load(f)


def _write(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=2, default=str)


# ---------- Users ----------
def get_user(username: str, password: str):
    data = _read(USERS_FILE)
    for u in data["users"]:
        if u["username"] == username and u["password"] == password:
            return u
    return None


# ---------- Reports ----------
def save_report(report: dict) -> str:
    data = _read(REPORTS_FILE)
    report["id"] = str(uuid.uuid4())
    report["created_at"] = datetime.utcnow().isoformat()
    data["reports"].append(report)
    _write(REPORTS_FILE, data)
    return report["id"]


def get_reports(user_id: str = None):
    data = _read(REPORTS_FILE)
    reports = data["reports"]
    if user_id:
        reports = [r for r in reports if r.get("user_id") == user_id]
    return sorted(reports, key=lambda x: x.get("created_at", ""), reverse=True)


def get_report(report_id: str):
    data = _read(REPORTS_FILE)
    for r in data["reports"]:
        if r["id"] == report_id:
            return r
    return None


def delete_report(report_id: str):
    data = _read(REPORTS_FILE)
    data["reports"] = [r for r in data["reports"] if r["id"] != report_id]
    _write(REPORTS_FILE, data)
