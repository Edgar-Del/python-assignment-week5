# Python Assignment Week 5 - Object Oriented Programming

This project demonstrates the fundamental concepts of Object Oriented Programming (OOP) in Python, including inheritance, encapsulation, and polymorphism.

## 📁 Project Structure

```
python-assignment-week5/
├── main.py                 # Main file that executes both activities
├── smartphone.py           # Activity 1: Smartphone class with inheritance
├── polymorphism_challenge.py # Activity 2: Polymorphism challenge
└── README.md              # This file
```

## Activity 1: Design Your Own Class!

### Demonstrated Objectives:
- **Inheritance**: The `Smartphone` class inherits from `ElectronicDevice`
- **Encapsulation**: Use of private attributes (`_brand`, `_model`, etc.)
- **Constructors**: Object initialization with unique values
- **Methods**: Specific functionalities like installing apps, charging battery

### Implemented Classes:
- `ElectronicDevice`: Base class with common functionalities
- `Smartphone`: Derived class with specific functionalities

### Features:
- ✅ Power on/off device
- ✅ Install/uninstall applications
- ✅ Charge battery
- ✅ Use applications (consumes battery)
- ✅ Detailed device information

## Activity 2: Polymorphism Challenge!

### Demonstrated Objectives:
- **Polymorphism**: Different implementations of the `move()` method
- **Abstract Classes**: Use of `ABC` and `@abstractmethod`
- **Multiple Inheritance**: Different types of vehicles

### Implemented Classes:
- `Vehicle`: Abstract base class
- `Car`: Implements `move()` as "driving on the road"
- `Plane`: Implements `move()` as "flying" or "taking off"
- `Boat`: Implements `move()` as "sailing on the sea"
- `Bicycle`: Implements `move()` as "pedaling"

### Features:
- ✅ Each vehicle has unique behavior in the `move()` method
- ✅ Specific functionalities per vehicle type
- ✅ Speed control and acceleration
- ✅ Clear demonstration of polymorphism

## 🚀 How to Run

### Option 1: Run everything at once
```bash
python main.py
```

### Option 2: Run activities separately
```bash
# Activity 1
python smartphone.py

# Activity 2
python polymorphism_challenge.py
```

## 📚 OOP Concepts Demonstrated

### 1. **Inheritance**
- `Smartphone` inherits from `ElectronicDevice`
- `Car`, `Plane`, `Boat`, `Bicycle` inherit from `Vehicle`

### 2. **Encapsulation**
- Use of private attributes with `_` (Python convention)
- Public methods to access/modify internal state

### 3. **Polymorphism**
- `move()` method implemented differently in each class
- Common interface (`Vehicle`) with specific behaviors

### 4. **Abstraction**
- Abstract class `Vehicle` defines common interface
- Specific implementations in subclasses

## Output Examples

### Activity 1 - Smartphone:
```
Apple iPhone 15 (2024) - Status: Powered Off
   OS: iOS 17
   Storage: 128GB
   RAM: 8GB
   Battery: 100%
   Apps: None
```

### Activity 2 - Polymorphism:
```
Ferrari F40 is driving at 100 km/h on the road!
Boeing 747 is taking off on the runway at 250 km/h!
Titanic is sailing at 30 km/h on the sea!
Caloi 10 is pedaling at 25 km/h in gear 5!
```
