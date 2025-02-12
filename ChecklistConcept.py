print("Project Name?")
name = input()
print("Supervisor?")
supervisor = input()
print("Date of Survey?\n")
date = input()


print("Project Name: ", name)
print("Supervisor: ", supervisor)
print("Date of Survey: ", date,"\n\n")



percentage = '100%'
total = 0
total2 = 0
Total = 0


def validate_input():
    while True:
        user_input = input("Enter a score between 0 or 1: ")

        try:
            value = int(user_input)

            if value in [0,1]:
                return value
            else:
                print("Error: Enter a valid score.")

        except ValueError:
            user_input = input("Invalid Input Type. Enter an integer.")

# Create a formatted string for the table
def format_row(row):
    return " | ".join(f"{str(item).ljust(width)}" for item, width in zip(row, col_widths))


#-----------------------------------------------------------------------------------------  1
# Table 1

headers = ["General Safety & Health", "Score"]
data = [
    ["Training Records" , ""],
    ["Housekeeping" , ""],
    ["Trash Disposal" , ""],
    ["Medical and First Aid" , ""],
    ["Drinking Water" , ""],
    ["Toilet Facilities" , ""],
    ["Lighting" , ""],
    ["Safety Data Sheets (SDS)" , ""],
    ["Postings: Evacuation and Emergency Procedures" , ""],
    ["Sidewalk Shed Inspections" , ""],
]

# Determine column widths
col_widths = [max(len(str(item)) for item in col) for col in zip(*data, headers)]

print(format_row(headers))
print("-" * (sum(col_widths) + len(col_widths) * 3 - 1))  # Print separator
for row in data:
    print(format_row(row))

print("\n")

print("\n")
# List Array
my_set = {'','','','','','','','','','',''}
my_list = list(my_set)

table = [
    ["General Safety & Health", "Score"],
    ["Training Records" , ""],
    ["Housekeeping" , ""],
    ["Trash Disposal" , ""],
    ["Medical and First Aid" , ""],
    ["Drinking Water" , ""],
    ["Toilet Facilities" , ""],
    ["Lighting" , ""],
    ["Safety Data Sheets (SDS)" , ""],
    ["Postings: Evacuation and Emergency Procedures" , ""],
    ["Sidewalk Shed Inspections" , ""],
]

column_name = "Score"
if column_name in table[0]:
    column_index = table[0].index(column_name)
else:
    raise ValueError(f"Column '{column_name}' not found.")


for row in table[1:]:
    for i in range(len(my_list)):

        #validate_input()
        result = validate_input()

    row[column_index] = result
    my_list[i] = int(result)

    total += sum(my_list)



my_set = set(my_list)

column_index = 1
for row in table[1:]:
    print(row[column_index])

# Calculate column widths
col_widths = [max(len(str(item)) for item in col) for col in zip(*table)]

# Print the table
for row in table:
    print(" | ".join(f"{str(item).ljust(width)}" for item, width in zip(row, col_widths)))

print("Total score: ",total,"%")
Total += total

#-----------------------------------------------------------------------------------------  2
# Table 2

headers2 = ["Personal Protective Equipment", "Score"]
data2 = [
    ["Hard Hats" , ""],
    ["Ear and Eye Protection" , ""],
    ["Respirators and Gas Masks" , ""],
    ["Safety Belts, Harnesses" , ""],
    ["Gloves" , ""],
    ["Others (List) Eye Wash" , ""],
]

# Determine column widths
col_widths = [max(len(str(item)) for item in col) for col in zip(*data2, headers2)]
print("\n\n")
print(format_row(headers2))
print("-" * (sum(col_widths) + len(col_widths) * 3 - 1))  # Print separator
for row in data2:
    print(format_row(row))

print("\n")

print("\n")
# List Array
my_set_2 = {'','','','','','','','','','',''}
my_list_2 = list(my_set_2)

table2 = [
    ["Personal Protective Equipment", "Score"],
    ["Hard Hats", ""],
    ["Ear and Eye Protection", ""],
    ["Respirators and Gas Masks", ""],
    ["Safety Belts, Harnesses", ""],
    ["Gloves", ""],
    ["Others (List) Eye Wash", ""],
]

column_name = "Score"
if column_name in table2[0]:
    column_index = table2[0].index(column_name)
else:
    raise ValueError(f"Column '{column_name}' not found.")


for row in table2[1:]:
    for i in range(len(my_list_2)):

        #validate_input()
        result = validate_input()

    row[column_index] = result
    my_list_2[i] = int(result)

    total2 += sum(my_list_2)



my_set2 = set(my_list_2)

column_index = 1
for row in table2[1:]:
    print(row[column_index])

# Calculate column widths
col_widths = [max(len(str(item)) for item in col) for col in zip(*table2)]

# Print the table
for row in table2:
    print(" | ".join(f"{str(item).ljust(width)}" for item, width in zip(row, col_widths)))

print("Total score: ",total2,"%")
Total += total2
print("\nGrand Total: ", Total, "%")