# distance= int(input("Bitte Fahrtstrecke in km eingeben: ")) #distance

start_price = 4.5     #fee


def expenses_calculation(distance):
    expenses = distance*price_per_km+start_price
    return expenses

    
def printer():
    print("Eingehende Distanz: ", actual_distance, "km")
    print("Rechnung: ", actual_distance, " * ",  price_per_km , " + ", start_price  )
    print("Gesamtkosten:", expenses_calculation(actual_distance),"€")
    
def calc_loop():
    for actual_distance in range (0, 22):
        if actual_distance <= 5:      
            price_per_km = 1.50
        elif actual_distance >5 and actual_distance <=20:     
            price_per_km = 1.75
        elif actual_distance >20 and actual_distance <=50:     
            price_per_km = 2.0
        else:                 
    printer(actual_distance, price_per_km)
    
def main():
    calc_loop()    