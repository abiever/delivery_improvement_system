class Movie:
    def __init__(self, ID, name, year, price, status):
        self.ID = ID
        self.name = name
        self.year = year
        self.price = price
        self.status = status

    def __str__(self):  # overwrite print(Movie) otherwise it will print object reference
        return "%s, %s, %s, %s, %s" % (self.ID, self.name, self.year, self.price, self.status)