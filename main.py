import hash_table_class
import csv



bestMovies = [
    [1, "CITIZEN KANE - 1941"],
    [2, "CASABLANCA - 1942"],
    [3, "THE GODFATHER - 1972"],
    [4, "GONE WITH THE WIND - 1939"],
    [5, "LAWRENCE OF ARABIA - 1962"],
    [6, "THE WIZARD OF OZ - 1939"],
    [7, "THE GRADUATE - 1967"],
    [8, "ON THE WATERFRONT- 1954"],
    [9, "SCHINDLER'S LIST -1993"],
    [10, "SINGIN' IN THE RAIN - 1952"],
    [11, "STAR WARS - 1977"]
]

myHash = hash_table_class.ChainingHashTable()

print("\nInsert:")
for movie in bestMovies:
    movie_id, movie_title = movie[0], movie[1]
    myHash.insert(movie_id, movie_title)

print(myHash.table)

print("\nSearch:")
print(myHash.search(1))  # Key=1, item="CITIZEN KANE - 1941"
print(myHash.search(11))  # Key=11, item="STAR WARS - 1977"; so same bucket and Chainin is working

print("\nUpdate:")
myHash.insert(1, "Star Trek - 1979")  # 2nd bucket; Key=1, item="Star Trek - 1979"
print(myHash.table)

print("\nRemove:")
myHash.remove(1)  # Key=1, item="Star Trek - 1979" to remove
print(myHash.table)

myHash.remove(11)  # Key=11, item="STAR WARS - 1977" to remove
print(myHash.table)

myHash.remove(10)  # Key=11, item="STAR WARS - 1977" to remove
print(myHash.table)

print("\nUpdate:")
myHash.insert(10, "Space Balls - 1983")  # 2nd bucket; Key=1, item="Star Trek - 1979"
print(myHash.table)
