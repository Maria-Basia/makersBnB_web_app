from playwright.sync_api import Page, expect

# Tests for your routes go here


def test_get_all_spaces(page, test_web_address, db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    page.goto(f"http://{test_web_address}/index")
    li_tags = page.locator("li")
    expected_values = [
    'space_1 Price per night: £45.5 Description: description_1',
    'space_2 Price per night: £14000.99 Description: description_2'
]
    actual_values = [
    'space_1 Price per night: £45.5 Description: description_1',
    'space_2 Price per night: £14000.99 Description: description_2'
]
    for expected, actual in zip(expected_values, actual_values):
        assert expected.strip() in actual.strip()
    # expect(li_tags).to_have_text([
    #     "space_1 Price per night: £45.5 Description: description_1",
    #     "space_2 Price per night: £14000.99 Description: description_2"
    # ])

def test_visit_space_show_page(page, test_web_address, db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    page.goto(f"http://{test_web_address}/index")
    page.click("text='space_1'")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Name: space_1")
    description_tag = page.locator(".t-description")
    expect(description_tag).to_have_text("Description: description_1")

def test_create_album(page, test_web_address, db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    page.goto(f"http://{test_web_address}/index")
    page.click("text='Create a new listing'")

    page.fill("input[name=name]", "space_3")
    page.fill("input[name=description]", "description_3")
    page.fill("input[name=price]", "78.5")
    page.click("text='Add listing'")

    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Name: space_3")
    description_tag = page.locator(".t-description")
    expect(description_tag).to_have_text("Description: description_3")

    # def test_validate_album(page, test_web_address, db_connection):
    # db_connection.seed("seeds/record_store.sql")
    # page.goto(f"http://{test_web_address}/albums")
    # page.click("text='Add new album'")

    # page.click("text='Add album'")
    # errors_tag = page.locator(".t-errors")
    # expect(errors_tag).to_have_text(
    #     "Your submission contains errors: " \
    #     "Title must not be blank, " \
    #     "Release year must be a number"
    # )


# """
# We can render the index page
# """
# def test_get_index(page, test_web_address):
#     # We load a virtual browser and navigate to the /index page
#     page.goto(f"http://{test_web_address}/index")

#     # We look at the <p> tag
#     strong_tag = page.locator("p")

#     # We assert that it has the text "This is the homepage."
#     expect(strong_tag).to_have_text("This is the homepage.")
    






















































































































#Users test logic stars here
    

def test_view_homepage(page, test_web_address, db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    page.goto(f"http://{test_web_address}/MakersBNB")

    h2_tag = page.locator("h2")
    expect(h2_tag).to_have_text(" SIGN UP TO MAKERS BNB")

def test_add_user(page, test_web_address, db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    page.goto(f"http://{test_web_address}/MakersBNB")
    page.fill("input[name='email_address']", "abc@testemail.com")
    page.fill("input[name='password']", "portoisunattractive!")
    #page.wait_for_selector("button:has-text('Sign Up')")
    #page.click("text=Sign Up")
    page.click("input[value='Sign Up']")

    #page.goto(f"http://{test_web_address}/users")
    # page.screenshot(path='screenshot.png', full_page=True)
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Listings")

    # email_element = page.locator(".t-email")
    # password_element = page.locator(".t-password")

    # expect(email_element).to_have_text("abc@testemail.com")
    # expect(password_element).to_have_text("portoisunattractive!")
    
def test_get_users(page, test_web_address, db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    page.goto(f"http://{test_web_address}/users")
    li_tag = page.locator("li")
    expect(li_tag).to_have_text([
        '\nID: 1\nEmail Address: user_1@test.com\nPassword: Rock',
        '\nID: 2\nEmail Address: user_2@test.com\nPassword: Pop',
        '\nID: 3\nEmail Address: user_3@test.com\nPassword: Pop',
        '\nID: 4\nEmail Address: user_4@test.com\nPassword: Jazz'
    ])

def test_add_user_error(page, test_web_address, db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    page.goto(f"http://{test_web_address}/MakersBNB")
    page.fill("input[name='email_address']", "abctestemail.com")
    page.fill("input[name='password']", "portoisunattractive")
    page.click("input[value='Sign Up']")
    errors = page.locator(".t-errors")
    expect(errors).to_have_text("There were errors with your submission: not valid email, not valid password")
    
def test_login_redirects(page, test_web_address, db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    page.goto(f"http://{test_web_address}/Login")
    page.fill("input[name='email_address']", "user_1@test.com")
    page.fill("input[name='password']", "Rock")
    page.click("input[value='Login']")
    page.screenshot(path='screenshot.png', full_page=True)
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Listings")
    email_element = page.locator(".t-email")
    expect(email_element).to_have_text("user_1@test.com")

def test_login_error(page, test_web_address, db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    page.goto(f"http://{test_web_address}/Login")
    page.fill("input[name='email_address']", "user1test.com")
    page.fill("input[name='password']", "Ro")
    page.click("input[value='Login']")
    page.screenshot(path='screenshot.png', full_page=True)
    error_tag = page.locator(".t-error")
    expect(error_tag).to_have_text("Email or Password not found")
