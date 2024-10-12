"""
grade = int(input("Enter your grade: "))
if grade > 96:
    print("1.0")
elif grade <= 96 and grade >= 94:
    print("1.25")
elif grade <= 93 and grade >= 91:
    print("1.5")
elif grade <= 90 and grade >= 87:
    print("1.75")
elif grade <= 86 and grade >= 84:
    print("2.0")
elif grade <= 83 and grade >= 81:
    print("2.25")
elif grade <= 80 and grade >= 78:
    print("2.50")
elif grade <= 77 and grade >= 75:
    print("2.75")
elif grade <= 74 and grade >= 72:
    print("3.0") 
"""
grade = int(input("Enter your grade: "))

if grade > 96:
    print("1.0")
elif grade <= 96 and grade >= 94:
    print("1.25")
elif grade <= 93 and grade >= 91:
    print("1.5")
elif grade <= 90 and grade >= 88:
    print("1.75")
elif grade <= 87 and grade >= 85:
    print("2.0")
elif grade <= 84 and grade >= 82:
    print("2.25")
elif grade <= 81 and grade >= 79:
    print("2.5")
elif grade <= 78 and grade >= 75:
    print("2.75")
elif grade == 75:
    print("3.0")
elif grade <= 74 and grade >= 60:
    print("4.0")
else:
    print("5.0")
