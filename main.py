# Aaron Tandem, Student ID 010169998

import hash_table_class
import truck_class
import methods
from datetime import datetime, time, timedelta


def distanceBetween(address1, address2):
    indexAddress1 = addressDataList.index(address1)
    indexAddress2 = addressDataList.index(address2)

    # because our 2D list is a series of arrays of i++ size, 'coordinates' will only work unidirectionally
    # because coordinates should be reversible, logic should be provided to account for such cases
    # So, this 'flips' the indexes so that the index reference never exceeds the ADT bounds
    if indexAddress2 > indexAddress1:
        tempIndex = indexAddress1
        flippedIndexAddress1 = indexAddress2
        flippedIndexAddress2 = tempIndex
        return distanceDataList[flippedIndexAddress1][flippedIndexAddress2]

    else:
        return distanceDataList[indexAddress1][indexAddress2]


def minDistanceFrom(fromAddress, truckPackages):
    minDistance = None
    minDistanceAddress = None
    minDistancePkgID = None

    for i in range(len(truckPackages)):

        if minDistance is None:
            minDistance = distanceBetween(fromAddress, truckPackages[i].getAddress())

        if minDistance >= distanceBetween(fromAddress, truckPackages[i].getAddress()):
            minDistance = distanceBetween(fromAddress, truckPackages[i].getAddress())
            minDistanceAddress = truckPackages[
                i].getAddress()  # return this and use it to update startingAddress in truck
            minDistancePkgID = truckPackages[i].getPackageID()

    return minDistance, minDistanceAddress, minDistancePkgID


#  startTime should be format time(x, x, x) or truck.getStartingTime?
def deliverTruckPackages(truck, startTime):
    totalDistanceTravelled = truck.getTotalDeliveryDistance()
    speed = 18  # miles per hour
    currentTime = datetime.combine(datetime.today(), startTime)

    for package in truck.getPackages():
        # this appears to automatically update the hash table
        package.setStatus("Out for delivery as of " + currentTime.strftime("%H:%M:%S"))
        # truck.printPackageList() # This is just to help check time inputs

    while len(truck.getPackages()) > 0:
        minDeliveryDistance, minDeliveryAddress, minDeliveryPkgID = minDistanceFrom(truck.getStartingAddress(),
                                                                                    truck.getPackages())
        totalDistanceTravelled += minDeliveryDistance
        truck.setStartingAddress(minDeliveryAddress)
        timeSpent = timedelta(hours=(minDeliveryDistance / speed))
        deliveryTime = currentTime + timeSpent
        currentTime = deliveryTime  # MUST include to update functional scope variable with time necessary to continue from
        # after a delivery
        truck.dropOffPackage(minDeliveryPkgID, packageHashTable, deliveryTime.strftime("%H:%M:%S"))

        print("Truck Package List Length:", len(truck.getPackages()))
        print("Deliverable PkgID:", minDeliveryPkgID)
        print("Minimum Address:", minDeliveryAddress)
        print("Current Time:", deliveryTime)
        print("Current Distance Travelled:", totalDistanceTravelled)

        #  brings truck back to HUB, adds time & distance to do so, resets startingAddress
        if len(truck.getPackages()) == 0:
            returnTrip = distanceBetween(minDeliveryAddress, "4001 South 700 East, Salt Lake City, UT 84107")
            truck.setTotalDeliveryDistance(totalDistanceTravelled + returnTrip)
            returnTripTime = timedelta(hours=(returnTrip / speed))
            truck.setEndingTime(deliveryTime + returnTripTime)
            truck.setStartingAddress("4001 South 700 East, Salt Lake City, UT 84107")


# instance of the self-adjusting data structure, followed by a method call to load it with package data
packageHashTable = hash_table_class.ChainingHashTable()
methods.loadPackageData("WGUPS_package_file.csv", packageHashTable)

# a list ADT to hold distances, followed by a method call to load the list with distance data
distanceDataList = []
methods.loadDistanceData("WGUPS_distance_table.csv", distanceDataList)

# a list ADT to hold addresses, followed by a method call to load the list with address data
addressDataList = []
methods.loadAddressData("WGUPS_distance_table.csv", addressDataList)

print("Package Data from Hashtable (before):")
# Fetch data from Hash Table
for i in range(len(packageHashTable.table)):
    print("Package: {}".format(packageHashTable.search(i + 1)))

# Truck 1 will be the first truck to leave the HUB, prioritizing packages that have deadlines
truck1 = truck_class.Truck(1)
truck1.addPackage(packageHashTable.search(1))
# packages 13, 14, 15, 16, 19, 20 must all be delivered together
truck1.addPackage(packageHashTable.search(13))
truck1.addPackage(packageHashTable.search(14))
truck1.addPackage(packageHashTable.search(15))
truck1.addPackage(packageHashTable.search(16))
truck1.addPackage(packageHashTable.search(20))
# other packages
truck1.addPackage(packageHashTable.search(29))
truck1.addPackage(packageHashTable.search(30))
truck1.addPackage(packageHashTable.search(31))
truck1.addPackage(packageHashTable.search(34))
truck1.addPackage(packageHashTable.search(37))
truck1.addPackage(packageHashTable.search(40))
# EOD packages
truck1.addPackage(packageHashTable.search(23))
truck1.addPackage(packageHashTable.search(24))
truck1.addPackage(packageHashTable.search(26))
truck1.addPackage(packageHashTable.search(27))

#  truck 2 will prioritize LATE packages that still have an early deadline
#  WILL LEAVE @ 9:10am!
truck2 = truck_class.Truck(2)
# packages 3, 18, 36, 38 must all be on Truck #2
truck2.addPackage(packageHashTable.search(3))
truck2.addPackage(packageHashTable.search(18))
truck2.addPackage(packageHashTable.search(36))
truck2.addPackage(packageHashTable.search(38))
# Truck 2 PRIORITY packages:
truck2.addPackage(packageHashTable.search(6))
truck2.addPackage(packageHashTable.search(25))
# EOD packages
truck2.addPackage(packageHashTable.search(33))
truck2.addPackage(packageHashTable.search(35))
truck2.addPackage(packageHashTable.search(21))
truck2.addPackage(packageHashTable.search(22))


# can only be loaded after 10:20am to "410 S State St"
# 9

print("deliverTruckPackages() Test Truck #1:")
deliverTruckPackages(truck1, time(8, 0, 0))
print("deliverTruckPackages() Test Truck #2:")
deliverTruckPackages(truck2, time(9, 10, 0))

print("Truck 1 packages AFTER delivery:")
truck1.printPackageList()
print("Truck 2 packages AFTER delivery:")
truck2.printPackageList()

print("Total Distance Travelled and ending time for Truck #1 test:")
print(truck1.getTotalDeliveryDistance(), truck1.getEndingTime())
print("Total Distance Travelled and ending time for Truck #2 test:")
print(truck2.getTotalDeliveryDistance(), truck2.getEndingTime())

# Truck 3 will deliver the remaining packages that have no explicit deadline priority
truck3 = truck_class.Truck(3)
#  PACKAGES FOR FINAL SHIPMENT
truck3.addPackage(packageHashTable.search(9))
truck3.getPackages()[0].setAddress("410 S State St")
truck3.addPackage(packageHashTable.search(28))
truck3.addPackage(packageHashTable.search(32))
truck3.addPackage(packageHashTable.search(2))
truck3.addPackage(packageHashTable.search(4))
truck3.addPackage(packageHashTable.search(5))
truck3.addPackage(packageHashTable.search(39))
truck2.addPackage(packageHashTable.search(21))
truck2.addPackage(packageHashTable.search(22))
truck3.addPackage(packageHashTable.search(7))
truck3.addPackage(packageHashTable.search(8))
truck3.addPackage(packageHashTable.search(10))
truck3.addPackage(packageHashTable.search(11))
truck3.addPackage(packageHashTable.search(12))
truck3.addPackage(packageHashTable.search(17))
truck3.addPackage(packageHashTable.search(19))

print("deliverTruckPackages() Test Truck #3:")
# sends truck3 off at the same time the driver for truck2 arrives back at HUB
deliverTruckPackages(truck3, truck2.getEndingTime().time())

print("Truck 3 packages AFTER delivery:")
truck3.printPackageList()

print("Total Distance Travelled and ending time for Truck #3 test:")
print(truck3.getTotalDeliveryDistance(), truck3.getEndingTime())

print("Total Distance for ALL trucks:")
print(
    str(truck1.getTotalDeliveryDistance() + truck2.getTotalDeliveryDistance() + truck3.getTotalDeliveryDistance()) + " miles.")

# print("lookup function test:")
# print(methods.hashTableLookUp(packageHashTable, 38))
# print(methods.hashTableLookUp(packageHashTable, 7))

# display the hash table data to the console
print("Package Data from Hashtable (after):")
# Fetch data from Hash Table
for i in range(len(packageHashTable.table)):
    print("Package: {}".format(packageHashTable.search(i + 1)))
