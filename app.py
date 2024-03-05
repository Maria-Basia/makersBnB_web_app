import os
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
from lib.space import Space
from lib.space_repository import SpaceRepository
from lib.space_parameters_validator import SpaceParametersValidator

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# GET /index
# Returns the homepage
#testing if this works
#   ; open http://localhost:5000/index



@app.route('/index', methods=['GET'])
def get_all_spaces():
    connection = get_flask_database_connection(app)
    repository = SpaceRepository(connection)
    spaces = repository.all()
    return render_template("spaces/index.html", spaces=spaces)

@app.route('/index/<id>')
def get_space(id):
    connection = get_flask_database_connection(app)
    repository = SpaceRepository(connection)
    space = repository.find(id)
    return render_template("spaces/show.html", space=space)

@app.route('/index/new', methods=['GET'])
def get_space_new():
    return render_template("spaces/new.html")

@app.route('/index', methods=['POST'])
def create_space():
    connection = get_flask_database_connection(app)
    repository = SpaceRepository(connection)

    validator = SpaceParametersValidator(
        request.form['name'],
        request.form['description'],
        request.form['price']
    )

    if not validator._is_valid():
        errors = validator.generate_errors()
        return render_template("spaces/new.html", errors=errors)
    space = Space(
        None,
        validator.get_valid_name(),
        validator.get_valid_description(),
        validator.get_valid_price(),
        1)
    repository.create(space)

    return redirect(f"/index/{space.id}")

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))


    









