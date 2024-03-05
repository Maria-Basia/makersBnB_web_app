from playwright.sync_api import Page, expect

# Tests for your routes go here


def test_get_all_spaces(page, test_web_address, db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    page.goto(f"http://{test_web_address}/index")
    li_tags = page.locator("li")
    expect(li_tags).to_have_text([
        "Name: space_1 Price per night: £45.5 Description: description_1",
        "Name: space_2 Price per night: £14000.99 Description: description_2"
    ])

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
    page.goto(f"http://{test_web_address}/new")
    page.click("text='Add new listing'")

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