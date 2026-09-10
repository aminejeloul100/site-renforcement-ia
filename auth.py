import hashlib
import json
import uuid
from pathlib import Path

USERS_PATH = Path(__file__).parent / "data" / "users.json"


def _load_users():
    if not USERS_PATH.exists():
        return {}
    return json.loads(USERS_PATH.read_text(encoding="utf-8"))


def _save_users(users):
    USERS_PATH.parent.mkdir(parents=True, exist_ok=True)
    USERS_PATH.write_text(json.dumps(users, ensure_ascii=False, indent=2), encoding="utf-8")


def _hash_password(password: str, salt: str) -> str:
    return hashlib.sha256((salt + password).encode("utf-8")).hexdigest()


def register(username: str, password: str):
    users = _load_users()
    if username in users:
        return False, "Ce nom d'utilisateur existe déjà."
    salt = uuid.uuid4().hex
    users[username] = {"salt": salt, "hash": _hash_password(password, salt)}
    _save_users(users)
    return True, "Compte créé avec succès."


def login(username: str, password: str):
    users = _load_users()
    if username not in users:
        return False, "Utilisateur introuvable."
    u = users[username]
    if _hash_password(password, u["salt"]) != u["hash"]:
        return False, "Mot de passe incorrect."
    return True, "Connexion réussie."
