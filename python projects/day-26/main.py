# numbers = [1, 2, 3]
#
# new_list = [n+1 for n in numbers]
# print(new_list)
#
# range_list = [x*2 for x in range(1,5)]
# print(range_list)
#
# names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
# long_names = [name.upper() for name in names if len(name) > 4]
# print(long_names)

student_scores = {
    "student": ["angela", "beth", "lily"],
    "score" : [65, 74, 25]
}

import pandas
df = pandas.DataFrame(student_scores)
print(df)

# loop through rows of a data frame

for (index, row) in df.iterrows():
    if row.student == "angela":
        print(row.score)