class student:
    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks
    def display(self):
        print("name:",self.name,"\troolno:",self.rollno,"\tmarks:",self.marks)
def display_all(students):
    if(len(students)==0):
        print("There are no students")
    else:
        for i in students:
            i.display()
def add_student(students):
    n=input("Name of the student: ")
    r=int(input("Roolno: "))
    for i in students:
        if i.rollno == r:
            print("Roll number already exists")
            return
    m=int(input("marks: "))
    s=student(n,r,m)
    students.append(s)
    print("student added sucessfully")
def search(students):
    r=int(input("Enter the rollno of the student you want to search: "))
    for i in students:
        if(i.rollno==r):
            i.display()
            break
    else:
        print("There is no student with that rollno")
def update(students):
    r=int(input("Enter the rollno of the student you want to update marks: "))
    m=int(input("input new marks: "))
    for i in students:
        if(i.rollno==r):
            i.marks=m
            print("marks updated sucessfully")
            i.display()
            break
    else:
        print("student not found")
def delete(students):
    r=int(input("Enter the rollno of the student you want to delete: "))
    for i in students:
        if(i.rollno==r):
            students.remove(i)
            print("student deleted sucessfully")
            break
    else:
        print("student not found")
def average(s):
    if(len(s)==0):
        print("no students available")
    else:
        tot=0
        for i in s:
            tot=tot+i.marks
        print("average marks of students: ",float(tot/len(s)))
def top(s):
    if(len(s)==0):
        print("no student found")
    else:
        maxx=s[0].marks
        for i in s:
            if(i.marks>maxx):
                maxx=i.marks
        for i in s:
            if(maxx==i.marks):
                i.display()
def load_students(students):
    try:
        with open("student file.txt","r") as f:
            for l in f:
                part=l.strip().split(",")
                n=part[0]
                r=int(part[1])
                m=int(part[2])
                s=student(n,r,m)
                students.append(s)
    except FileNotFoundError:
        print("File not found")
def save(s):
    with open("student file.txt","w") as f:
        for i in s:
            f.write(i.name+","+str(i.rollno)+","+str(i.marks)+"\n")
students=[]
load_students(students)
while(True):
    print("1.Add student\n2.view all students\n3.search student\n4.update marks\n5.delete student\n6.average\n7.top scorer\n8.Exit")
    choice=int(input("enter choice: "))
    if(choice==1):
        add_student(students)
    elif(choice==2):    
        display_all(students)
    elif(choice==3):
        search(students)
    elif(choice==4):
        update(students)
    elif(choice==5):
        delete(students)
    elif(choice==6):
        average(students)
    elif(choice==7):
        top(students)
    elif(choice==8):
        save(students)
        print("Thank you")
        break
    else:
        print("Try numbers between 1 and 8")