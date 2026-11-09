import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

# Print first 5 cities only
for city in cities[:5]:
    print(city)

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = []
for city in cities:
    temps.append(float(city['temperature']))
print(sum(temps)/len(temps))
print()

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = [float(city['temperature']) for city in cities]
print(sum(temps)/len(temps))
print()

# Print all cities in Germany

print("All cities in Germany")
for city in cities:
    if city['country'] == "Germany":
        print(city)
print()

# Print all cities in Spain with a temperature above 12°C

print("All cities in Spain with a temperature above 12°C")
for city in cities:
    if city['country'] == "Spain":  
        if float(city['temperature']) > 12:
            print(city)


# Count the number of unique countries

uniqe_countries = set(city['country'] for city in cities)
print(f"Number of unique countries:",len(uniqe_countries))

all_germany_temp = []
# Print the average temperature for all the cities in Germany
for city in cities:
    if city['country'] == 'Germany':
        all_germany_temp.append(float(city['temperature']))

    for temp in all_germany_temp:
        avg_temp = sum(all_germany_temp)/len(all_germany_temp)
print(f"The average temperature for all the cities in Germany:{avg_temp:.2f}")

# Print the max temperature for all the cities in Italy

city_italy = []
for city in cities:
    if city['country'] == 'Italy':
        city_italy.append(float(city['temperature']))

max__temp_italy = max(city_italy)
print(f"The max temperature for all the cities in Italy {max__temp_italy}")
