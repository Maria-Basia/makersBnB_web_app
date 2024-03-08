from lib.space import Space
from lib.space_repository import SpaceRepository
import datetime

"""When I call #all in the SpaceRepository 
I get all the Spaces back in the list"""

def test_get_all_spaces(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = SpaceRepository(db_connection)
    result = repository.all()
    assert result == [
        Space(1, "space_1", "description_1", 45.50, datetime.date(2004, 4, 22), datetime.date(2005, 5, 24), "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQuGLC22QwkKwitA_xtn6tuNDLNYOHpKJRvWA&usqp=CAU", 1),
        Space(2, "space_2", "description_2", 14000.99, datetime.date(2003, 3, 11), datetime.date(2002, 2, 3), "https://images.unsplash.com/photo-1611622295630-7839220cf0e8?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8N3x8c2hhY2t8ZW58MHx8MHx8fDA%3D", 2)
    ]




"""When we call #find in SpaceRepository with a 
specific id we are presented with the Space attached to 
this id"""

def test_find_space_with_id(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = SpaceRepository(db_connection)
    result = repository.find(1)
    assert result == Space(1, "space_1", "description_1", 45.50, datetime.date(2004, 4, 22), datetime.date(2005, 5, 24), "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQuGLC22QwkKwitA_xtn6tuNDLNYOHpKJRvWA&usqp=CAU", 1)

def test_create(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = SpaceRepository(db_connection)
    space = Space(None, "mybnb", "in beverley hills", 9000, datetime.date(2024, 3, 10), datetime.date(2024, 3, 15), "https://www.google.com/url?sa=i&url=https%3A%2F%2Fpicsum.photos%2F&psig=AOvVaw19lgLrStfZ1km9nKsbgciA&ust=1710014076081000&source=images&cd=vfe&opi=89978449&ved=0CBMQjRxqFwoTCOCam_645YQDFQAAAAAdAAAAABAE", 2)
    repository.create(space)
    assert space.id == 3
    assert repository.all() == [
        Space(1, "space_1", "description_1", 45.50, datetime.date(2004, 4, 22), datetime.date(2005, 5, 24), "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQuGLC22QwkKwitA_xtn6tuNDLNYOHpKJRvWA&usqp=CAU", 1),
        Space(2, "space_2", "description_2", 14000.99, datetime.date(2003, 3, 11), datetime.date(2002, 2, 3), "https://images.unsplash.com/photo-1611622295630-7839220cf0e8?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8N3x8c2hhY2t8ZW58MHx8MHx8fDA%3D", 2),
        Space(3, "mybnb", "in beverley hills", 9000.0, datetime.date(2024, 3, 10), datetime.date(2024, 3, 15), "https://www.google.com/url?sa=i&url=https%3A%2F%2Fpicsum.photos%2F&psig=AOvVaw19lgLrStfZ1km9nKsbgciA&ust=1710014076081000&source=images&cd=vfe&opi=89978449&ved=0CBMQjRxqFwoTCOCam_645YQDFQAAAAAdAAAAABAE", 2)
    ]

# def test_date(db_connection):
#     db_connection.seed("seeds/makersbnb.sql")
#     repository = SpaceRepository(db_connection)
#     repository.select_date(1)
