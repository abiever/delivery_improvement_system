import hash_table_class
import package_class
import methods
import csv

# instance of the self-adjusting data structure, followed by loading with data
packageHashTable = hash_table_class.ChainingHashTable()
methods.loadPackageData("WGUPS_package_file.csv", packageHashTable)

distanceDataList = []
methods.loadDistanceData("WGUPS_distance_table.csv", distanceDataList)

# display the hash table data to the console
# print("Package Data from Hashtable:")
# # Fetch data from Hash Table
# for i in range(len(packageHashTable.table)):
#     print("Package: {}".format(packageHashTable.search(i+1)))


print("Distance Data List:")
print(distanceDataList)
# print(distanceDateList[4])
# print(distanceDateList[4][4])

