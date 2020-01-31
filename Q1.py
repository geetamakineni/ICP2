lst_lb = []
lst_kg = []
n = int(input("enter the number of students:"))
print("Enter the Weights of students in lbs:")
for j in range(n):
    elements = int(input())
    lst_lb.append(elements)
lst_kg=[lst_lb[j]*(0.453514) for j in range(n)]
print("The weights of students in kgs are:", lst_kg)
