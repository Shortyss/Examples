# 1JAcnSkyjjyE2wuZ

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