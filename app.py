import logging
import sqlite3
from flask import Flask, request

app = Flask(__name__)
logger = logging.getLogger(__name__)

# DPDP-009: hardcoded credentials committed to source
password = "hunter2superSecret99"
api_key = "sk_test_abc1234567890def"


@app.post("/user/profile")
def save_profile():
    # DPDP-004: personal data read straight from request parameters
    email = request.args["email"]
    aadhaar_number = request.args["aadhaar"]
    phone = request.form["phone"]

    # DPDP-002: personal data written to logs in plaintext
    logger.info("New signup email " + email + " phone " + phone)
    logger.error("Profile save failed for user aadhaar " + aadhaar_number)

    # DPDP-010: raw SQL with plaintext password, built by string concatenation
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users VALUES ('" + email + "', '" + password + "')")
    conn.commit()
    return {"ok": True}
