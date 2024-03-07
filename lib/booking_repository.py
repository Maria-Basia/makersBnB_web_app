from lib.booking import Booking

class BookingRepository:

    def __init__(self, connection):
        self._connection = connection
        
    def all(self):
        rows = self._connection.execute("SELECT * FROM bookings")
        bookings = []
        for row in rows:
            booking = Booking(
                row["id"], 
                row["date_from"],
                row["date_to"],
                row["user_id"],
                row["space_id"]
                )
            bookings.append(booking)
        return bookings
    
    def find(self, id):
        rows = self._connection.execute("SELECT * FROM bookings WHERE id =%s", [id])
        row = rows[0]
        return Booking(row["id"], row["date_from"], row["date_to"], row["user_id"], row["space_id"])
    
    def add(self, booking):
        rows = self._connection.execute('INSERT INTO bookings (date_from, date_to, user_id, space_id) VALUES (%s, %s, %s, %s)', [
            booking.date_from, booking.date_to, booking.user_id, booking.space_id ])
        row = rows[0]
        booking.id = row["id"] 
        return None