class User:

    def __init__(self, id, email_address, password):
        self.id = id
        self.email_address = email_address
        self.password = password

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    def __repr__(self):
        return f"User({self.id}, {self.email_address}, {self.password})"
    
    def is_valid(self):
        return self.valid_length(self.password) and self.has_special_characters(self.password)

    def valid_length(self):
        return len(self.password) > 7

    def has_special_characters(self):
        characters = ["!","@","$","%","&"]
        for char in characters:
            if char in self.password:
                return True
        return False
        