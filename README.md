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

## APP DESCRIPTION

# MakersBnB | AirBnB-like web app | March 2024 | 2-week project
**Tech Python | Flask | Pytest | HTML | CSS | PostgreSQL**
**Group project**

A property rental web app similar to Airbnb. The project was developed using Test-Driven Development (TDD). Key features include user signup and login with sessions, viewing all property listings, detailed property pages, single-night bookings, and creating new property listings.



