class Truck:
    def __init__(self, packages):
        #IDEA: Perhaps store the packages as a list here??
        self.packages = [packages]

    def __str__(self):  # overwrite print(Movie) otherwise it will print object reference
        return "%s, %s, %s, %s, %s" % (self.ID, self.name, self.year, self.price, self.status)