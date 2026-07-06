class OutOfRangeError(Exception):
    """Raised when an input violates physical limits."""
    pass

class UnitConverter:
    def __init__(self):
        pass
        
    def km_miles(self):
        try:
            km = float(input("Enter the distance in kilometers: "))
            if km < 0:
                raise OutOfRangeError("Distance cannot be negative.")
            miles = km * 0.621371
            print(f"Result: {km} km = {miles:.2f} miles\n")
        except ValueError:
            print("Error: That is not a valid number.\n")
        except OutOfRangeError as error:
            print(f"Range Error: {error}\n")

    def celsius_fahrenheit(self):
        ABSOLUTE_ZERO_CELSIUS = -273.15
        try:
            celsius = float(input("Enter the temperature in Celsius: "))
            if celsius < ABSOLUTE_ZERO_CELSIUS:
                raise OutOfRangeError(f"Temperature cannot be below Absolute Zero ({ABSOLUTE_ZERO_CELSIUS}°C).")
            fahrenheit = (celsius * 9/5) + 32
            print(f"Result: {celsius}°C = {fahrenheit:.2f}°F\n")
        except ValueError:
            print("Error: That is not a valid number.\n")
        except OutOfRangeError as error:
            print(f"Range Error: {error}\n")

    def kg_lbs(self):
        try:
            kg = float(input("Enter the weight in kilograms: "))
            if kg < 0:
                raise OutOfRangeError("Weight cannot be negative.")
            lbs = kg * 2.20462
            print(f"Result: {kg} kg = {lbs:.2f} lbs\n")
        except ValueError:
            print("Error: That is not a valid number.\n")
        except OutOfRangeError as error:
            print(f"Range Error: {error}\n")

    def liters_gallons(self):
        try:
            liters = float(input("Enter volume in liters: "))
            if liters < 0:
                raise OutOfRangeError("Volume cannot be negative.")
            gallons = liters * 0.264172
            print(f"Result: {liters} L = {gallons:.2f} gallons\n")
        except ValueError:
            print("Error: That is not a valid number.\n")
        except OutOfRangeError as error:
            print(f"Range Error: {error}\n")

    def gb_tb(self):
        try:
            gb = float(input("Enter data size in GB: "))
            if gb < 0:
                raise OutOfRangeError("Data size cannot be negative.")
            tb = gb / 1024
            print(f"Result: {gb} GB = {tb:.4f} TB\n")
        except ValueError:
            print("Error: That is not a valid number.\n")
        except OutOfRangeError as error:
            print(f"Range Error: {error}\n")

    def ms_kmh(self):
        try:
            ms = float(input("Enter speed in m/s: "))
            if ms < 0:
                raise OutOfRangeError("Speed cannot be negative.")
            kmh = ms * 3.6
            print(f"Result: {ms} m/s = {kmh:.2f} km/h\n")
        except ValueError:
            print("Error: That is not a valid number.\n")
        except OutOfRangeError as error:
            print(f"Range Error: {error}\n")

    def pa_atm(self):
        try:
            pa = float(input("Enter pressure in Pascals: "))
            if pa < 0:
                raise OutOfRangeError("Pressure cannot drop below a perfect vacuum (0 Pa).")
            atm = pa / 101325
            print(f"Result: {pa} Pa = {atm:.5f} atm\n")
        except ValueError:
            print("Error: That is not a valid number.\n")
        except OutOfRangeError as error:
            print(f"Range Error: {error}\n")

    def run_menu(self):
        while True:
            print("=== Multi-Unit Converter Menu ===")
            print("1. Kilometers to Miles")
            print("2. Celsius to Fahrenheit")
            print("3. Kilograms to Pounds")
            print("4. Liters to Gallons")
            print("5. Gigabytes to Terabytes")
            print("6. Meters/Second to KM/Hour")
            print("7. Pascals to Atmospheres")
            print("8. Exit")
            
            choice = input("Select an option (1-8): ").strip()
            print() 
            
            if choice == '1':
                self.km_miles()
            elif choice == '2':
                self.celsius_fahrenheit()
            elif choice == '3':
                self.kg_lbs()
            elif choice == '4':
                self.liters_gallons()
            elif choice == '5':
                self.gb_tb()
            elif choice == '6':
                self.ms_kmh()
            elif choice == '7':
                self.pa_atm()
            elif choice == '8':
                print("Thank you for using UnitConverter. Goodbye!")
                break
            else:
                print("Invalid selection! Please enter a number between 1 and 8.\n")


if __name__ == "__main__":
    converter = UnitConverter()
    converter.run_menu()
