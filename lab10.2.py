import matplotlib.pyplot as plt
import numpy as np
import csv 
import sys

def valueround(value):
    if value >= 1:
        return round(value)
    else: 
        return round(value, 1)


try:
    with open ("Data.csv", "r", encoding= "utf-8-sig") as file:
        reader = csv.DictReader(file, delimiter=",")

        years = []
        for column in reader.fieldnames:
            if 'YR' in column:
                year = ''.join(filter(str.isdigit, column))[:4]
                years.append(year)
        
        valuesUkraine = []
        valuesSpain = []
        for line in reader:
            for year in years:
                value = float(line[f"{year} [YR{year}]"])
                ready_made_value = valueround(value)

                if line['Country Name'] == 'Ukraine':
                    valuesUkraine.append(ready_made_value)
                else:
                    valuesSpain.append(ready_made_value)
except:
    print("File \"Data.csv\" nor found!")
    sys.exit

np.array(years)
np.array(valuesUkraine)
np.array(valuesSpain)

plt.figure(figsize = (11, 5))
plt.plot(years, valuesUkraine, label = "Ukraine", color = "#E72626")
plt.plot(years, valuesSpain, label = "Spain", color = "#43E726")

plt.title("Total reserves in months of imports (2005-2024)", fontsize = 15)
plt.xlabel("Year", fontsize = 10, color = "#266AE7")
plt.ylabel("Indicator", fontsize = 10, color = "#2636E7")

plt.grid(True)
plt.legend()

plt.show()

country = input("Enter country to build a bar chart ( Ukraine/Spain ): ")
while country not in ["Ukraine", "Spain"]:
    country = input("Please, enter only letters and only Ukraine or Spain: ")

if country == "Ukraine":
     valuescountry = valuesUkraine
else: 
     valuescountry = valuesSpain

fig, ax = plt.subplots()
ax.bar(years, valuescountry, label = country, color ="#26E7E7")

fig.set_figwidth(11)
fig.set_figheight(5)
ax.set_facecolor("seashell")

plt.title("Total reserves in months of imports (2005-2024)", fontsize = 15)
plt.xlabel("Year", fontsize = 10, color = "#E76A26")
plt.ylabel("Indicator", fontsize = 10, color = "#E78726")
plt.legend(loc="center left", bbox_to_anchor = (1, 0.5))

plt.show()