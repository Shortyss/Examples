from flask import render_template, request, redirect, url_for

from models import db, app, Pet


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add-pet", methods=["GET", "POST"])
def add_pet():
    if request.form:  # tady jde post
        new_pet = Pet(
            name=request.form["name"],
            age=request.form["age"],
            breed=request.form["breed"],
            color=request.form["color"],
            size=request.form["size"],
            weight=request.form["weight"],
            url=request.form["url"],
            gender=request.form["gender"],
            spay=request.form["spay"],
            description=request.form["description"],
        )
        db.session.add(new_pet)
        db.session.commit()
        return redirect(url_for("index"))

    return render_template("addpet.html")


@app.route("/pet/<id>")
def pet(id):
    pet = Pet.query.get_or_404(id)
    return render_template("pet.html", pet=pet)


# MVC - model view controller - Flask
# MVP - model view presenter - Netter PHP
# MVVM - model view view-model - Angular


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True)