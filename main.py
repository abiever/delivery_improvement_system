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


def deliverTruckPackages(truck):
    # TODO: Potentially set this as truck.etc(), update the flow of logic, so we can get() times whenever? This might be necessary to
    #  send trucks off at specific times
    totalDistanceTravelled = 0
    speed = 18  # miles per hour
    currentTime = datetime.combine(datetime.today(), time(8, 0, 0))

    for package in truck.getPackages():
        # this appears to automatically update the hash table
        package.setStatus("Out for delivery as of " + currentTime.strftime("%H:%M:%S"))
        # truck.printPackageList() # This is just to help check time inputs

    while len(truck.getPackages()) > 0:
        minDeliveryDistance, minDeliveryAddress, minDeliveryPkgID = minDistanceFrom(truck.getStartingAddress(), truck.getPackages())
        totalDistanceTravelled += minDeliveryDistance
        truck.setStartingAddress(minDeliveryAddress)
        timeSpent = timedelta(hours=(minDeliveryDistance / speed))
        deliveryTime = currentTime + timeSpent
        currentTime = deliveryTime #  MUST include to update functional scope variable with time necessary to continue from
        # after a delivery
        truck.dropOffPackage(minDeliveryPkgID, packageHashTable, deliveryTime.strftime("%H:%M:%S"))

        print("Truck Package List Length:", len(truck.getPackages()))
        print("Deliverable PkgID:", minDeliveryPkgID)
        print("Minimum Address:", minDeliveryAddress)
        print("Current Time:", deliveryTime)
        print("Current Distance Travelled:", totalDistanceTravelled)

        if len(truck.getPackages()) == 0:
            truck.setTotalDeliveryDistance(totalDistanceTravelled)

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

truck1 = truck_class.Truck(1)
truck1.addPackage(packageHashTable.search(1))
truck1.addPackage(packageHashTable.search(2))
truck1.addPackage(packageHashTable.search(4))
truck1.addPackage(packageHashTable.search(5))
truck1.addPackage(packageHashTable.search(7))
truck1.addPackage(packageHashTable.search(8))
truck1.addPackage(packageHashTable.search(10))
truck1.addPackage(packageHashTable.search(11))
truck1.addPackage(packageHashTable.search(12))
# packages 13, 14, 15, 16, 19, 20 must all be delivered together
truck1.addPackage(packageHashTable.search(13))
truck1.addPackage(packageHashTable.search(14))
truck1.addPackage(packageHashTable.search(15))
truck1.addPackage(packageHashTable.search(16))
truck1.addPackage(packageHashTable.search(17))
truck1.addPackage(packageHashTable.search(19))
truck1.addPackage(packageHashTable.search(20))

# print("Truck 1 packages BEFORE delivery:")
# truck1.printPackageList()
#
# print("Minimum distance for Packages in Truck #1:")
# print(minDistanceFrom(truck1.getStartingAddress(), truck1.getPackages()))

truck2 = truck_class.Truck(2)
# packages 3, 18, 36, 38 must all be on Truck #2
truck2.addPackage(packageHashTable.search(3))
truck2.addPackage(packageHashTable.search(18))
truck2.addPackage(packageHashTable.search(36))
truck2.addPackage(packageHashTable.search(38))
# print("Minimum distance for Packages in Truck #2:")
# print(minDistanceFrom(truck2.getStartingAddress(), truck2.getPackages()))

print("deliverTruckPackages() Test:")
deliverTruckPackages(truck1)
deliverTruckPackages(truck2)

print("Truck 1 packages AFTER delivery:")
truck1.printPackageList()

print("Total Distance Travelled for Truck #1 test:")
print(truck1.getTotalDeliveryDistance())
print("Total Distance Travelled for Truck #2 test:")
print(truck2.getTotalDeliveryDistance())

print("lookup function test:")
print(methods.hashTableLookUp(packageHashTable, 38))
print(methods.hashTableLookUp(packageHashTable, 7))

# display the hash table data to the console
print("Package Data from Hashtable (after):")
# Fetch data from Hash Table
for i in range(len(packageHashTable.table)):
    print("Package: {}".format(packageHashTable.search(i + 1)))
