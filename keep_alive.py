# keep_alive.py আপডেট করুন
import os
from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

def run():
    # রেন্ডার থেকে পোর্ট নাম্বারটি অটোমেটিক নেবে, না থাকলে ডিফল্ট ৮০৮০
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run)
    t.start()
