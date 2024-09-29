# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FAHRENHEIT_OFFSET = 32

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    # Convert Fahrenheit to Celsius using global conversion factor
    return (fahrenheit - FAHRENHEIT_OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    # Convert Celsius to Fahrenheit using global conversion factor
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FAHRENHEIT_OFFSET

# Main program to prompt the user for input
def main():
    try:
        # Prompt user for temperature and unit
        temp = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        
        if unit == "F":
            converted_temp = convert_to_celsius(temp)
            print(f"{temp}°F is {converted_temp}°C")
        elif unit == "C":
            converted_temp = convert_to_fahrenheit(temp)
            print(f"{temp}°C is {converted_temp}°F")
        else:
            # Raise error if the unit is not 'C' or 'F'
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

# Run the program
if __name__ == "__main__":
    main()
