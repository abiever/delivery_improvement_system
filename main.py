# Aaron Tandem, Student ID 010169998

import hash_table_class
import truck_class
import methods
from datetime import datetime, time, timedelta


# This method finds and returns how many miles there are between two provided addresses held within a list storing address data.
# It is subsequently used in the minDistanceFrom() method below to sequentially find which two addresses are closest to one another.
def distanceBetween(address1, address2):
    indexAddress1 = addressDataList.index(address1)
    indexAddress2 = addressDataList.index(address2)

    # The 2D list is a series of arrays of i++ size, so 'coordinates' will only work uni-directionally
    # e.x. distanceDataList[3][22] will return an integer representing distance, but distanceDataList[22][3] will throw an exception
    # However, because coordinates should be 'reversible', logic should be provided for cases when a coordinate is 'out-of-bounds'
    # So, this 'flips' the indexes when necessary so that the index reference never exceeds what the Address Data List allows for
    if indexAddress2 > indexAddress1:
        tempIndex = indexAddress1
        flippedIndexAddress1 = indexAddress2
        flippedIndexAddress2 = tempIndex
        return distanceDataList[flippedIndexAddress1][flippedIndexAddress2]

    else:
        return distanceDataList[indexAddress1][indexAddress2]


# This method makes use of the distanceBetween() function above to sequentially find the address of a package in a truck's list that is
# closest to the provided 'fromAddress' (i.e. 'where the truck was last located'). This 'fromAddress' generally always starts at the WGUPS
# HUB located at "4001 South 700 East, Salt Lake City, UT 84107". However, this address is automatically updated to the address of the last
# delivered package in the recursive call of minDistanceFrom() in the deliverTruckPackages() method below. This is a critical part of the
# Nearest Neighbor Greedy Algorithm used by this program to solve WGUPS's package delivery efficiency issues.
def minDistanceFrom(fromAddress, truckPackages):
    minDistance = None
    minDistanceAddress = None
    minDistancePkgID = None

    for i in range(len(truckPackages)):
        # Because no distance has yet been calculated to be smaller than the first one in the truck's list, it defaults to the initial value
        # for minDistance with the initial call of distanceBetween().
        if minDistance is None:
            minDistance = distanceBetween(fromAddress, truckPackages[i].getAddress())

        # Whenever distanceBetween() finds a distance smaller than or equal to the previously initialized minDistance, it sets minDistance
        # to this new distance integer and also sets the minDistanceAddress & minDistancePkgID to the respective address and ID for that
        # related package in the truck's package list.
        if minDistance >= distanceBetween(fromAddress, truckPackages[i].getAddress()):
            minDistance = distanceBetween(fromAddress, truckPackages[i].getAddress())
            minDistanceAddress = truckPackages[i].getAddress()  # will be used to update startingAddress in truck after package delivery
            minDistancePkgID = truckPackages[i].getPackageID()

    # This method returns these three data points in a tuple so that they may be used to continue the Nearest Neighbor algorithm with the
    # deliverTruckPackages() method below.
    return minDistance, minDistanceAddress, minDistancePkgID


# This method is the final part of the Nearest Neighbor algorithm chosen for this project, and the part of the algorithm that
# simultaneously removes (i.e. "delivers") a package from a truck's package list and update's that truck's "startingAddress" as the same
# address of the package that was just removed/delivered.
# The second argument "startTime" must be of format 'time(x, x, x)', including when calling getStartingTime() or getEndingTime() from the
# provided 'truck' argument.
def deliverTruckPackages(truck, startTime):
    totalDistanceTravelled = truck.getTotalDeliveryDistance()  # Initially '0', but will be a different number upon subsequent calls
    speed = 18  # integer representation of miles per hour
    currentTime = datetime.combine(datetime.today(), startTime)

    # This loop will set each package's status to 'en route' upon the truck leaving the HUB.
    for package in truck.getPackages():
        # this setStatus will also automatically update the hash table data structure
        package.setStatus("En route.")

    while len(truck.getPackages()) > 0:
        # This utilizes 'unpacking' to initialize the three variables with the three data points from the tuple returned from the
        # minDistanceFrom() method. Combined with the while loop, these three variables, along with all their processing below leading into
        # truck.dropOffPackage(), are recursively repeated and updated until the length of the truck's package list reaches '0'.
        minDeliveryDistance, minDeliveryAddress, minDeliveryPkgID = minDistanceFrom(truck.getStartingAddress(), truck.getPackages())
        totalDistanceTravelled += minDeliveryDistance

        truck.setStartingAddress(minDeliveryAddress)
        timeSpent = timedelta(hours=(minDeliveryDistance / speed)) # calculates how long it took to get the package's delivery address
        deliveryTime = currentTime + timeSpent # sets deliveryTime as culmination of time taken to get to the delivery destination
        currentTime = deliveryTime  # NEEDED to update functional scope variable with time necessary to continue from after a delivery

        # This 'removes' the package related the algorithmically discovered closest address (minDeliveryAddress), and simultaneously
        # passes along data to update the hash table data structure with the delivery time of that package, along with the package object
        # itself also having its 'timeDelivered' member updated with 'deliveryTime' for further processing during the user interface being
        # used.
        truck.dropOffPackage(minDeliveryPkgID, packageHashTable, deliveryTime.strftime("%H:%M:%S"))

        # Once the length of the truck's list of packages becomes '0', delivery of that truck's packages is finished, so auto-calculation
        # of that truck's return trip back to the HUB is implemented through another call of distanceBetween() using the final delivered
        # package's address and the HUB's. The truck's 'Ending Time' is then set so that this time can be used in subsequent calls of
        # deliverTruckPackages() with either same truck upon reloading or other trucks ready to ship out. The truck's 'Starting Address' is
        # also automatically reset to the HUB's so that deliveries will correctly begin from there again.
        if len(truck.getPackages()) == 0:
            returnTrip = distanceBetween(minDeliveryAddress, "4001 South 700 East, Salt Lake City, UT 84107")
            truck.setTotalDeliveryDistance(totalDistanceTravelled + returnTrip)
            returnTripTime = timedelta(hours=(returnTrip / speed))
            truck.setEndingTime(deliveryTime + returnTripTime)
            truck.setStartingAddress("4001 South 700 East, Salt Lake City, UT 84107")


# This is the instance of the self-adjusting data structure (hash table), followed by a method call to load it with package data
packageHashTable = hash_table_class.ChainingHashTable()
methods.loadPackageData("WGUPS_package_file.csv", packageHashTable)

# This is an empty list data structure that'll hold distances, followed by a method call to load the list with distance data
distanceDataList = []
methods.loadDistanceData("WGUPS_distance_table.csv", distanceDataList)

# This is an empty list data structure that'll hold addresses, followed by a method call to load the list with address data
addressDataList = []
methods.loadAddressData("WGUPS_distance_table.csv", addressDataList)

# Truck 1 will be the first truck to leave the HUB, prioritizing packages that have early deadlines
truck1 = truck_class.Truck(1)  # The constructor of the Truck Class is called to create a new truck object
# Packages are loaded manually by calling the truck's addPackage() along with the hash table's search functionality
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

# Truck 2 will prioritize LATE on arrival packages that still have an early deadline
# NOTE: IT WILL LEAVE @ 9:10am!
truck2 = truck_class.Truck(2)
# packages 3, 18, 36, 38 must all be on Truck #2
truck2.addPackage(packageHashTable.search(3))
truck2.addPackage(packageHashTable.search(18))
truck2.addPackage(packageHashTable.search(36))
truck2.addPackage(packageHashTable.search(38))
# Truck 2 PRIORITY packages:
truck2.addPackage(packageHashTable.search(6))
truck2.addPackage(packageHashTable.search(25))
truck2.addPackage(packageHashTable.search(33))
truck2.addPackage(packageHashTable.search(12))
truck2.addPackage(packageHashTable.search(23))
truck2.addPackage(packageHashTable.search(24))
truck2.addPackage(packageHashTable.search(26))
truck2.addPackage(packageHashTable.search(27))

# deliverTruckPackages() method calls to send out Trucks 1 and 2
deliverTruckPackages(truck1, time(8, 0, 0))
deliverTruckPackages(truck2, time(9, 10, 0))

# Truck 3 will deliver the remaining packages that have no explicit deadline priority
truck3 = truck_class.Truck(3)
# PACKAGES FOR FINAL SHIPMENT
truck3.addPackage(packageHashTable.search(9))
truck3.getPackages()[0].setAddress("410 S State St")  # UPDATES Package #9 with the correct address
truck3.addPackage(packageHashTable.search(28))
truck3.addPackage(packageHashTable.search(32))
truck3.addPackage(packageHashTable.search(2))
truck3.addPackage(packageHashTable.search(4))
truck3.addPackage(packageHashTable.search(5))
truck3.addPackage(packageHashTable.search(39))
truck3.addPackage(packageHashTable.search(21))
truck3.addPackage(packageHashTable.search(22))
truck3.addPackage(packageHashTable.search(7))
truck3.addPackage(packageHashTable.search(8))
truck3.addPackage(packageHashTable.search(10))
truck3.addPackage(packageHashTable.search(11))
truck3.addPackage(packageHashTable.search(35))
truck3.addPackage(packageHashTable.search(17))
truck3.addPackage(packageHashTable.search(19))

# Method call of deliverTruckPackages() that sends Truck 3 off at the same time the driver for Truck 2 arrives back at HUB
deliverTruckPackages(truck3, truck2.getEndingTime().time())

# print("lookup function test:")
# print(methods.hashTableLookUp(packageHashTable, 38))
# print(methods.hashTableLookUp(packageHashTable, 7))


if __name__ == "__main__":
    while True:
        methods.displayMenu()

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            # display the hash table data to the console
            print("PackageID, Address, City, State, Zip, Delivery Deadline, Kilograms, Status, DeliveryTime")
            # Fetch data from Hash Table and then print it
            for i in range(len(packageHashTable.table)):
                print("{}".format(packageHashTable.search(i + 1)))
            print("Distance Traveled for Truck #1: " + str(round(truck1.getTotalDeliveryDistance(), 1)) + " miles.")
            print("Distance Traveled for Truck #2: " + str(round(truck2.getTotalDeliveryDistance(), 1)) + " miles.")
            print("Distance Traveled for Truck #3: " + str(round(truck3.getTotalDeliveryDistance(), 1)) + " miles.")
            print("Cumulative Distance for All Trucks: " +
                  str(round(truck1.getTotalDeliveryDistance(), 1) +
                      round(truck2.getTotalDeliveryDistance(), 1) +
                      round(truck3.getTotalDeliveryDistance(), 1)
                      ) + " miles."
                  )
        elif choice == "2":
            inputID = int(input("Enter packageID (1-40): "))
            inputTimeStr = input("Enter time (hh, mm, ss):")

            # Split the input string into individual components
            hour, minute, second = map(int, inputTimeStr.split(','))
            inputTime = time(hour, minute, second)

            foundPkg = packageHashTable.search(inputID)

            if foundPkg is not None:
                foundPkgDateTime = datetime.strptime(foundPkg.getTimeDelivered(), "%H:%M:%S")
                foundPkgTime = foundPkgDateTime.time()

                if inputTime >= foundPkgTime:
                    print(f"Package {inputID} was " + foundPkg.getStatus() + " at " + foundPkg.getTimeDelivered() + " to " +
                          foundPkg.getAddress() + ".")
                elif inputTime < foundPkgTime and inputTime >= time(8, 0, 0):
                    print(f"Package {inputID} is en route as of {inputTime}" + ".")
                elif inputTime < time(8, 0, 0):
                    print(f"Package {inputID} is at HUB preparing for delivery. Deliveries will begin promptly at 8 am.")
            else:
                print(f"Cannot find package with ID '{inputID}'. Please enter a valid ID and try again.")
        elif choice == "3":
            inputTimeStr = input("Enter time (hh, mm, ss):")

            # Split the input string into individual components
            hour, minute, second = map(int, inputTimeStr.split(','))
            inputTime = time(hour, minute, second)

            print(f"Delivery Status for All Packages as of {inputTime}:")
            for i in range(len(packageHashTable.table)):
                foundPkg = packageHashTable.search(i + 1)
                foundPkgDateTime = datetime.strptime(foundPkg.getTimeDelivered(), "%H:%M:%S")
                foundPkgTime = foundPkgDateTime.time()
                if inputTime >= foundPkgTime:
                    print(f"Package {i + 1} was " + foundPkg.getStatus() + " at " + foundPkg.getTimeDelivered() + " to " +
                          foundPkg.getAddress() + ".")
                elif inputTime < foundPkgTime and inputTime >= time(8, 0, 0):
                    print(f"Package {i + 1} is en route as of {inputTime}" + ".")
                elif inputTime < time(8, 0, 0):
                    print(f"Package {i + 1} is at HUB preparing for delivery. Deliveries will begin promptly at 8 am.")

        elif choice == "4":
            print("Thank you for using WGUPS. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
