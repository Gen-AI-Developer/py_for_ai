# Demonstrating the use of __new__ and __init__ methods in a class
# Classes are blueprints for creating objects


class Car:
    def __new__(cls, *args, **kwargs):
        print("Creating a new instance of Car")
        instance = super(Car, cls).__new__(cls)
        return instance

    def __init__(self, brand: str, wheels: int) -> None:
        print("Initializing the Car instance")
        self.brand = brand
        self.wheels = wheels

    def turn_on(self) -> None:
        print(f"Turning on : {self.brand} car")

    def turn_off(self) -> None:
        print(f"Turning off: {self.brand} car")

    def drive(self, km: float) -> None:
        print(f"Driving : {self.brand} car for {km} km")

    def describe(self) -> None:
        print(f"This is a {self.brand} car with {self.wheels} wheels.")
def main() -> None:
    my_car = Car("Toyota", 4)
    my_car.turn_on()
    my_car.drive(100)
    my_car.describe()
    my_car.turn_off()
if __name__ == "__main__":
    main()

# Create a Simple example of __new__ and __init__
class Example:
    def __new__(cls, *args, **kwargs):
        print("Creating a new instance of Example")
        instance = super(Example, cls).__new__(cls)
        return instance

    def __init__(self, value):
        print("Initializing the Example instance")
        self.value = value