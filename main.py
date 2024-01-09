import hash_table_class
import package_class
import csv

# instance of the self-adjusting data structure
packageHashTable = hash_table_class.ChainingHashTable()

# this function reads through the WGUPS package CVS file, then 'loads' it into the hash table
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

            # creates new Package object
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

            # inserts newly created Package object into the hash table with its unique ID
            packageHashTable.insert(packageID, newPackage)


distanceDateList = []
def loadDistanceData(fileName):
    with open(fileName, newline='') as distanceDataCSV:
        distanceData = csv.reader(distanceDataCSV, delimiter=',', dialect='unix')
        next(distanceData)  # this skips the header??
        next(distanceData) # having these here makes a difference TODO: use this to help create AddressList?
        # loop through the distanceDataCSV and add  the data to distanceDataList one row at a time
        for distanceInfo in distanceData:
            distanceDateList.append(distanceInfo)


loadPackageData("WGUPS_package_file.csv")
loadDistanceData("WGUPS Distance Table - Sheet1.csv")

print("Package Data from Hashtable:")
# Fetch data from Hash Table
for i in range(len(packageHashTable.table)):
    print("Package: {}".format(packageHashTable.search(i+1)))

print("An Increasing 2D List:")
i = 1
maxRows = 10
arr = []
while i < maxRows:
    arr.append([0 for i in range(i)])
    # print(arr)
    i += 1
print(arr)
arr[1][1] = 5
arr[4][3] = 'alex'
arr[6][0] = 783
print(arr)

print("Distance Data List:")
print(distanceDateList)
# print(distanceDateList[4])
# print(distanceDateList[4][4])

