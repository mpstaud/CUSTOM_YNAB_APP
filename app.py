from dotenv import load_dotenv
load_dotenv()
import os
from flask import Flask, jsonify, request
import requests


app = Flask(__name__)

YNAB_TOKEN = os.getenv("YNAB_TOKEN")
YNAB_BASE_URL = "https://api.ynab.com/v1"

headers = {"Authorization": f"Bearer {YNAB_TOKEN}"}

@app.route('/')
def home():
    return '<h1>Matts YNAB App</h1>'

@app.route('/budgets', methods=["GET"])
def get_budgets():
    response = requests.get(f"{YNAB_BASE_URL}/budgets", headers=headers)
    data = response.json()
    return jsonify(data)

if __name__ == '__main__':
    app.run()