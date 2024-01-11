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
    return distanceDataList[addressDataList.index(address1)][addressDataList.index(address2)]

index1 = addressDataList.index('3365 S 900 W')
index2 = addressDataList.index('177 W Price Ave')

print("Address Data List Index of String Value:")
print(index1)
print(index2)

print("Output of distanceBetween Function:")
print(distanceBetween('3365 S 900 W', '177 W Price Ave'))

print("Output from distanceDataList:")
print(distanceDataList[index1][index2])

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
