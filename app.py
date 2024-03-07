import os
from flask import Flask, request, render_template, redirect, session
from lib.database_connection import get_flask_database_connection
from lib.space import Space
from lib.space_repository import SpaceRepository
from lib.space_parameters_validator import SpaceParametersValidator
from lib.user_repository import UserRepository
from lib.booking import Booking
from lib.booking_repository import BookingRepository
from lib.user import User
import secrets

# Create a new Flask app
app = Flask(__name__)

app.secret_key = secrets.token_hex(24)

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
    if 'user_id' in session and 'email_address' in session:
        user_id = session['user_id']
        email_address = session['email_address']
        return render_template("spaces/index.html", spaces=spaces, email_address=email_address)
    else:
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
        request.form['price'],
        request.form['date_from'],
        request.form['date_to']
    )

    if not validator._is_valid():
        errors = validator.generate_errors()
        return render_template("spaces/new.html", errors=errors)
    space = Space(
        None,
        validator.get_valid_name(),
        validator.get_valid_description(),
        validator.get_valid_price(),
        validator.get_valid_date_from(),
        validator.get_valid_date_to(),
        1)
    repository.create(space)

    return redirect(f"/index/{space.id}")

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.

@app.route('/booking_confirmation', methods=['GET'])
def get_booking_confirmation_page():
    return render_template("spaces/booking_confirmation.html")



@app.route('/index', methods=['POST'])
def create_booking():
    connection = get_flask_database_connection(app)
    repository = BookingRepository(connection)

    date_chosen = request.form['selected_date']

    booking = Booking(
        None,
        date_chosen,
        1,
        1)
    repository.create(booking)
    return redirect(f"/booking_confirmation")




# @app.route('/index/<id>')
# def get_space(id):
#     connection = get_flask_database_connection(app)
#     repository = SpaceRepository(connection)
#     space = repository.find(id)
#     requested_date = request.form['requested_date']
#     repository.select_date(id)

#     return render_template("spaces/show.html", space=space)














































































































#Users logic starts here
    
@app.route('/MakersBNB', methods=['GET'])
def get_homepage():
    return render_template('homepage.html')

@app.route('/MakersBNB', methods=['POST'])
def post_new_user():
    connection = get_flask_database_connection(app)
    user_repository = UserRepository(connection)
    email_address = request.form['email_address']
    password = request.form['password']
    confirm_password = request.form['confirm_password']
    user = User(None, email_address, password)
    if user_repository.validate_email(email_address):
        return render_template('homepage.html', user=user, errors="email already in use"), 400
    elif password != confirm_password:
        return render_template('homepage.html', user=user, errors="passwords do not match"), 400
    elif not user.password_is_valid() or not user.email_is_valid() or not password == confirm_password:
        return render_template('homepage.html', user=user, errors=user.generate_errors()), 400
    else:
        user_repository.add(user)
        session['user_id'] = user.id
        session['email_address'] = user.email_address

        return redirect('/index')

@app.route('/users', methods=['GET'])
def get_users():
    connection = get_flask_database_connection(app)
    user_repository = UserRepository(connection)
    users = user_repository.all()
    return render_template("users_list.html", users = users) 

@app.route('/Login', methods=['GET'])
def get_user_login():
    return render_template('login.html')
    

# @app.route('/Login', methods=['POST'])
# def post_user_login():
#     connection = get_flask_database_connection(app)
#     user_repository = UserRepository(connection)
#     email_address = request.form['email_address']
#     password = request.form['password']
#     user_found = user_repository.validate_login(email_address, password)
#     #if not user_found:
#     #    return render_template('login.html', error="Email or Password not found"), 400
#     return redirect('/index')





@app.route('/Login', methods=['POST'])
def login_post():
    email_address = request.form['email_address']
    password = request.form['password']

    connection = get_flask_database_connection(app)
    user_repository = UserRepository(connection)
    session_v = user_repository.find(email_address, password)
    user_found = user_repository.validate_login(email_address, password)
    if not user_found:
        return render_template('login.html', error="Email or Password not found"), 400
    else:
        # Set the user ID in session
        session['user_id'] = session_v.id
        session['email_address'] = session_v.email_address

        return redirect('/index')




















if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
