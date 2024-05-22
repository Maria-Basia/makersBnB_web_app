## SETUP

```shell
# Install dependencies and set up the virtual environment
; pipenv install

# Activate the virtual environment
; pipenv shell

# Install the virtual browser we will use for testing
; playwright install

# Install postgreSQL
; brew install postgresql@15 # @number indicates latest version

#Make sure postgreSQL installation directory is on your PATH environment variable. 
<sub>In the output from the Homebrew installation</sub>
<sub>you just ran, should be a line which looks like the below:</sub>
; echo 'export PATH="/opt/homebrew/opt/postgresql@15/bin:$PATH"' >> ~/.zshrc

#Start the postgreSQL software in the background
; $ brew services start postgresql@15

# Create a test and development database
; createdb makersbnb_db
; createdb makersbnb_db_test

#Reset all of the database tables and add any data that is needed for the tests to run.
<sub>This is so that our tests, and application, are always operating from a fresh</sub>
; psql -h 127.0.0.1 makersbnb_db < seeds/database_connection.sql

#Seed the database
; psql -h 127.0.0.1 makersbnb_db < seeds/makersbnb.sql  

# Run the tests (with extra logging)
; pytest -sv

# Run the app
; python app.py

# Now visit http://localhost:5000/index in your browser
```

## WEB APP DESCRIPTION

# MakersBnB | AirBnB-like web app | March 2024 | 2-week project
**Tech Python | Flask | Pytest | HTML | CSS | PostgreSQL**
**Group project**

A property rental web app similar to Airbnb. Key features include user signup and login with sessions, viewing all property listings, detailed property pages, single-night bookings, and creating new property listings. 

The backend of the application is built using Python and Flask, providing a robust framework for handling routing, session management, and database interactions.

A PostgreSQL database was used to store User and Property data, enabling efficient linking between the User and Property tables.

The frontend is developed using HTML to structure the web pages and CSS to enhance the visual appeal and the layout.

Test-Driven Development (TDD) was applied throughout the project. The testing framework used is Pytest and the project achieves 100% test coverage. 

# Login page

![Creenshot of the signup page](<Screenshot 2024-05-22 at 11.33.39.png>)







