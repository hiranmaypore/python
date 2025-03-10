class person():
    def __init__(self):
        super().__init__()
        self.name = input("Enter the name :")
        self.address = input("Enter the address :")
        self.mobile_nunber = input("Enter the mobile_number :")
        
class student(person):
    def __init__(self):
        super().__init__()
        self.department = input("Enter the department :")
        self.roll_number = input("Enter the roll_number :")
        self.year = input("Enter the year :")
        
class employee(person):
    def __init__(self):
        super().__init__()
        self.department = input("Enter the department :")
        self.subject_taken = []
        for i in range (int(input("Enter the number of subjects :"))):
            self.subject_taken.append("Enter the subject name :")
            
Em = []
for i in range(int(input("Enter number of employee :"))):
    ob = employee()
    Em.append(ob)
for i in range(len(Em)):
    print("\nEmployee department =",Em[i].department,"\nEmployee subject_taken =",Em[i].subject_taken)