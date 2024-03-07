import pandas as pd

class Space():
    
    def __init__(self, id, name, description, price, date_from, date_to, user_id, available_dates = None):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.date_from = date_from
        self.date_to = date_to
        self.user_id = user_id
        self.available_dates = pd.date_range(start=date_from, end=date_to)


    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Space({self.id}, {self.name}, {self.description}, {self.price}, {self.date_from}, {self.date_to}, {self.user_id})"
    

    # <a href="/booking_confirmation" class="button-link">
    #       <input type="button" value="Confirm your booking">
    #   </a>