class Booking:

    def __init__(self, id, date_from, date_to, user_id, space_id):
        self.id = id
        self.date_from = date_from
        self.date_to = date_to
        self.user_id = user_id
        self.space_id = space_id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Booking({self.id}, {self.date_from}, {self.date_to} {self.user_id}, {self.space_id})"