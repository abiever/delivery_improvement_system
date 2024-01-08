import hash_table_class
import package_class
import csv

# "Package ID",Address,City,State,Zip,"Delivery Deadline","Weight KILO","Special Notes",
    
# TODO: Use this to get csv data loaded into hash table?
def loadPackageData(fileName):
    with open(fileName, newline='') as packageDataCSV:
        packageData = csv.reader(packageDataCSV, delimiter=',')
        next(packageData)  # this skips the header
        for packageInfo in packageData:
            packageID = int(packageInfo[0])
            packageAddress = packageInfo[1]
            packageCity = packageInfo[2]
            packageState = packageInfo[3]
            packageZIP = packageInfo[4]
            packageDeadline = packageInfo[5]
            packageWeight = packageInfo[6]
            packageStatus = "at hub"

            # movie object
            newPackage = package_class.Package(
                packageID,
                packageAddress,
                packageCity,
                packageState,
                packageZIP,
                packageDeadline,
                packageWeight,
                packageStatus
            )
            # print(m)

            # insert it into the hash table
            packageHashTable.insert(packageID, newPackage)


packageHashTable = hash_table_class.ChainingHashTable()

loadPackageData("WGUPS_package_file.csv")

print(packageHashTable.table.)

'''
print("Package Data from Hashtable:")
# Fetch data from Hash Table
for i in range(len(packageHashTable)+1):
    print("Movie: {}".format(packageHashTable.search(i+1))) 
'''