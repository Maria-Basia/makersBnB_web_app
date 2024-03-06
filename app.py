import os
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
from lib.space import Space
from lib.space_repository import SpaceRepository
from lib.user_repository import UserRepository
from lib.user import User

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

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.


    




















































































































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
    user = User(None, email_address, password)
    if not user.password_is_valid() or not user.email_is_valid():
        return render_template('homepage.html', user=user, errors=user.generate_errors()), 400
    user = user_repository.add(user)
    return redirect('/users')

@app.route('/users', methods=['GET'])
def get_users():
    connection = get_flask_database_connection(app)
    user_repository = UserRepository(connection)
    users = user_repository.all()
    return render_template("users_list.html", users = users) 

@app.route('/Login', methods=['POST'])
def post_new_user():
    connection = get_flask_database_connection(app)
    user_repository = UserRepository(connection)
    email_address = request.form['email_address']
    password = request.form['password']
    user = User(None, email_address, password)
    #if not user.password_is_valid() or not user.email_is_valid():
    #    return render_template('homepage.html', user=user, errors=user.generate_errors()), 400
    
    return redirect('/index')



























if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
