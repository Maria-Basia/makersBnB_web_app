## Setup

```shell
# Install dependencies and set up the virtual environment
; pipenv install

# Activate the virtual environment
; pipenv shell

# Install the virtual browser we will use for testing
; playwright install

#Install psycopg
; pipenv install psycopg2

# Install postgreSQL
; brew install postgresql@15 # @number indicates latest version

#Once you install postgreSQL, you'll need to make sure that the 
#installation directory is on your PATH environment variable. 
#In the output from the Homebrew installation 
#you just ran, should be a line which looks like the below:
; echo 'export PATH="/opt/homebrew/opt/postgresql@15/bin:$PATH"' >> ~/.zshrc

#Start the postgreSQL software in the background
; $ brew services start postgresql@15

# Create a test and development database
; createdb makersbnb_db
; createdb makersbnb_db_test

#Reset all of the database tables and add any data that is needed for the tests to run.
#This is so that our tests, and application, are always operating from a fresh 
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

