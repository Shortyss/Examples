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

@app.route("/edit/<id>", methods=['GET', 'POST'])
def edit_pet(id):
    pet = Pet.query.get(id)
    if request.form:
        pet.name = request.form['name']
        pet.age = request.form['age']
        pet.breed = request.form['breed']
        pet.color = request.form['color']
        pet.weight = request.form['weight']
        pet.size = request.form['size']
        pet.url = request.form['url']
        pet.url_tag = request.form['alt']
        pet.pet = request.form['pet']
        pet.gender = request.form['gender']
        pet.spay = request.form['spay']
        pet.house_trained = request.form['housetrained']
        pet.description = request.form['description']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template("editpet.html", pet=pet)


@app.route('/remove/<id>')
def remove_pet(id):
    pet = Pet.query.get(id)
    db.session.delete(pet)
    db.session.commit()
    return redirect(url_for('index'))


# MVC - model view controller - Flask
# MVP - model view presenter - Netter PHP
# MVVM - model view view-model - Angular


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True)