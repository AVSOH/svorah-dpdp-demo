import logging
import sqlite3
from flask import Flask, request

app = Flask(__name__)
logger = logging.getLogger(__name__)

password = "hunter2superSecret99"
api_key = "sk_test_abc1234567890def"


@app.post("/user/profile")
def save_profile():
14 |     email = request.args["email"]
      15 |     aadhaar_number = request.args["aadhaar"]
      16 |     phone = request.form["phone"]
      17 | 
      18 |     logger.info("New signup email " + mask_email(email) + " phone " + mask_phone(phone))
>>>   19 |     logger.error("Profile save failed for user aadhaar " + mask_aadhaar(aadhaar_number))
      20 | 
      21 |     conn = sqlite3.connect("users.db")
      22 |     cursor = conn.cursor()
      23 |     cursor.execute("INSERT INTO users VALUES ('" + mask_email(email) + "', '" + password + "')")
      24 |     conn.commit()
    return {"ok": True}
