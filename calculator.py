import math
import statistics

def basic_calculator():
    print("Basic Calculator")
    while True:
        print("\nOptions:")
        print("Enter '1' for addition")
        print("Enter '2' for subtraction")
        print("Enter '3' for multiplication")
        print("Enter '4' for division")
        print("Enter '5' for exponentiation")
        print("Enter '6' for square root")
        print("Enter '7' for sine function")
        print("Enter '8' for cosine function")
        print("Enter '9' for tangent function")
        print("Enter '10' for natural logarithm")
        print("Enter '11' for unit conversion")
        print("Enter '12' for statistical functions")
        print("Enter '0' to quit the program")

        user_input = input("Enter the operation number: ")

        if user_input == '0':
            break
        elif user_input == '11':
            unit_conversion()
        elif user_input == '12':
            statistical_functions()
        elif user_input in ('1', '2', '3', '4', '5', '10'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if user_input == '1':
                result = num1 + num2
            elif user_input == '2':
                result = num1 - num2
            elif user_input == '3':
                result = num1 * num2
            elif user_input == '4':
                if num2 != 0:
                    result = num1 / num2
                else:
                    result = "Cannot divide by zero."
            elif user_input == '5':
                result = math.pow(num1, num2)
            elif user_input == '10':
                if num1 > 0 and num2 > 0:
                    result = math.log(num1, num2)
                else:
                    result = "Invalid input for logarithm."
        elif user_input in ('6', '7', '8', '9'):
            num = float(input("Enter a number: "))
            if user_input == '6':
                if num >= 0:
                    result = math.sqrt(num)
                else:
                    result = "Invalid input for square root."
            elif user_input == '7':
                result = math.sin(num)
            elif user_input == '8':
                result = math.cos(num)
            elif user_input == '9':
                result = math.tan(num)
        else:
            result = "Unknown input. Please try again."

        print("Result: " + str(result))

def unit_conversion():
    print("\nUnit Conversion")
    while True:
        print("Enter '1' for length conversion")
        print("Enter '2' for mass conversion")
        print("Enter '3' for temperature conversion")
        print("Enter '0' to return to the main menu")

        user_input = input("Enter the conversion number: ")

        if user_input == '0':
            break
        elif user_input == '1':
            length_conversion()
        elif user_input == '2':
            mass_conversion()
        elif user_input == '3':
            temperature_conversion()
        else:
            print("Unknown input. Please try again.")

def length_conversion():
    print("\nLength Conversion")
    value = float(input("Enter the value: "))
    while True:
        print("Enter '1' to convert meters to feet")
        print("Enter '2' to convert feet to meters")
        print("Enter '0' to return to the unit conversion menu")

        user_input = input("Enter the conversion number: ")

        if user_input == '0':
            break
        elif user_input == '1':
            result = value * 3.28084
            print(f"{value} meters is equal to {result} feet")
        elif user_input == '2':
            result = value / 3.28084
            print(f"{value} feet is equal to {result} meters")
        else:
            print("Unknown input. Please try again.")

def mass_conversion():
    print("\nMass Conversion")
    value = float(input("Enter the value: "))
    while True:
        print("Enter '1' to convert kilograms to pounds")
        print("Enter '2' to convert pounds to kilograms")
        print("Enter '0' to return to the unit conversion menu")

        user_input = input("Enter the conversion number: ")

        if user_input == '0':
            break
        elif user_input == '1':
            result = value * 2.20462
            print(f"{value} kilograms is equal to {result} pounds")
        elif user_input == '2':
            result = value / 2.20462
            print(f"{value} pounds is equal to {result} kilograms")
        else:
            print("Unknown input. Please try again.")

def temperature_conversion():
    print("\nTemperature Conversion")
    value = float(input("Enter the temperature in Celsius: "))
    while True:
        print("Enter '1' to convert Celsius to Fahrenheit")
        print("Enter '2' to convert Fahrenheit to Celsius")
        print("Enter '0' to return to the unit conversion menu")

        user_input = input("Enter the conversion number: ")

        if user_input == '0':
            break
        elif user_input == '1':
            result = (value * 9/5) + 32
            print(f"{value}°C is equal to {result}°F")
        elif user_input == '2':
            result = (value - 32) * 5/9
            print(f"{value}°F is equal to {result}°C")
        else:
            print("Unknown input. Please try again.")

def statistical_functions():
    print("\nStatistical Functions")
    while True:
        print("Enter '1' for mean calculation")
        print("Enter '2' for median calculation")
        print("Enter '3' for variance calculation")
        print("Enter '4' for standard deviation calculation")
        print("Enter '0' to return to the main menu")

        user_input = input("Enter the statistical function number: ")

        if user_input == '0':
            break
        elif user_input == '1':
            data = input("Enter a list of numbers separated by spaces: ").split()
            data = [float(x) for x in data]
            result = statistics.mean(data)
            print(f"Mean: {result}")
        elif user_input == '2':
            data = input("Enter a list of numbers separated by spaces: ").split()
            data = [float(x) for x in data]
            result = statistics.median(data)
            print(f"Median: {result}")
        elif user_input == '3':
            data = input("Enter a list of numbers separated by spaces: ").split()
            data = [float(x) for x in data]
            result = statistics.variance(data)
            print(f"Variance: {result}")
        elif user_input == '4':
            data = input("Enter a list of numbers separated by spaces: ").split()
            data = [float(x) for x in data]
            result = statistics.stdev(data)
            print(f"Standard Deviation: {result}")
        else:
            print("Unknown input. Please try again.")

if __name__ == '__main__':
    basic_calculator()
