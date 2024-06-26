# {{TABLE NAME}} Model and Repository Classes Design Recipe

_Copy this recipe template to design and implement Model and Repository classes for a database table._

## 1. Design and create the Table

If the table is already created in the database, you can skip this step.

## 2. Create Test SQL seeds

Your tests will depend on data stored in PostgreSQL to run.

If seed data is provided (or you already created it), you can skip this step.

```sql
-- EXAMPLE
-- (file: spec/seeds_{table_name}.sql)

-- Write your SQL seed here. 

-- First, you'd need to truncate the table - this is so our table is emptied between each test run,
-- so we can start with a fresh state.
-- (RESTART IDENTITY resets the primary key)

TRUNCATE TABLE students RESTART IDENTITY; -- replace with your own table name.

-- Below this line there should only be `INSERT` statements.
-- Replace these statements with your own seed data.

INSERT INTO students (name, cohort_name) VALUES ('David', 'April 2022');
INSERT INTO students (name, cohort_name) VALUES ('Anna', 'May 2022');
```

Run this SQL file on the database to truncate (empty) the table, and insert the seed data. Be mindful of the fact any existing records in the table will be deleted.

```bash
psql -h 127.0.0.1 your_database_name < seeds_{table_name}.sql
```

## 3. Define the class names

Usually, the Model class name will be the capitalised table name (single instead of plural). The same name is then suffixed by `Repository` for the Repository class name.

```python
# Table name: albums

# Model class
# (in lib/album.py)
class User


# Repository class
# (in lib/album_repository.py)
class UserRepository

```

## 4. Implement the Model class

Define the attributes of your Model class. You can usually map the table columns to the attributes of the class, including primary and foreign keys.

```python
# Table name: albums

# Model class
# (in lib/album.py)

class User:
    def __init__(self):
        self.id = 0
        self.email = ""
        self.password = ""
    

        # Replace the attributes by your own columns.


# We can set the attributes to default empty values and set them later,
# here's an example:
#
# >>> student = Student()
# >>> student.name = "Will"
# >>> student.cohort_name = "September Devs"
# >>> student.name
# 'Will'
# >>> student.cohort_name
# 'September Devs'

```

*You may choose to test-drive this class, but unless it contains any more logic than the example above, it is probably not needed.*

## 5. Define the Repository Class interface

Your Repository class will need to implement methods for each "read" or "write" operation you'd like to run against the database.

Using comments, define the method signatures (arguments and return value) and what they do - write up the SQL queries that will be used by each method.

```python
# Table name: albums

# Repository class
# (in lib/album_repository.py)

class UserRepository():

    def __init__(self, connection):
        self._connection = connection 


    def add(self, user):

        #user = Executes the SQL query:
        #INSERT INTO Users (id, email, password)

    # Selecting all records
    # No arguments
    #def all():
        # Executes the SQL query:
        # SELECT id, title, release_year, artist_id FROM albums;

        # Returns an array of Album objects.


        # Gets a single record by its ID
        # One argument: the id (number)
    #def find(id):
        # Executes the SQL query:
        # SELECT id, name, cohort_name FROM students WHERE id = $1;

        # Returns a single Student object.

        # Add more methods below for each operation you'd like to implement.

    # def create(student)
    # 

    # def update(student)
    # 

    # def delete(student)
    # 

```

## 6. Write Test Examples

Write Python code that defines the expected behaviour of the Repository class, following your design from the table written in step 5.

These examples will later be encoded as Pytest tests.

```python
# EXAMPLES

# 1
# Get all albums

repo = AlbumRepository()

albums = repo.all()

len(albums) # =>  12

albums[0].id # =>  1
albums[0].title # =>  'Doolittle'
albums[0].release_year # =>  1989
albums[0].artist_id # =>  1

albums[1].id # =>  2
albums[1].title # =>  'Surfer Rosa'
albums[1].release_year # =>  1988
albums[1].artist_id # =>  1

....

# 2
# Get a single album

repo = AlbumRepository()

album = repo.find(1)

album.id # =>  1
album.title # =>  'Doolittle'
album.release_year # =>  1989
album.artist_id #=> 1

# Add more examples for each method
```

Encode this example as a test.


## 7. Test-drive and implement the Repository class behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._