from lib.space import Space

"""
Constructs with a id, name, description, price and user_id
"""

def test_constructs():

    space = Space(1, "mybnb", "in beverley hills", 9000, "2004-04-22", "2005-05-24", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQuGLC22QwkKwitA_xtn6tuNDLNYOHpKJRvWA&usqp=CAU", 2)

    assert space.id == 1
    assert space.name == "mybnb"
    assert space.description == "in beverley hills"
    assert space.price == 9000
    assert space.date_from == "2004-04-22"
    assert space.date_to == "2005-05-24"
    assert space.image_url == 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQuGLC22QwkKwitA_xtn6tuNDLNYOHpKJRvWA&usqp=CAU'
    assert space.user_id == 2


"""
Space with equal contents are equal
"""

def test_equal():
    space1 = Space(1, "mybnb", "in beverley hills", 9000, "2004-04-22", "2005-05-24", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQuGLC22QwkKwitA_xtn6tuNDLNYOHpKJRvWA&usqp=CAU", 1)
    space2 = Space(1, "mybnb", "in beverley hills", 9000, "2004-04-22", "2005-05-24", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQuGLC22QwkKwitA_xtn6tuNDLNYOHpKJRvWA&usqp=CAU", 1)
    assert space1 == space2


"""
Spaces format to string
"""

def test_format():
    space = Space(1, "mybnb", "in beverley hills", 9000, "2004-04-22", "2005-05-24", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQuGLC22QwkKwitA_xtn6tuNDLNYOHpKJRvWA&usqp=CAU", 2)
    assert str(space) == "Space(1, mybnb, in beverley hills, 9000, 2004-04-22, 2005-05-24, https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQuGLC22QwkKwitA_xtn6tuNDLNYOHpKJRvWA&usqp=CAU, 2)"

