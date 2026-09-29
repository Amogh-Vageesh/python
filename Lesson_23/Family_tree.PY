#create the parent class with shared family traits

class familymember:
    def __init__(self, eye_color, height_cm):
        self.eye_color = eye_color
        self.height_cm = height_cm 
    def show_traits(self):
        print(f"Eye color : {self.eye_color}")
        print(f"Height (cm): {self.height_cm}")

#create the child class that inherits traits

class kid(familymember):
    def __init__(self, name, age, eye_color, height_cm):
        self.name = name
        self.age = age
        super().__init__(eye_color, height_cm)

#override show_traits to add the kids own traits also

    def show_traits(self):
        print(f"Name : {self.name} ")
        print(f"age : {self.age}")
        super().show_traits()

#add a brand new method only kid has

    def favorite_hobby(self, hobby):
        print(f"{self.name} loves {hobby}")

#create a kid object with real family traits

child = kid("Maya", 10, "blue", 140)

#call the overridden and new method

child.show_traits()
child.favorite_hobby("painting")

#check whether kid is really a subclass of family member
print(f"Is child a subclass of family member? {issubclass(kid, familymember)}")