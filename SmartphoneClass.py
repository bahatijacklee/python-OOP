# Define a Smartphone class
class Smartphone:
    def __init__(self, brand, model, storage, battery_life):
        self.brand = brand
        self.model = model
        self.storage = storage  # in GB
        self.battery_life = battery_life  # in hours
    
    # Method to display smartphone details
    def display_info(self):
        print(f"Smartphone: {self.brand} {self.model}")
        print(f"Storage: {self.storage}GB")
        print(f"Battery life: {self.battery_life} hours")
    
    # Method to simulate charging the phone
    def charge(self):
        print(f"{self.brand} {self.model} is charging... 🔋")

# Define a Smartwatch class that inherits from Smartphone
class Smartwatch(Smartphone):
    def __init__(self, brand, model, storage, battery_life, has_heart_rate_monitor):
        # Call the parent constructor
        super().__init__(brand, model, storage, battery_life)
        self.has_heart_rate_monitor = has_heart_rate_monitor

    # Override the display_info method to include specific details for Smartwatch
    def display_info(self):
        super().display_info()  # Call the parent method
        print("Heart Rate Monitor:", "Yes" if self.has_heart_rate_monitor else "No")
    
    # Additional method specific to Smartwatch
    def track_activity(self):
        print(f"{self.brand} {self.model} is tracking your activity... 🏃")

# Create objects and test the classes
phone = Smartphone("Apple", "iPhone 14", 128, 20)
watch = Smartwatch("Apple", "Watch Series 8", 32, 18, True)

# Display information and call methods
phone.display_info()
phone.charge()
print()
watch.display_info()
watch.track_activity()
