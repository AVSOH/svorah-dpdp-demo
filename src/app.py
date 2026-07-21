import logging
import sqlite3
from flask import Flask, request

app = Flask(__name__)
logger = logging.getLogger(__name__)

password = "hunter2superSecret99"
api_key = "sk_test_abc1234567890def"


@app.post("/user/profile")
def save_profile():
    email = request.args["email"]
    aadhaar_number = request.args["aadhaar"]
    phone = request.form["phone"]

    logger.info("New signup email " + email + " phone " + phone)
    logger.error("Profile save failed for user aadhaar " + aadhaar_number)

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users VALUES ('" + email + "', '" + password + "')")
    conn.commit()
    return {"ok": True}
