from abc import ABC, abstractmethod

class Vehicle(ABC):
    """Abstract base class for all vehicles"""
    
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed
        self.current_speed = 0
    
    @abstractmethod
    def move(self):
        """Abstract method that must be implemented by each subclass"""
        pass
    
    def accelerate(self, increment):
        """Accelerates the vehicle"""
        new_speed = self.current_speed + increment
        if new_speed <= self.max_speed:
            self.current_speed = new_speed
            print(f"{self.name} accelerated to {self.current_speed} km/h")
        else:
            self.current_speed = self.max_speed
            print(f"{self.name} reached maximum speed of {self.max_speed} km/h!")
    
    def brake(self, decrement):
        """Brakes the vehicle"""
        new_speed = max(0, self.current_speed - decrement)
        self.current_speed = new_speed
        if new_speed > 0:
            print(f"{self.name} braked to {self.current_speed} km/h")
        else:
            print(f"{self.name} stopped completely!")
    
    def get_status(self):
        """Returns current vehicle status"""
        return f"{self.name}: Current speed: {self.current_speed} km/h (Max: {self.max_speed} km/h)"


class Car(Vehicle):
    """Car class that inherits from Vehicle"""
    
    def __init__(self, name, max_speed, fuel_type):
        super().__init__(name, max_speed)
        self.fuel_type = fuel_type
        self.doors = 4
    
    def move(self):
        """Specific implementation for car"""
        if self.current_speed > 0:
            print(f"{self.name} is driving at {self.current_speed} km/h on the road!")
        else:
            print(f"{self.name} is parked in the garage.")
    
    def open_door(self, door_number):
        """Opens a specific car door"""
        if 1 <= door_number <= self.doors:
            print(f"Door {door_number} of {self.name} was opened!")
        else:
            print(f"Door {door_number} doesn't exist in {self.name}!")


class Plane(Vehicle):
    """Plane class that inherits from Vehicle"""
    
    def __init__(self, name, max_speed, max_altitude):
        super().__init__(name, max_speed)
        self.max_altitude = max_altitude
        self.current_altitude = 0
    
    def move(self):
        """Specific implementation for plane"""
        if self.current_speed > 0 and self.current_altitude > 0:
            print(f"{self.name} is flying at {self.current_speed} km/h at {self.current_altitude}m altitude!")
        elif self.current_speed > 0:
            print(f"{self.name} is taking off on the runway at {self.current_speed} km/h!")
        else:
            print(f"{self.name} is parked at the airport.")
    
    def take_off(self):
        """Makes the plane take off"""
        if self.current_speed >= 200:
            self.current_altitude = min(self.max_altitude, 1000)
            print(f"🛫 {self.name} took off! Current altitude: {self.current_altitude}m")
        else:
            print(f"{self.name} needs at least 200 km/h to take off!")
    
    def land(self):
        """Makes the plane land"""
        if self.current_altitude > 0:
            self.current_altitude = 0
            self.current_speed = 0
            print(f"{self.name} landed successfully!")
        else:
            print(f"{self.name} is already on the ground!")


class Boat(Vehicle):
    """Boat class that inherits from Vehicle"""
    
    def __init__(self, name, max_speed, max_depth):
        super().__init__(name, max_speed)
        self.max_depth = max_depth
        self.anchored = True
    
    def move(self):
        """Specific implementation for boat"""
        if self.current_speed > 0 and not self.anchored:
            print(f"{self.name} is sailing at {self.current_speed} km/h on the sea!")
        elif self.current_speed > 0 and self.anchored:
            print(f"{self.name} is anchored but with engine running!")
        else:
            print(f"{self.name} is anchored at the port.")
    
    def raise_anchor(self):
        """Raises the boat's anchor"""
        if self.anchored:
            self.anchored = False
            print(f"{self.name}'s anchor was raised! Boat free to sail!")
        else:
            print(f"{self.name} is not anchored!")
    
    def drop_anchor(self):
        """Drops the boat's anchor"""
        if not self.anchored:
            self.anchored = True
            self.current_speed = 0
            print(f"{self.name}'s anchor was dropped! Boat anchored.")
        else:
            print(f"{self.name} is already anchored!")


class Bicycle(Vehicle):
    """Bicycle class that inherits from Vehicle"""
    
    def __init__(self, name, max_speed, gears):
        super().__init__(name, max_speed)
        self.gears = gears
        self.current_gear = 1
    
    def move(self):
        """Specific implementation for bicycle"""
        if self.current_speed > 0:
            print(f"{self.name} is pedaling at {self.current_speed} km/h in gear {self.current_gear}!")
        else:
            print(f"{self.name} is parked at the bike rack.")
    
    def change_gear(self, new_gear):
        """Changes the bicycle's gear"""
        if 1 <= new_gear <= self.gears:
            self.current_gear = new_gear
            print(f"{self.name} changed to gear {self.current_gear}!")
        else:
            print(f"Gear {new_gear} doesn't exist in {self.name}!")


def demonstrate_polymorphism():
    """Demonstrates polymorphism between different vehicle types"""
    print("=" * 60)
    print("ACTIVITY 2: POLYMORPHISM CHALLENGE!")
    print("=" * 60)
    
    # Creating different types of vehicles
    car = Car("Ferrari F40", 320, "Gasoline")
    plane = Plane("Boeing 747", 900, 13000)
    boat = Boat("Titanic", 45, 4000)
    bicycle = Bicycle("Caloi 10", 60, 21)
    
    # List of vehicles to demonstrate polymorphism
    vehicles = [car, plane, boat, bicycle]
    
    print("CREATING VEHICLES:")
    for vehicle in vehicles:
        print(vehicle.get_status())
    print()
    
    # Demonstrating polymorphism - all have move() method but behave differently
    print("DEMONSTRATING POLYMORPHISM:")
    print("All vehicles implement move() differently:")
    print()
    
    for vehicle in vehicles:
        print(f"--- {vehicle.name} ---")
        vehicle.move()  # Each one behaves differently!
        print()
    
    # Testing specific functionalities
    print("TESTING SPECIFIC FUNCTIONALITIES:")
    
    # Car
    car.accelerate(100)
    car.move()
    car.open_door(2)
    print()
    
    # Plane
    plane.accelerate(250)
    plane.take_off()
    plane.move()
    plane.land()
    print()
    
    # Boat
    boat.raise_anchor()
    boat.accelerate(30)
    boat.move()
    boat.drop_anchor()
    print()
    
    # Bicycle
    bicycle.accelerate(25)
    bicycle.change_gear(5)
    bicycle.move()
    print()
    
    # Final demonstration of polymorphism
    print("FINAL POLYMORPHISM DEMONSTRATION:")
    print("Calling move() on all vehicles again:")
    print()
    
    for vehicle in vehicles:
        vehicle.move()


if __name__ == "__main__":
    demonstrate_polymorphism()
