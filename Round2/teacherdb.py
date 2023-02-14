import numpy as np
import pandas as pd


df_teacher = pd.DataFrame({
    "name": ["Pep Guardiola", "Jurgen Klopp", "Mikel Arteta", "Zinadine Zidane"],
    "married": [True, True, False, True],
    "school": ["Manchester High School", "Liverpool High School", "Arsenal High", np.nan]
})

df_student = pd.DataFrame({
    "teacher": ["Mikel Arteta", "Mikel Arteta", "Pep Guardiola", "Jurgen Klopp", "Jurgen Klopp", "Jurgen Klopp", "Pep Guardiola","Pep Guardiola","Mikel Arteta"],
    "name": ["Bukayo Saka", "Gabriel Martinelli", "Jack Grealish", "Roberto Firmino", "Andrew Robertson", "Darwin Nunez", "Ederson Moraes", "Manuel Akanji", "Thomas Partey"],
    "age": [21, 21, 27, 31, 28, 23, 29, 27, 29],
    "height": ['2.1m', '2.1m', '2.1m', '2.1m', '2.1m', '2.1m', '2.1m', '2.1m', '2.1m'],
    # "weight": ['80kg', '70kg', '690kg', '73kg', '60kg', '70kg', '80kg', '88kg', '74kg'],
    })

print("df_teacher : ", df_teacher.to_json(orient='values'))
print("df_student : ", df_student.to_json(orient='values'))
df_combined = pd.concat([df_teacher, df_student], axis=1).to_json(orient='values')

print("Teacher and Student Df combined : ", df_combined)

# Adding weight column to df_student

weight = ['80kg', '70kg', '690kg', '73kg', '60kg', '70kg', '80kg', '88kg', '74kg']
df_student['weight'] = weight
print(pd.concat([df_teacher, df_student], axis=1).to_json(orient='values'))
