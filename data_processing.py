import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

class Table:
    def __init__(self, data):
        self.data = data

    def filter(self, condition):
        filtered_data = [item for item in self.data if condition(item)]
        return Table(filtered_data)

    def aggregate(self, key, aggregation_function):
        values = [float(item[key]) for item in self.data]
        return aggregation_function(values)

    def select(self, key):
        # แก้ไขจาก item(key) เป็น item[key]
        return [item[key] for item in self.data]

class DataLoader:
    @staticmethod
    def load_csv(filepath):
        data = []
        with open(filepath, 'r') as f:
            rows = csv.DictReader(f)
            for r in rows:
                data.append(dict(r))
        return Table(data)

    
csv_path = os.path.join(__location__, 'Cities.csv')
table = DataLoader.load_csv(csv_path)

# Print first 5 cities only
for city in table.data[:5]:
    print(city)
print()

# Print the average temperature of all the cities
# (แก้ไข: ลบ cities ออกจาก aggregate)
print("The average temperature of all the cities:")
avg_all = table.aggregate('temperature', lambda temps: sum(temps) / len(temps))
print(f"{avg_all:.2f}")
print()

# Print all cities in Germany
# (แก้ไข: ใช้ .select('city') เพื่อดึงรายชื่อเมืองมาแสดงผล)
print("All cities in Germany")
germany_table = table.filter(lambda c: c['country'] == 'Germany')
for city in germany_table.select('city'):
    print(city)
print()

# Print all cities in Spain with a temperature above 12°C
# (แก้ไข: ลบ cities ออกจาก filter)
print("All cities in Spain with a temperature above 12°C")
spain_warm_table = table.filter(lambda c: c['country'] == 'Spain' and float(c['temperature']) > 12)
for city in spain_warm_table.select('city'):
    print(city)
print()

# Count the number of unique countries
uniqe_countries = set(table.select('country'))
print("Number of unique countries:", len(uniqe_countries))
print()

# Print the average temperature for all the cities in Germany
# (แก้ไข: เรียกใช้ germany_table ที่กรองไว้แล้ว)
avg_germany_temp = germany_table.aggregate('temperature', lambda temps: sum(temps) / len(temps))
print(f"The average temperature for all the cities in Germany: {avg_germany_temp:.2f}")
print()

# Print the max temperature for all the cities in Italy
# (แก้ไข: ใช้ italy_table และลบ italy_cities ออกจาก aggregate)
italy_table = table.filter(lambda c: c['country'] == 'Italy')
max_temp_italy = italy_table.aggregate('temperature', max)
print(f"The max temperature for all the cities in Italy: {max_temp_italy:.2f}")