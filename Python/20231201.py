class Student:
    # Constructor 建構子(建立物件時使用)
    def __init__(self, name, age, student_id, gpa):
        #屬性
        self.name = name
        self.age = age
        self.student_id = student_id
        self.gpa = gpa

    # Getter methods
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_student_id(self):
        return self.student_id

#建立物件
student1 = Student("Joen", 20, "S12345", 3.5)
#建立空物件
student2 = Student()