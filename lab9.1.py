import csv
import sys

try: 
    filecsv = open("Data.csv", "r", encoding= "utf-8-sig") 
    reader = csv.DictReader(filecsv, delimiter=',')
    for line in reader:
        print(line)
    filecsv.close()
except:
    print("File \"Data.csv\" not found!")
    sys.exit()

try:
    with open("Data.csv", "r", encoding = "utf-8-sig") as file: 
        reader = csv.DictReader(file, delimiter=',')
        database = list(reader)

        column3 = list(database[0].keys())[2]
        column5 = list(database[0].keys())[4]

        values = []
        for line in database:
            value = line[column5]
            try:
                values.append((line[column3], float(value)))
            except ValueError:
                continue

        country_min, minimum = min(values, key = lambda number: number[1])
        country_max, maximum = max(values, key = lambda number: number[1])

        with open("Results.csv", "w+", newline='', encoding= 'utf-8-sig') as file:
            writer = csv.writer(file)
            information = [
                ["Country Name", "2015 [YR2015]"],
                [country_min, minimum],
                [country_max, maximum]
            ]
            writer.writerows(information)
            print("\nCreated file \"Results.csv\" with search results!")
except:
    print("\nFile \"Data.csv\" not found!")
    sys.exit()