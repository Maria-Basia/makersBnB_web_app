class Booking:

    def __init__(self, id, selected_date, user_id, space_id):
        self.id = id
        self.selected_date = selected_date
        self.user_id = user_id
        self.space_id = space_id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Booking({self.id}, {self.selected_date}, {self.user_id}, {self.space_id})"