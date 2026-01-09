from dotenv import load_dotenv
load_dotenv()
import os
from flask import Flask, jsonify, request
import requests
from flask_restful import Api, Resource, fields, marshal_with, abort
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
api = Api(app)

YNAB_TOKEN = os.getenv("YNAB_TOKEN")
YNAB_BASE_URL = "https://api.ynab.com/v1"
BUDGET_ID = "98715f8e-a625-45d9-98d2-9407e0af37b8"

headers = {"Authorization": f"Bearer {YNAB_TOKEN}"}

class BudgetModel(db.Model):
    __tablename__ = "budgets"
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    last_modified_on = db.Column(db.String(50))
    def __repr__(self):
        return f"Budget(id={self.id}, name={self.name})"


budgetFields = {
    "id": fields.String,
    "name": fields.String,
    "last_modified_on": fields.String,
}



@app.route('/')
def home():
    return '<h1>Matts YNAB App</h1>'

@app.route('/budgets', methods=["GET"])
def get_budgets():
    response = requests.get(f"{YNAB_BASE_URL}/budgets", headers=headers)
    data = response.json()
    return jsonify(data)

@app.route('/categories', methods=["GET"])
def get_categories():
    response = requests.get(f"{YNAB_BASE_URL}/budgets/{BUDGET_ID}/categories")
    data = response.json()
    return jsonify(data)

if __name__ == '__main__':
    app.run()