class vehicle:

    def __init__(self , max_speed , mileage)

        self.max_speed = max_speed
        self.mileage = mileage

Model_X = vehicle(200,20)

print(f"Model_X max speed is {Model_X.max_speed} and mileage is {Model_X.mileage}")