import csvimport package_class# this method is used to ascertain whether values passed to it are valid floatsdef is_float(value):    try:        float(value)        return True    except ValueError:        return False# this function reads through the WGUPS package CVS file, then 'loads' it into the hash tabledef loadPackageData(fileName, hashTable):    with open(fileName, newline='') as packageDataCSV:        packageData = csv.reader(packageDataCSV, delimiter=',')        next(packageData)  # this skips the header        for packageInfo in packageData:            packageID = int(packageInfo[0])            packageAddress = packageInfo[1]            packageCity = packageInfo[2]            packageState = packageInfo[3]            packageZIP = packageInfo[4]            packageDeadline = packageInfo[5]            packageWeight = packageInfo[6]            packageStatus = "at hub"            # creates new Package object            newPackage = package_class.Package(                packageID,                packageAddress,                packageCity,                packageState,                packageZIP,                packageDeadline,                packageWeight,                packageStatus            )            # inserts newly created Package object into a previously defined hash table with its unique ID            hashTable.insert(packageID, newPackage)# this function reads through a provided file containing distance data, parses its, then loads it into the provided listdef loadDistanceData(fileName, list):    with open(fileName, newline='') as distanceDataCSV:        distanceData = csv.reader(distanceDataCSV, delimiter=',', dialect='unix')        # loops through the distanceDataCSV and appends only the necessary distance data to distanceDataList one row at a time        for distanceInfo in distanceData:            filtered_row = [float(value) for value in distanceInfo if (value != '' and is_float(value))]            if len(filtered_row) != 0:                list.append(filtered_row)# this function reads through a provided file containing address data, parses its, then loads it into the provided listdef loadAddressData(fileName, list):    with open(fileName, newline='') as addressDataCSV:        addressData = csv.reader(addressDataCSV, delimiter=',', dialect='unix')        for addressInfo in addressData:            # This isn't ideal, but it gets the job done by only appending the data from arrays that DON'T have floats            # in them and only have a length of 2. Appends just the first element which is the necessary address            if not any(isinstance(element, float) for element in addressInfo) and len(addressInfo) == 2:                list.append(addressInfo[0])