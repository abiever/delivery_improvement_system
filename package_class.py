# "Package ID",Address,City,State,Zip,"Delivery Deadline","Weight KILO","Special Notes",

class Package:
    def __init__(self, ID, address, city, state, zip, deadline, weight, status):
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.status = status

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s" % (self.ID, self.address, self.city, self.state,
        self.zip, self.deadline, self.weight, self.status)

    # may need getters for each member, but 'getAddress()' is likely most important
    def getPackageID(self):
        return self.ID

