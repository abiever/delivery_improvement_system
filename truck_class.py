class Truck:
    def __init__(self, truckNumber):
        self.packages = []
        self.truckNumber = truckNumber
        self.startingAddress = "4001 South 700 East, Salt Lake City, UT 84107"
        #TODO: add a "startingAddress" here set to HUB, then update it as needed when doing NN algorithm steps

    # this method will either append a package to the packages list or print that the list is full
    def addPackage(self, package):
        if len(self.packages) < 16:
            self.packages.append(package)
        else:
            print("Truck is full for Truck #" + str(self.truckNumber) + ". No more packages can be added.")

    def removePackage(self, packageID):
        for package in self.packages:
            if package.getPackageID() == packageID:
                self.packages.remove(package)

    def dropOffPackage(self, packageID, hashTable):
        # TODO: this method needs to both remove the package from the packages list and update the hashtable to say 'delivered' + time
        # TODO: package.setStatus() to "delivered" and set delivery time
        for package in self.packages:
            if package.getPackageID() == packageID:
                package.setStatus("Delivered.")
                # insert/update this specific hashtable entry
                hashTable.insert(package.getPackageID(), package)
                self.packages.remove(package)

    def getPackages(self):
        return self.packages

    # this method prints to the console all packages contained in the truck
    def printPackageList(self):
        print("List of Packages for Truck #" + str(self.truckNumber))
        if len(self.packages) > 0:
            for package in self.packages:
                print(package)
        else:
            print("No packages in Truck #" + str(self.truckNumber))

    def getStartingAddress(self):
        return self.startingAddress

    def setStartingAddress(self, startingAddress):
        self.startingAddress = startingAddress

