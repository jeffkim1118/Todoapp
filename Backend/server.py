from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from config import Config
from models import Task

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(model_class=Base)




@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/tasks")
def show_tasks():
    return "<li>Go to work</li>"


if __name__ == "__main__":
    app.run(debug=True)