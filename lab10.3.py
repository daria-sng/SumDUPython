# Скільки відсотків оцінок учнів є відмінними, добрими, задовільними та початковими
import matplotlib.pyplot as plt
import numpy as np

students = {
    'Daniel Miller': [10, 11, 8, 9, 10],
    'Emma Smith': [11, 11, 12, 10, 9],
    'John Jones': [1, 5, 8, 10, 2],
    'Amelia Davis': [7, 8, 4, 6, 8],
    'James Brown': [10, 1, 7, 8, 9],
    'Charlotte Lopez': [3, 10, 12, 11, 10],
    'Thomas Wilson': [6, 4, 2, 1, 1],
    'Ava Garcia': [10, 10, 12, 10, 11],
    'Ethan Anderson': [9, 8, 10, 9, 2],
    'Ella Harris': [1, 6, 9, 10, 4]
}

total = 0
generalmarks = [0, 0, 0, 0]

for student, grades in students.items():
    total += len(grades)
    for grade in grades:
        if 12 >= grade >= 10:
            generalmarks[0] += 1
        elif 9 >= grade >= 7:
            generalmarks[1] += 1
        elif 6 >= grade >= 4:
            generalmarks[2] += 1
        else:
            generalmarks[3] += 1

categories = ["Excellent", "Good", "Satisfactory", "Elementary"]

fig, ax = plt.subplots(figsize = (7, 4), subplot_kw=dict(aspect = "equal"))
ax.set_title("Total percentage grades of all students")
color =["#59FF00", "#00FF8C", "#FFAE00", "#E72626"]

def function(percentage, grades):
    value = int(np.round(percentage/100.*np.sum(grades)))
    return f"{percentage:.0f}%\n({value} grds)"

wedges, texts, autotexts = ax.pie(generalmarks, 
                                  colors = color, 
                                  autopct = lambda percentage: function(percentage, generalmarks), 
                                  textprops = dict(color = "w"))

ax.legend(wedges, categories, title = "Grade Categories", loc= "center left", bbox_to_anchor = (1, 0, 0.5, 1))
plt.setp(autotexts, size = 10, weight = 700)

plt.show()
