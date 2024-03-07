from lib.booking import Booking
from lib.booking_repository import BookingRepository

"""When I call #all in the SpaceRepository 
I get all the Spaces back in the list"""

def test_get_all_bookings(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = BookingRepository(db_connection)
    result = repository.all()
    assert result == [
        Booking(1, '2024-03-10', '2024-03-12', 1, 1),
        Booking(2, '2024-03-20', '2024-04-01', 2, 2) ]

#stupid assertion error 

def test_find_booing_with_id(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = BookingRepository(db_connection)
    result = repository.find(1)
    assert result == Booking('2024/03/10', '2024/03/12', 1, 1)