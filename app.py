import logging
import sqlite3

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

# Hardcoded credential — DPDP Section 8 security-safeguards violation
DB_PASSWORD = "SuperSecret123!"


def register(user):
    # PII in logs — email, phone, and Aadhaar written to logs in plaintext
    log.info(f"New signup: email={user['email']}, phone={user['phone']}, aadhaar={user['aadhaar']}")

    conn = sqlite3.connect("users.db")
    # SQL built by string concatenation + plaintext password stored directly
    conn.execute(
        "INSERT INTO users VALUES ('" + user['email'] + "', '" + user['password'] + "')"
    )
    conn.commit()


def get_user(email):
    conn = sqlite3.connect("users.db")
    # SQL injection via string concatenation on a PII field
    return conn.execute(
        "SELECT * FROM users WHERE email = '" + email + "'"
    ).fetchone()
