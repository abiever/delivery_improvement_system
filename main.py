import hash_table_class
import truck_class
import methods

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

    for i in range(len(truckPackages)):
        if minDistance is None:
            minDistance = distanceBetween(fromAddress, truckPackages[i].getAddress())
        if minDistance < distanceBetween(fromAddress, truckPackages[i].getAddress()):
            minDistance = distanceBetween(fromAddress, truckPackages[i].getAddress())

    return minDistance
    #TODO: use a combination of distanceBetween and getAddress() from packages in trucks to find min distance


# instance of the self-adjusting data structure, followed by a method call to load it with package data
packageHashTable = hash_table_class.ChainingHashTable()
methods.loadPackageData("WGUPS_package_file.csv", packageHashTable)

# a list ADT to hold distances, followed by a method call to load the list with distance data
distanceDataList = []
methods.loadDistanceData("WGUPS_distance_table.csv", distanceDataList)

# a list ADT to hold addresses, followed by a method call to load the list with address data
addressDataList = []
methods.loadAddressData("WGUPS_distance_table.csv", addressDataList)

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
truck1.printPackageList()
truck1Packages = truck1.getPackages()
# this appears to successfully be getting the appropriate address and printing it out as needed
# print(truck1Packages[8].getAddress())
# print(truck1Packages[10].getAddress())
# print("Distance between two addresses in Truck #1:")
# print(distanceBetween(truck1Packages[8].getAddress(), truck1Packages[10].getAddress()))
print(minDistanceFrom(truck1.getStartingAddress(), truck1.getPackages()))

#TODO: 1) Try to getAddress() from two truck packages, then get the distance between these 2 addresses using distanceBetween()
#TODO: 2) If successsful, create algorithm to automatically do this NN-style with minDistance() method


# truck2 = truck_class.Truck(2)
# # packages 3, 18, 36, 38 must all be on Truck #2
# truck2.addPackage(packageHashTable.search(3))
# truck2.addPackage(packageHashTable.search(18))
# truck2.addPackage(packageHashTable.search(36))
# truck2.addPackage(packageHashTable.search(38))
# truck2.printPackageList()

# print("lookup function test:")
# print(methods.hashTableLookUp(packageHashTable, 38))

# display the hash table data to the console
# print("Package Data from Hashtable:")
# # Fetch data from Hash Table
# for i in range(len(packageHashTable.table)):
#     print("Package: {}".format(packageHashTable.search(i+1)))

print("Distance Data List:")
print("Length:", len(distanceDataList))
print(distanceDataList)

# print("Address Data List:")
# print("Length:", len(addressDataList))
# for i in range(len(addressDataList)):
#     print(addressDataList[i])
