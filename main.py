import hash_table_class
import methods

# instance of the self-adjusting data structure, followed by a method call to load it with package data
packageHashTable = hash_table_class.ChainingHashTable()
methods.loadPackageData("WGUPS_package_file.csv", packageHashTable)

# a list ADT to hold distances, followed by a method call to load the list with data
distanceDataList = []
methods.loadDistanceData("WGUPS_distance_table.csv", distanceDataList)

addressDataList = []
methods.loadAddressData("WGUPS_distance_table.csv", addressDataList)

def distanceBetween(address1, address2):
    return distanceDataList[address1][address2]

print("Address Data List Index of String Value:")
print(addressDataList.index('Salt Lake County/United Police Dept 3365 S 900 W'))

# print(distanceBetween(1, 1))

# print(distanceDataList[4][2])

# display the hash table data to the console
# print("Package Data from Hashtable:")
# # Fetch data from Hash Table
# for i in range(len(packageHashTable.table)):
#     print("Package: {}".format(packageHashTable.search(i+1)))

# print("Distance Data List:")
# print(len(distanceDataList))
# print(distanceDataList)
#
# print("Address Data List:")
# print(len(addressDataList))
# print(addressDataList)
