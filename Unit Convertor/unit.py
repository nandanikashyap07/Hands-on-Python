def length_converter():
    print("Length Converter")
    print("1. Meter to Kilometer")
    print("2. Kilometer to Meter")
    print("3. Centimeter to Meter")
    print("4. Meter to Centimeter")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        m = float(input("Enter value in meters: "))
        print("Kilometers:", m / 1000)
    elif ch == 2:
        km = float(input("Enter value in km: "))
        print("Meters:", km * 1000)
    elif ch == 3:
        cm = float(input("Enter value in cm: "))
        print("Meters:", cm / 100)
    elif ch == 4:
        m = float(input("Enter value in meters: "))
        print("Centimeters:", m * 100)
    else:
        print("Invalid Choice!")


def weight_converter():
    print("Weight Converter")
    print("1. Gram to Kilogram")
    print("2. Kilogram to Gram")
    print("3. Pound to Kilogram")
    print("4. Kilogram to Pound")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        g = float(input("Enter grams: "))
        print("Kilograms:", g / 1000)
    elif ch == 2:
        kg = float(input("Enter kilograms: "))
        print("Grams:", kg * 1000)
    elif ch == 3:
        lb = float(input("Enter pounds: "))
        print("Kilograms:", lb * 0.453592)
    elif ch == 4:
        kg = float(input("Enter kilograms: "))
        print("Pounds:", kg / 0.453592)
    else:
        print("Invalid Choice!")


def temperature_converter():
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        c = float(input("Enter Celsius: "))
        print("Fahrenheit:", (c * 9/5) + 32)
    elif ch == 2:
        f = float(input("Enter Fahrenheit: "))
        print("Celsius:", (f - 32) * 5/9)
    elif ch == 3:
        c = float(input("Enter Celsius: "))
        print("Kelvin:", c + 273.15)
    elif ch == 4:
        k = float(input("Enter Kelvin: "))
        print("Celsius:", k - 273.15)
    else:
        print("Invalid Choice!")


def time_converter():
    print("Time Converter")
    print("1. Seconds to Minutes")
    print("2. Minutes to Seconds")
    print("3. Hours to Minutes")
    print("4. Minutes to Hours")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        s = float(input("Enter seconds: "))
        print("Minutes:", s / 60)
    elif ch == 2:
        m = float(input("Enter minutes: "))
        print("Seconds:", m * 60)
    elif ch == 3:
        h = float(input("Enter hours: "))
        print("Minutes:", h * 60)
    elif ch == 4:
        m = float(input("Enter minutes: "))
        print("Hours:", m / 60)
    else:
        print("Invalid Choice!")


while True:
    print("UNIT CONVERTER")
    print("1. Length")
    print("2. Weight")
    print("3. Temperature")
    print("4. Time")
    print("5. Exit")

    choice = int(input("Enter your option: "))

    if choice == 1:
        length_converter()
    elif choice == 2:
        weight_converter()
    elif choice == 3:
        temperature_converter()
    elif choice == 4:
        time_converter()
    elif choice == 5:
        print("Thank you for using Unit Converter!")
        break
    else:
        print("Invalid choice!")
