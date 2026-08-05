#weight on the moon and earth assignment  
mass = int(input("Enter mass of the object: "))
earth_gravity = 9.8
moon_gravity = 1.62
wgtearth = mass * earth_gravity
wgtmoon = mass * moon_gravity
print("The weight of object on earth is: ",wgtearth)
print("The weight of object on moon is: ",wgtmoon)
print("Identifiers: earth_gravity and moon_gravity")
print("Operation used: Multiplication")
print("datatype of mass: ",type(mass))
