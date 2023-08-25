gender=input("Enter the gender of the baby,")
h_value=int(input("Enter the hemoglobin value of the baby="))
if gender=="Male":
    if h_value<117:
        print("The hemoglobin levels are too low for this one")
    if h_value>155:
        print("The hemoglobin levels are too high for this one")
    else:
        print("The hemoglobin levels are satisfactory")
if gender=="Female":
    if h_value<134:
        print("The hemoglobin levels are too low for this one")
    if h_value>167:
        print("The hemoglobin levels are too high for this one")
    else:
        print("The hemoglobin levels are satisfactory")