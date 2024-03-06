from lib.user import User

def test_user_constructs():
    user = User(1, "email_1", "password_1") 
    assert user.id == 1
    assert user.email_address == "email_1"
    assert user.password == "password_1"

def test_users_are_equal():
    user1 = User(1, "email_1", "password_1") 
    user2 = User(1, "email_1", "password_1") 
    assert user1 == user2

def test_user_format():
    user = User(1, "email_1", "password_1") 
    assert str(user) == "User(1, email_1, password_1)" 

def test_is_email_valid():
    user = User(1, "emailtest", "password_1")
    assert user.generate_errors() == "not valid email, not valid password"

def test_if_email_password_blank():
    user = User(None, "", "")
    assert user.generate_errors() == "not valid email, not valid password"


    
    