class SpaceParametersValidator:
    def __init__(self, name, description, price, date_from, date_to, image_url):
        self.name = name
        self.description = description
        self.price = price
        self.date_from = date_from
        self.date_to = date_to
        self.image_url = image_url

    def _is_valid(self):
        return self._is_name_valid() and self._is_description_valid() and self._is_price_valid()
    
    def generate_errors(self):
        errors = []
        if not self._is_name_valid():
            errors.append("Name must not be blank")
        if not self._is_description_valid():
            errors.append("Description must not be blank")
        if not self._is_price_valid():
            errors.append("Price must be a number")
        return errors
    
    def get_valid_name(self):
        if not self._is_name_valid():
            raise ValueError("Cannot get valid name")
        return self.name
    
    def get_valid_description(self):
        if not self._is_description_valid():
            raise ValueError("Cannot get valid description")
        return self.description
    
    def get_valid_price(self):
        if not self._is_price_valid():
            raise ValueError("Cannot get valid price")
        return self.price
    
    def get_valid_date_from(self):
        if not self._is_date_from_valid():
            raise ValueError("Cannot get valid date from")
        return self.date_from
    
    def get_valid_date_to(self):
        if not self._is_date_to_valid():
            raise ValueError("Cannot get valid date to")
        return self.date_to
    

    def _is_date_from_valid(self):
        if self.date_from == "":
            return False
        return True

    def _is_date_to_valid(self):
        if self.date_to == "":
            return False
        return True
    
    def _is_name_valid(self):
        if self.name is None:
            return False
        if self.name == "":
            return False
        return True
    
    def _is_description_valid(self):
        if self.description is None:
            return False
        if self.description == "":
            return False
        return True
    
    
    def _is_price_valid(self):
        if self.price is None:
            return False
        if not self.price.replace('.', '', 1).isdigit():
            return False
        return True


