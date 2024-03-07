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
                row["selected_date"],
                row["user_id"],
                row["space_id"]
                )
            print("HEREEEE")
            print(booking)
            print("HEREEEE")
            bookings.append(booking)
        print(bookings)
        return bookings
    
    def find(self, id):
        rows = self._connection.execute("SELECT * FROM bookings WHERE id =%s", [id])
        row = rows[0]
        return Booking(row["id"], row["selected_date"], row["user_id"], row["space_id"])
    
    def create(self, booking):
        rows = self._connection.execute('INSERT INTO bookings (selected_date, user_id, space_id) VALUES (%s, %s, %s)  RETURNING id', [
            booking.selected_date, booking.user_id, booking.space_id])
        row = rows[0]
        booking.id = row["id"] 
        return None
    

