import hash_table_class
import truck_class
import methods

# instance of the self-adjusting data structure, followed by a method call to load it with package data
packageHashTable = hash_table_class.ChainingHashTable()
methods.loadPackageData("WGUPS_package_file.csv", packageHashTable)

# a list ADT to hold distances, followed by a method call to load the list with data
distanceDataList = []
methods.loadDistanceData("WGUPS_distance_table.csv", distanceDataList)

addressDataList = []
methods.loadAddressData("WGUPS_distance_table.csv", addressDataList)

# firstAddress = '2835 Main St'
# index1 = addressDataList.index(firstAddress)
#
# secondAddress = '3060 Lester St'
# index2 = addressDataList.index(secondAddress)
#
# print("Address Data List Index of String Value:")
# print(index1)
# print(index2)
#
# print("Output of distanceBetween Function for:", firstAddress, "to", secondAddress)
# print(methods.distanceBetween(firstAddress, secondAddress, addressDataList, distanceDataList))
#
# print("Output of distanceBetween Function for:", secondAddress, "to", firstAddress)
# print(methods.distanceBetween(secondAddress, firstAddress, addressDataList, distanceDataList))

truck1 = truck_class.Truck(1)
truck1.addPackage(packageHashTable.search(1))
truck1.addPackage(packageHashTable.search(20))
truck1.printPackageList()

truck2 = truck_class.Truck(2)
truck2.addPackage(packageHashTable.search(3))
truck2.addPackage(packageHashTable.search(18))
truck2.addPackage(packageHashTable.search(36))
truck2.addPackage(packageHashTable.search(38))
truck2.printPackageList()

truck1.removePackage(1)
truck1.printPackageList()
truck1.removePackage(20)
truck1.printPackageList()

truck2.removePackage(18)
truck2.printPackageList()
# print("Output from distanceDataList:", index1, "-", index2)
# print(distanceDataList[index1][index2])

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
