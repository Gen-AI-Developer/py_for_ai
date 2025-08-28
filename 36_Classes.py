#Classes are blue prints

class Car:
    def __init__(self,brand:str,wheels:int) -> None:
        self.brand = brand
        self.wheels = wheels
    
    def turn_on(self) -> None:
        print(f"Turing on : {self.brand} car")
        
    def turn_off(self) -> None:
        print(f" Turing off: {self.brand} car")
        
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