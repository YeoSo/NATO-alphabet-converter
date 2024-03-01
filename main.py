import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
# converted_student = {}
#
# for student, score in zip(student_dict["student"], student_dict["score"]):
#     converted_student[student] = score
#
# print(converted_student)

# formatted_student_dic = {student: score for student, score in zip(student_dict["student"], student_dict["score"])}
# print(formatted_student_dic)


student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
student_df = {}
for (index, row) in student_data_frame.iterrows():
    student = row["student"]
    score = row["score"]
    student_df[student] = score
    # Access index and row
    # Access row.student or row.score
# print(student_df)

# With Dic comprehension below:
student_df = {row["student"]: row["score"] for (index, row) in student_data_frame.iterrows()}
# print(student_df)
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

data = pandas.read_csv("nato_phonetic_alphabet.csv")

# formatted_alphabet = {}
#
# for index, row in data.iterrows():
#     letter = row["letter"]
#     code = row["code"]
#     formatted_alphabet[letter] = code
# print(formatted_alphabet)

# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

# Dictionary comprehension:
formatted_alphabet = {row["letter"]: row["code"] for index, row in data.iterrows()}
# print(formatted_alphabet)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user = input("Type words to convert: ").upper()
# sliced_word = list(user)

name_alphabet = []

for letter in user:
    name_alphabet.append(formatted_alphabet[letter])
print(name_alphabet)

# List comprehension:
# name_alphabet = [formatted_alphabet[letter] for letter in user]
# print(name_alphabet)
