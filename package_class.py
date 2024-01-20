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
        self.timeDelivered = "N/A"

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.ID, self.address, self.city, self.state,
        self.zip, self.deadline, self.weight, self.status, self.timeDelivered)

    def getPackageID(self):
        return self.ID

    def getAddress(self):
        return self.address

    def setAddress(self, address):
        self.address = address

    def getCity(self):
        return self.city

    def getZip(self):
        return self.zip

    def getDeadline(self):
        return self.deadline

    def getWeight(self):
        return self.weight

    def getStatus(self):
        return self.status

    def setStatus(self, newStatus):
        self.status = newStatus

    def setTimeDelivered(self, timeDelivered):
        self.timeDelivered = timeDelivered

    def getTimeDelivered(self):
        return self.timeDelivered

