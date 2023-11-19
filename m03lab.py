class Vehicle:
    def __init__(self, type):
        self.type = type

    def __str__(self):
        return "Vehicle type: " + self.type + "\n"

        
class Automobile(Vehicle):
    def __init__(self, type, year, make, model, doors, roof):
        super().__init__(type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def __str__(self):
        return "Vehicle type: " + type + "\n" + \
                "Year: " + self.year + "\n" + \
                "Make: " + self.make + "\n" + \
                "Model: " + self.model + "\n" \
                "Number of doors: " + self.doors + "\n" \
                "Type of roof: " + self.roof + "\n"



type = "car"
year = input("Please input the year of your " + type + ": ")
make = input("Please input the make of your " + type + ": ")
model = input("Please input the model of your " + type + ": ")
doors = input("Please input the number of doors of your " + type + ": ")
roof = input("Please input the type of roof on your " + type + ": ")

car = Automobile(type, year, make, model, doors, roof)

print(car)