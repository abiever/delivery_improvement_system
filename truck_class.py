class Truck:
    def __init__(self):
        self.packages = []

    # def __str__(self):  # overwrite print(Movie) otherwise it will print object reference
    #     return "%s, %s, %s, %s, %s" % (self.ID, self.name, self.year, self.price, self.status)

    #will likely need a method that 'removes' a package from the list once it's been delivered

    # TODO: Create addPackage() method to append to packages[]
    def addPackage(self, package):
        self.packages.append(package)

    def printPackageList(self, truckNumber):
        print("List of Packages for Truck #" + str(truckNumber))
        for package in self.packages:
            print(package)