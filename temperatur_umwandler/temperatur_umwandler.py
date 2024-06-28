print("(1) Umrechnung von Celsius nach Kelvin")
print("(2) Umrechnnung von Celsius nach Fahrenheit")
print("(3) Umrechnung von Kelvin nach Celsius")
print("(4) Umrechnung von Kelvin nach Fahrenheit")
print("(5) Umrechnung von Fahrenheit nach Celsius")
print("(6) Umrechnung von Fahrenheit nach Kelvin")

choice = input("Bitte wählen: ")

if choice == "1":
    print("Umrechnung von Celsius nach Kelvin")
    celsius = float(input("Bitte Temperatur in Celsius eingeben: "))
    if celsius >= -273.15:
        kelvin = celsius + 273.15
        print(celsius, "°C = ", kelvin, "K") 
    else:
        print("Fehler: keine mögliche Temperatur")

elif choice == "2":
    print("Umrechnung von Celsius nach Fahrenheit")
    celsius = float(input("Bitte Temperatur in Celsius eingeben: "))
    if celsius >= -273.15:
        fahrenheit = celsius * 1.8 + 32.0
        print(celsius, "°C = ", fahrenheit, "°F")
    else:
        print("Fehler: keine mögliche Temperatur")

elif choice == "3":
    print("Umrechnung von Kelvin nach Celsius")
    kelvin = float(input("Bitte Temperatur in Kelvin eingeben: "))
    if kelvin >= 0.0:
        celsius = kelvin - 273.15
        print(kelvin, "K = ", celsius, "C°")
    else:
        print("Fehler: keine mögliche Temperatur")

elif choice == "4":
    print("Umrechnung von Kelvin nach Fahrenheit")
    kelvin = float(input("Bitte Temperatur in Kelvin eingeben: ")) 
    if kelvin >= 0.0:
        fahrenheit = kelvin*1.8 - 459.67
        print(kelvin, "K = ", fahrenheit, "°F")
    else:
        print("Fehler: keine mögliche Temperatur")

elif choice == "5":
    print("Umrechnung von Fahrenheit nach Celsius")
    fahrenheit = float(input("Bitte Temperatur in Fahrenheit eingeben: ")) 
    if fahrenheit >= -459.67:
        celsius = 5.0*(fahrenheit - 32.0)/9.0
        print(fahrenheit, "°F = ", celsius, "°C")
    else:
        print("Fehler: keine mögliche Temperatur")

elif choice == "6":
    print("Umrechnung von Fahrenheit nach Kelvin")
    fahrenheit = float(input("Temperatur in Fahrenheit: ")) 
    if fahrenheit >= -459.67:    
        kelvin = (fahrenheit + 459.67)/1.8
        print(fahrenheit, "°F = ", kelvin, "K")  
    else:
        print("Fehler: keine mögliche Temperatur!")        

else:
    print("Falsche Eingabe!")    