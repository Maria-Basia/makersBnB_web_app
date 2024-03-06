class User:

    def __init__(self, id, email_address, password):
        self.id = id
        self.email_address = email_address
        self.password = password

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    def __repr__(self):
        return f"User({self.id}, {self.email_address}, {self.password})"
    
    def password_is_valid(self):
        return self.valid_length() and self.has_special_characters()
    
    def email_is_valid(self):
        return "@" in self.email_address
    
    def valid_length(self):
        return len(self.password) > 7

    def has_special_characters(self):
        characters = ["!","@","$","%","&"]
        for char in characters:
            if char in self.password:
                return True
        return False
    
    def generate_errors(self):
        errors = []
        if self.email_is_valid() == False:
            errors.append("not valid email")

        if self.password_is_valid() == False:
            errors.append("not valid password")


        if len(errors) == 0:
            return None
        else:
            return ", ".join(errors)
        
    
        