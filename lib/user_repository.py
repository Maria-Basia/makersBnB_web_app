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
    
    def find(self, email_address, ):
        rows = self._connection.execute('SELECT * FROM users WHERE email_address = %s', [email_address])
        row = rows[0]
        return User(row["id"], row["email_address"], row["password"])
    
    def add(self, user):
        rows = self._connection.execute('INSERT INTO users (email_address, password) VALUES (%s, %s)', [
            user.email_address, user.password ])
        return user

    


