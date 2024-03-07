from lib.space import Space


class SpaceRepository:
    def __init__(self, connection):
        self._connection = connection 

    def all(self):
        rows = self._connection.execute("SELECT * FROM spaces")
        spaces = []
        for row in rows:
            space = Space(
                row["id"], 
                row["name"],
                row["description"],
                row["price"],
                row["date_from"],
                row["date_to"],
                row["user_id"],
                row["image_url"]
                )
            spaces.append(space)
        return spaces
    
    def find(self, id):
        rows = self._connection.execute("SELECT * FROM spaces WHERE id =%s", [id])
        row = rows[0]
        return Space(row["id"], row["name"], row["description"], row["price"], row["date_from"], row["date_to"], row["user_id"], row["image_url"])


    
    def create(self, space):
        formatted_dates = [date.strftime('%Y-%m-%d') for date in space.available_dates]
        rows = self._connection.execute(
            'INSERT INTO spaces (name, description, price, date_from, date_to, user_id, image_url, available_dates) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING id',
            [space.name, space.description, round(float(space.price), 2), space.date_from, space.date_to, space.user_id, space.image_url, formatted_dates]
            )
        row = rows[0]
        space.id = row["id"]
        return None


    def select_date(self, id, requested_date):
        rows = self._connection.execute("SELECT available_dates FROM spaces WHERE id =%s", [id])
        for element in rows:
            dates = list(element.values())
            print(dates[0])
        available_dates = dates[0]
        print(type(rows)) 
        print("HERE!!!!!!!!!!")
        print(rows)
        # for row in rows:
        #     if row == 
        