# Generic "Parent" class
class Vehicle:

    def __init__(self, color, year, make, model, mileage=0):
        self.color = color
        self.year = year
        self.make = make
        self.model = model
        self.mileage = mileage

    def honk(self):
        return "HOOOOOOOOONK!"

    def drive(self, miles_driven):
        self.mileage += miles_driven
        return self.mileage


# More specific "Child" class
class Car(Vehicle):
    # Static Attribute
    # can't be changed via user input to the constructor
    num_wheels = 4

    def __init__(self, color, year, make, model, style, mileage=0, top_open=False):
        super().__init__(color, year, make, model, mileage)
        self.style = style
        self.top_open = top_open

    def raise_top(self):
        if (self.top_open):
            return "top is already open"
        else:
            self.top_open = True
            return "top is now open"

    def lower_top(self):
        if (self.top_open):
            self.top_open = False
            return "top is now closed"
        else:
            return "top is already closed"

    def __repr__(self):
        return f"<A {self.color} {self.make} {self.model} with {self.mileage} miles>"


if __name__ == '__main__':
    my_vehicle = Car('red', 2022, 'Porsche', 'Boxter', 'convertible')
    print(my_vehicle.raise_top)
    
    