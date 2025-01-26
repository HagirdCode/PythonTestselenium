employee_salaries = { 
    "rushikesh" : 4000,
    "nitin" : 5000,
    "nagesh" : 6000,
    "nita" : 7000}
for name in employee_salaries : employee_salaries[name] += employee_salaries [name] * 0.10

total_salary = sum (employee_salaries.values())
avrage_salary = total_salary / len (employee_salaries)

print (f"avrage_salary:{avrage_salary}")

various_keys = {
"A" : 1,
"b" : 2,
"c" : 3,}
various_keys2 = {
"A" : 2,
"b" : 3,
"c" : 1
}

# various_keys.update(various_keys2)
# print(various_keys)

# merged_dict = {**various_keys, **various_keys2}
# print(merged_dict)

merged_dict = various_keys | various_keys2
print(merged_dict)


# Imporatant methods to merge two dictionaries 
# Summary:
# 1. update() modifies the first dictionary in place.
# 2. ** unpacking creates a new dictionary by combining both dictionaries.
# 3. | (available in Python 3.9+) provides a concise and intuitive way to merge dictionaries.