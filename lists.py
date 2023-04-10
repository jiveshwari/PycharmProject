
lucky_number = [23,43,5,44,33,67,34,98]
friends = ["pheobe","joey","rachel","monica","ross","chandler"]
print(friends)
print(friends[0])
friends[5] = "Janice"
print(friends)

#List Functions
friends.extend(lucky_number)
print(friends)
friends.append(  "YOOOOO")
print(friends)
friends.insert(3,"Richard Burke")
print(friends)
friends.remove("Richard Burke")
print(friends)
friends.clear()
lucky_number.sort()
print(friends)
print(lucky_number)
friends2 = friends.copy()
print(friends2)

#Tupples

coordinates = [(6, 7),(3.545, 2.453)] #Tupple are unchangable
print(coordinates[0])
print(coordinates)



