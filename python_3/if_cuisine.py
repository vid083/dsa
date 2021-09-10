indian = ["samosa", "kachori"]
italian = ["pizza", "pasta"]
chinese = ["fried rice", "noodles"]

dish = input("Enter a dish name: ")

if dish in indian:
    print("indian")

elif dish in italian:
    print("italian")

elif dish in chinese:
    print("chinese")

else:
    print("i dnt know")

