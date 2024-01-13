class Truck:
    def __init__(self, truckNumber):
        self.packages = []
        self.truckNumber = truckNumber

    # def __str__(self):  # overwrite print(Movie) otherwise it will print object reference
    #     return "%s, %s, %s, %s, %s" % (self.ID, self.name, self.year, self.price, self.status)

    #will likely need a method that 'removes' a package from the list once it's been delivered

    # this method will either append a package to the packages list or print that the list is full
    def addPackage(self, package):
        if len(self.packages) < 16:
            self.packages.append(package)
        else:
            print("Truck is full for" + str(self.truckNumber) + "No more packages can be added.")

    def removePackage(self, packageID):
        # TODO: this method needs to both remove the package from the packages list and update the
        for package in self.packages:
            if package.getPackageID() == packageID:
                self.packages.remove(package)

    # this method prints to the console all packages contained in the truck
    def printPackageList(self):
        print("List of Packages for Truck #" + str(self.truckNumber))
        if len(self.packages) > 0:
            for package in self.packages:
                print(package)
        else:
            print("No packages in Truck #" + str(self.truckNumber))

