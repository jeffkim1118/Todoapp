from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime
# from sqlalchemy.orm import DeclarativeBase
# from config import Config
# from models import Task

app = Flask(__name__)
# app.config.from_object(Config)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db' # Location of the db
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Makes warning message to go away


db = SQLAlchemy(app)

class TodoNote(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    note = db.Column(db.String(100))
    date_created = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, note, date_created):
        self.note = note
        self.date_created = date_created
        
        
# class TodoNote(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     todo = db.Column(db.String(100), unique=False, nullable=False)
    
#     def __repr__(self):
#         return f'<User {self.username}>'

# with app.app_context():
#         db.create_all()


# new_todo = TodoNote(todo="Send an email to my mother")
# db.session.add(new_todo)
# db.session.commit()

# todoNotes = TodoNote.query.all()


# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

# @app.route("/tasks")
# def show_tasks():
#     return todoNotes


# Create the database if the database doesn't exist.
if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)