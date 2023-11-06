from flask import render_template

from models import db, app


@app.route("/")
def index():
    return render_template("index.html")

# MVC - model view controller - Flask
# MVP - model view presenter - Netter PHP
# MVVM - model view view-model - Angular


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True)