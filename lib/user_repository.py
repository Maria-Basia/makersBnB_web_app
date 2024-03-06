from lib.user import User
class UserRepository:

    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM users')
        users = []
        for row in rows:
            item = User(row["id"], row["email_address"], row["password"])
            users.append(item)
        return users
    
    def find(self, email_address, password):
        rows = self._connection.execute('SELECT * FROM users WHERE email_address = %s AND password = %s', [email_address, password])
        if rows == []:
            return False
        return True
    
    def add(self, user):
        rows = self._connection.execute('INSERT INTO users (email_address, password) VALUES (%s, %s)', [
            user.email_address, user.password ])
        return user

    
    


