import random
#import lemonadestandclasses

# IN CLASS temp = random.randint(55, 92)

temp = random.randint(55, 92)
def temp_cust(temp):
    customers = 0
    if 55 <= temp <= 64:
        customers = 50
        return customers
    elif 65 <= temp <= 74:
        customers = 65
        return customers
    elif 75 <= temp <= 84:
        customers = 80
        return customers
    elif 85 <= temp <= 92:
        customers = 100
        return customers
customers = temp_cust(temp)

def weather_cust(customers):
    weather = random.randint(1, 4)
    if weather == 1:
        weather_name = "Sunny"
        customers += customers*0.6
        return [weather_name, round(customers)]
    elif weather == 2:
        weather_name = "Sunny and Dry"
        customers += customers*0.75
        return [weather_name, round(customers)]
    elif weather == 3:
        weather_name = "Cloudy"
        customers -= customers*0.25
        return [weather_name, round(customers)]
    elif weather == 4:
        weather_name = "Rainy"
        customers -= customers*0.65
        return [weather_name, round(customers)]



cust_list = weather_cust(customers)
weather_name = cust_list[0]
pot_customers = cust_list[1]

print(f'{temp} degrees and {weather_name} \n{pot_customers} potential customers')


