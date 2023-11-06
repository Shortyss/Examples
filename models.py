# 1JAcnSkyjjyE2wuZ
import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

user = "postgres"
password = "1JAcnSkyjjyE2wuZ"
host = "db.trkvexjwateosjxemsvg.supabase.co"
port = 5432
db_name = "postgres"

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql+psycopg://{user}:password@{host}:{port}/postgres?password={password}"


db = SQLAlchemy(app)


class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=datetime.datetime.now)
    name = db.Column(db.String())
    age = db.Column(db.String())
    breed = db.Column(db.String())
    color = db.Column(db.String())
    size = db.Column(db.String())
    weight = db.Column(db.String())
    url = db.Column(db.String())
    gender = db.Column(db.String())
    spay = db.Column(db.String())
    description = db.Column(db.String())

    def __repr__(self):
        return f'''<Pet Name: {self.name} Age: {self.age} 
                    Breed: {self.breed} Color: {self.color}
                    Size: {self.size} Weight: {self.weight}
                    URL: {self.url} Type: {self.pet_type}
                    Gender: {self.gender} Spay: {self.spay}
                    House Trained: {self.house_trained}
                    Description: {self.description}>'''