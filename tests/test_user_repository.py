from lib.user_repository import UserRepository
from lib.user import User

def test_get_all_users(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = UserRepository(db_connection)

    users = repository.all()

    assert users == [
    User(1, 'user_1@test.com', 'Rock'),
    User(2, 'user_2@test.com', 'Pop'),
    User(3, 'user_3@test.com', 'Pop'),
    User(4, 'user_4@test.com', 'Jazz')
    ]
def test_find_a_user(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = UserRepository(db_connection)
    user = repository.find('user_1@test.com', 'Rock')
    assert user == True

def test_no_user_found(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = UserRepository(db_connection)
    user = repository.find('user1@test.com', 'Fun')
    assert user == False
    
def test_add_user_adds_to_table(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = UserRepository(db_connection)
    new_user = User(None, "email_13@gmail.com", "pass123")
    repository.add(new_user)
    assert repository.all() == [
    User(1, 'user_1@test.com', 'Rock'),
    User(2, 'user_2@test.com', 'Pop'),
    User(3, 'user_3@test.com', 'Pop'),
    User(4, 'user_4@test.com', 'Jazz'),
    User(5, "email_13@gmail.com", "pass123")
    ]
