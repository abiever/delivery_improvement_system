import hash_table_class
import truck_class
import methods

# instance of the self-adjusting data structure, followed by a method call to load it with package data
packageHashTable = hash_table_class.ChainingHashTable()
methods.loadPackageData("WGUPS_package_file.csv", packageHashTable)

# a list ADT to hold distances, followed by a method call to load the list with distance data
distanceDataList = []
methods.loadDistanceData("WGUPS_distance_table.csv", distanceDataList)

# a list ADT to hold addresses, follwed by a method call to load the list with address data
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

truck2 = truck_class.Truck(2)
# packages 3, 18, 36, 38 must all be on Truck #2
truck2.addPackage(packageHashTable.search(3))
truck2.addPackage(packageHashTable.search(18))
truck2.addPackage(packageHashTable.search(36))
truck2.addPackage(packageHashTable.search(38))
truck2.printPackageList()

print("lookup function test:")
print(methods.hashTableLookUp(packageHashTable, 38))

# display the hash table data to the console
# print("Package Data from Hashtable:")
# # Fetch data from Hash Table
# for i in range(len(packageHashTable.table)):
#     print("Package: {}".format(packageHashTable.search(i+1)))

# print("Distance Data List:")
# print("Length:", len(distanceDataList))
# print(distanceDataList)

# print("Address Data List:")
# print("Length:", len(addressDataList))
# for i in range(len(addressDataList)):
#     print(addressDataList[i])
