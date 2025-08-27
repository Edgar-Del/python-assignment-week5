

class ElectronicDevice:
    """Base class for electronic devices"""
    
    def __init__(self, brand, model, year):
        self._brand = brand
        self._model = model
        self._year = year
        self._powered_on = False
    
    def power_on(self):
        """Turns on the device"""
        if not self._powered_on:
            self._powered_on = True
            print(f"🔌 {self._brand} {self._model} has been powered on!")
        else:
            print(f"⚠️ {self._brand} {self._model} is already powered on!")
    
    def power_off(self):
        """Turns off the device"""
        if self._powered_on:
            self._powered_on = False
            print(f"🔌 {self._brand} {self._model} has been powered off!")
        else:
            print(f"⚠️ {self._brand} {self._model} is already powered off!")
    
    def get_info(self):
        """Returns device information"""
        return f"📱 {self._brand} {self._model} ({self._year}) - Status: {'Powered On' if self._powered_on else 'Powered Off'}"


class Smartphone(ElectronicDevice):
    """Smartphone class that inherits from ElectronicDevice"""
    
    def __init__(self, brand, model, year, operating_system, storage_gb, ram_gb):
        # Call parent class constructor
        super().__init__(brand, model, year)
        
        # Smartphone-specific attributes
        self._operating_system = operating_system
        self._storage_gb = storage_gb
        self._ram_gb = ram_gb
        self._battery = 100
        self._installed_apps = []
    
    def install_app(self, app_name):
        """Installs an application"""
        if app_name not in self._installed_apps:
            self._installed_apps.append(app_name)
            print(f"📱 App '{app_name}' installed successfully!")
        else:
            print(f"⚠️ App '{app_name}' is already installed!")
    
    def uninstall_app(self, app_name):
        """Uninstalls an application"""
        if app_name in self._installed_apps:
            self._installed_apps.remove(app_name)
            print(f"🗑️ App '{app_name}' uninstalled!")
        else:
            print(f"❌ App '{app_name}' not found!")
    
    def charge_battery(self, percentage):
        """Charges the battery"""
        if 0 <= percentage <= 100:
            self._battery = min(100, self._battery + percentage)
            print(f"🔋 Battery charged! Current level: {self._battery}%")
        else:
            print("❌ Invalid percentage for charging!")
    
    def use_app(self, app_name):
        """Uses an application (consumes battery)"""
        if app_name in self._installed_apps:
            if self._battery > 0:
                self._battery = max(0, self._battery - 5)
                print(f"📱 Using '{app_name}'... Battery remaining: {self._battery}%")
            else:
                print("🔋 Battery depleted! Charge the smartphone first!")
        else:
            print(f"❌ App '{app_name}' is not installed!")
    
    def get_info(self):
        """Overrides parent method to show specific information"""
        base_info = super().get_info()
        apps_str = ", ".join(self._installed_apps) if self._installed_apps else "None"
        return (f"{base_info}\n"
                f"   OS: {self._operating_system}\n"
                f"   Storage: {self._storage_gb}GB\n"
                f"   RAM: {self._ram_gb}GB\n"
                f"   Battery: {self._battery}%\n"
                f"   Apps: {apps_str}")


# Example usage for Activity 1
def demonstrate_smartphone():
    print("=" * 50)
    print("🏗️ ACTIVITY 1: DESIGN YOUR OWN CLASS!")
    print("=" * 50)
    
    # Creating unique instances
    iphone = Smartphone("Apple", "iPhone 15", 2024, "iOS 17", 128, 8)
    samsung = Smartphone("Samsung", "Galaxy S24", 2024, "Android 14", 256, 12)
    
    print("📱 Creating unique smartphones:")
    print(iphone.get_info())
    print()
    print(samsung.get_info())
    print()
    
    # Demonstrating functionalities
    print("🔧 Testing functionalities:")
    iphone.power_on()
    iphone.install_app("Instagram")
    iphone.install_app("WhatsApp")
    iphone.install_app("TikTok")
    iphone.use_app("Instagram")
    iphone.charge_battery(20)
    print()
    
    samsung.power_on()
    samsung.install_app("YouTube")
    samsung.install_app("Spotify")
    samsung.use_app("YouTube")
    print()
    
    # Showing final state
    print("📊 Final state of smartphones:")
    print(iphone.get_info())
    print()
    print(samsung.get_info())


if __name__ == "__main__":
    demonstrate_smartphone()
