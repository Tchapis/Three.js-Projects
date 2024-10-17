# Temperature conversion module
#How to Use in Other Programs:
#To use this module in other Python programs, simply import the relevant functions from this module.

# from temperature_conversion import kelvin_to_celsius, celsius_to_fahrenheit

# # Convert 300K to Celsius
# celsius_value = kelvin_to_celsius(300)
# print(f"300K is {celsius_value:.2f}°C")

# # Convert 25°C to Fahrenheit
# fahrenheit_value = celsius_to_fahrenheit(25)
# print(f"25°C is {fahrenheit_value:.2f}°F")




# Convert Kelvin to Celsius
def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

# Convert Celsius to Kelvin
def celsius_to_kelvin(celsius):
    return celsius + 273.15

# Convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Convert Kelvin to Fahrenheit
def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

# Convert Fahrenheit to Kelvin
def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

# Example usage
if __name__ == "__main__":
    # Example inputs
    temp_in_kelvin = 300
    temp_in_celsius = 26.85
    temp_in_fahrenheit = 80.33

    # Convert Kelvin to Celsius and Fahrenheit
    print(f"{temp_in_kelvin}K is {kelvin_to_celsius(temp_in_kelvin):.2f}°C")
    print(f"{temp_in_kelvin}K is {kelvin_to_fahrenheit(temp_in_kelvin):.2f}°F")

    # Convert Celsius to Kelvin and Fahrenheit
    print(f"{temp_in_celsius}°C is {celsius_to_kelvin(temp_in_celsius):.2f}K")
    print(f"{temp_in_celsius}°C is {celsius_to_fahrenheit(temp_in_celsius):.2f}°F")

    # Convert Fahrenheit to Celsius and Kelvin
    print(f"{temp_in_fahrenheit}°F is {fahrenheit_to_celsius(temp_in_fahrenheit):.2f}°C")
    print(f"{temp_in_fahrenheit}°F is {fahrenheit_to_kelvin(temp_in_fahrenheit):.2f}K")
