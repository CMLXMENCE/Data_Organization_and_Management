# 2018510008 Özgür Cem Arslan     2019510022 Mehmet Ali Berk
import csv
import json
from blist import sorteddict

json_dict = []
with open("input.csv", encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    students = sorteddict()
    for row in csv_reader:
        if row[0] == 'id':
            continue
        students[row[0]] = {"name": row[1], "lastname": row[2], "email": row[3], "grade": row[4]}
    # Do not use quotation marks in first and last name.
    # DELETE FROM STUDENTS WHERE name = John or grade <= 20
    # DELETE FROM STUDENTS WHERE name = Sandy or grade > 10
    # Leave a space after the variable name when using a single command
    # DELETE FROM STUDENTS WHERE name = Sandy (there is a space after sandy here)
#while True:  # we tried to loop the code but in the first input(line:19) we got ‘list’ object is not callable error and we couldn't be able to fix it so we left it in comment line
    command = input("please enter command")
    if command[0:27] == "INSERT INTO STUDENTS VALUES":
        input = command[28:len(command) - 1].split(",")
        students[input[0]] = {"name": input[1], "lastname": input[2], "email": input[3], "grade": input[4]}

    keys_to_delete = []
    keys_to_select = []
    and_or_cond = command[26:len(command)].split(" ")
    if command[0:26] == "DELETE FROM STUDENTS WHERE":
        input = command[26:len(command)].split(" ")
        for key in students.keys():
            if input[3] == students[key]["name"] and and_or_cond[4] != "and" and and_or_cond[4] != "or":
                keys_to_delete.append(key)
                json_dict.append(students[key])
            elif input[3] == students[key]["lastname"] and and_or_cond[4] != "and" and and_or_cond[4] != "or":
                keys_to_delete.append(key)
                json_dict.append(students[key])
            elif input[2] == ">" and len(and_or_cond) < 4 and and_or_cond[4] != "and" and and_or_cond[4] != "or":
                if int(input[3]) < int(students[key]["grade"]):
                    keys_to_delete.append(key)
                    json_dict.append(students[key])
            elif input[2] == "<" and len(and_or_cond) < 4 and and_or_cond[4] != "and" and and_or_cond[4] != "or":
                if int(input[3]) > int(students[key]["grade"]):
                    keys_to_delete.append(key)
                    json_dict.append(students[key])
            elif input[2] == "=" and len(and_or_cond) < 4 and and_or_cond[4] != "and" and and_or_cond[4] != "or":
                if int(input[3]) == int(students[key]["grade"]):
                    keys_to_delete.append(key)
                    json_dict.append(students[key])
            elif input[2] == "!=" and len(and_or_cond) < 4 and and_or_cond[4] != "and" and and_or_cond[4] != "or":
                if int(input[3]) != int(students[key]["grade"]):
                    keys_to_delete.append(key)
                    json_dict.append(students[key])
            elif input[2] == ">=" and len(and_or_cond) < 4 and and_or_cond[4] != "and" and and_or_cond[4] != "or":
                if int(input[3]) <= int(students[key]["grade"]):
                    keys_to_delete.append(key)
                    json_dict.append(students[key])
            elif input[2] == "<=" and len(and_or_cond) < 4 and and_or_cond[4] != "and" and and_or_cond[4] != "or":
                if int(input[3]) >= int(students[key]["grade"]):
                    keys_to_delete.append(key)
                    json_dict.append(students[key])
            if and_or_cond[4] == "and":
                if input[3] == students[key]["name"] and input[6] == students[key]["lastname"]:
                    keys_to_delete.append(key)
                    json_dict.append(students[key])
                if input[3] == students[key]["name"] and input[6] == ">":
                    if int(input[7]) < int(students[key]["grade"]):
                        keys_to_delete.append(key)
                        json_dict.append(students[key])
                if input[3] == students[key]["name"] and input[6] == "<":
                    if int(input[7]) > int(students[key]["grade"]):
                        keys_to_delete.append(key)
                        json_dict.append(students[key])
                if input[3] == students[key]["name"] and input[6] == "=":
                    if int(input[7]) == int(students[key]["grade"]):
                        keys_to_delete.append(key)
                        json_dict.append(students[key])
                if input[3] == students[key]["name"] and input[6] == "!=":
                    if int(input[7]) != int(students[key]["grade"]):
                        keys_to_delete.append(key)
                        json_dict.append(students[key])
                if input[3] == students[key]["name"] and input[6] == ">=":
                    if int(input[7]) <= int(students[key]["grade"]):
                        keys_to_delete.append(key)
                        json_dict.append(students[key])
                if input[3] == students[key]["name"] and input[6] == "<":
                    if int(input[7]) >= int(students[key]["grade"]):
                        keys_to_delete.append(key)
                        json_dict.append(students[key])
                if input[3] == students[key]["lastname"] and input[6] == ">":
                    if int(input[7]) < int(students[key]["grade"]):
                        keys_to_delete.append(key)
                        json_dict.append(students[key])
                if input[3] == students[key]["lastname"] and input[6] == "<":
                    if int(input[7]) > int(students[key]["grade"]):
                        keys_to_delete.append(key)
                        json_dict.append(students[key])
                if input[3] == students[key]["lastname"] and input[6] == "=":
                    if int(input[7]) == int(students[key]["grade"]):
                        keys_to_delete.append(key)
                        json_dict.append(students[key])
                if input[3] == students[key]["lastname"] and input[6] == "!=":
                    if int(input[7]) != int(students[key]["grade"]):
                        keys_to_delete.append(key)
                        json_dict.append(students[key])
                if input[3] == students[key]["lastname"] and input[6] == ">=":
                    if int(input[7]) <= int(students[key]["grade"]):
                        keys_to_delete.append(key)
                        json_dict.append(students[key])
                if input[3] == students[key]["lastname"] and input[6] == "<":
                    if int(input[7]) >= int(students[key]["grade"]):
                        keys_to_delete.append(key)
                        json_dict.append(students[key])
            if and_or_cond[4] == "or":
                if input[3] == students[key]["name"] or input[6] == students[key]["lastname"]:
                    keys_to_delete.append(key)
                    json_dict.append(students[key])
                elif input[3] == students[key]["name"] or input[6] == ">":
                    if int(input[7]) < int(students[key]["grade"]):
                        keys_to_delete.append(key)
                        json_dict.append(students[key])
                elif input[3] == students[key]["name"] or input[6] == "<":
                    if int(input[7]) > int(students[key]["grade"]):
                        keys_to_delete.append(key)
                        json_dict.append(students[key])
                elif input[3] == students[key]["name"] or input[6] == "=":
                    if int(input[7]) == int(students[key]["grade"]):
                        keys_to_delete.append(key)
                        json_dict.append(students[key])
                elif input[3] == students[key]["name"] or input[6] == "!=":
                    if int(input[7]) != int(students[key]["grade"]):
                        keys_to_delete.append(key)
                        json_dict.append(students[key])
                elif input[3] == students[key]["name"] or input[6] == ">=":
                    if int(input[7]) <= int(students[key]["grade"]):
                        keys_to_delete.append(key)
                        json_dict.append(students[key])
                elif input[3] == students[key]["name"] or input[6] == "<":
                    if int(input[7]) >= int(students[key]["grade"]):
                        keys_to_delete.append(key)
                        json_dict.append(students[key])
                elif input[3] == students[key]["lastname"] or input[6] == ">":
                    if int(input[7]) < int(students[key]["grade"]):
                        keys_to_delete.append(key)
                        json_dict.append(students[key])
                elif input[3] == students[key]["lastname"] or input[6] == "<":
                    if int(input[7]) > int(students[key]["grade"]):
                        keys_to_delete.append(key)
                        json_dict.append(students[key])
                elif input[3] == students[key]["lastname"] or input[6] == "=":
                    if int(input[7]) == int(students[key]["grade"]):
                        keys_to_delete.append(key)
                        json_dict.append(students[key])
                elif input[3] == students[key]["lastname"] or input[6] == "!=":
                    if int(input[7]) != int(students[key]["grade"]):
                        keys_to_delete.append(key)
                        json_dict.append(students[key])
                elif input[3] == students[key]["lastname"] or input[6] == ">=":
                    if int(input[7]) <= int(students[key]["grade"]):
                        keys_to_delete.append(key)
                        json_dict.append(students[key])
                elif input[3] == students[key]["lastname"] or input[6] == "<":
                    if int(input[7]) >= int(students[key]["grade"]):
                        keys_to_delete.append(key)
                        json_dict.append(students[key])

    input = command[0:len(command)].split(" ")
    input1 = input[1].split(",")
    for key in students.keys():
        if input[0] == "SELECT" and (input1[0] == "name" or input1[1] == "lastname") and (
                input[9] == "name" or input[9] == "lastname"):
            if input[6] == ">":
                if int(input[7]) < int(students[key]["grade"]) and (
                        input[11] == students[key]["name"] or input[11] == students[key]["lastname"]):
                    keys_to_select.append(key)
                    json_dict.append(students[key])
            if input[6] == "<":
                if int(input[7]) > int(students[key]["grade"]) and (
                        input[11] == students[key]["name"] or input[11] == students[key]["lastname"]):
                    keys_to_select.append(key)
                    json_dict.append(students[key])
            if input[6] == "=":
                if int(input[7]) == int(students[key]["grade"]) and (
                        input[11] == students[key]["name"] or input[11] == students[key]["lastname"]):
                    keys_to_select.append(key)
                    json_dict.append(students[key])
            if input[6] == ">=":
                if int(input[7]) <= int(students[key]["grade"]) and (
                        input[11] == students[key]["name"] or input[11] == students[key]["lastname"]):
                    keys_to_select.append(key)
                    json_dict.append(students[key])
            if input[6] == "<=":
                if int(input[7]) >= int(students[key]["grade"]) and (
                        input[11] == students[key]["name"] or input[11] == students[key]["lastname"]):
                    keys_to_select.append(key)
                    json_dict.append(students[key])
            if input[6] == "!=":
                if int(input[7]) != int(students[key]["grade"]) and (
                        input[11] == students[key]["name"] or input[11] == students[key]["lastname"]):
                    keys_to_select.append(key)
                    json_dict.append(students[key])
        elif input[0] == "SELECT" and (input1[0] == "name" or input1[1] == "lastname") and (
                input[9] != "name" or input[9] != "lastname"):
            if input[6] == ">":
                if int(input[7]) > int(students[key]["grade"]):
                    print("dsaf")
                    keys_to_select.append(key)
                    json_dict.append(students[key])
            if input[6] == "<":
                if int(input[7]) < int(students[key]["grade"]):
                    keys_to_select.append(key)
                    json_dict.append(students[key])
            if input[6] == "=":
                if int(input[7]) == int(students[key]["grade"]):
                    keys_to_select.append(key)
                    json_dict.append(students[key])
            if input[6] == ">=":
                if int(input[7]) >= int(students[key]["grade"]):
                    keys_to_select.append(key)
                    json_dict.append(students[key])
            if input[6] == "<=":
                if int(input[7]) <= int(students[key]["grade"]):
                    keys_to_select.append(key)
                    json_dict.append(students[key])
            if input[6] == "!=":
                if int(input[7]) != int(students[key]["grade"]):
                    keys_to_select.append(key)
                    json_dict.append(students[key])


json_object = json.dumps(json_dict, indent = 4)

with open("students.json", "w") as outfile:
    outfile.write(json_object)






print(keys_to_delete)
for i in keys_to_delete:
    students.pop(i)
print(keys_to_select)
for i in keys_to_select:
    students.pop(i)
