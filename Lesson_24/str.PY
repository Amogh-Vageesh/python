class vehicle:

    def __init__(self,type,color,speed):
        self.color = color
        self.type = type
        self.speed = speed

    def mileage(self,fuel_used,distance):
        self.mileage = distance/fuel_used

    def __str__(self):
        return f"the vehicle type is {self.type} ,color is {self.color}, top speed is {self.speed}"

bmw_X9 = vehicle("Car","black",150)
audi_R8 = vehicle("Car","silver",200)

bmw_X9.mileage(5,100)
audi_R8.mileage(4,120)

print(f"Mileage of bmw x9 is {bmw_X9.mileage}")
print(f"Mileage of audi R8 is {audi_R8.mileage}")

print(bmw_X9)
