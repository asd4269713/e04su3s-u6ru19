class Member:
    def __init__(self,new_gender, new_major, new_id):
        self.__gender = new_gender#__代表PRIVATE
        self.major = new_major
        self.id = new_id
    def set_gender(self,new__gender):
        if new__gender == 'M' or new__gender=='F':
            self.__gender = new__gender
        else:
            print('請輸入M|F')
    def get_gender(self):
        return self.__gender
    def join_class(self):
        pass
    def quit_class(self):
        pass
    def borrow_resources(self):
        pass
class Student(Member):
    def __init__(self,new_gender, new_major, new_id):
        super().__init__(new_gender, new_major, new_id)
    def borrow_resources(self):
        print("students borrow")
class Professor(Member):
    def __init__(self,new_gender, new_major, new_id):
        super().__init__(new_gender, new_major, new_id)
    def borrow_resources(self):
        print("professor borrow")
studentA = Student('M','IEM','B10721155')
studentB = Student('W','DCC','B10721055')
ProfessorA = Professor('M','BA','PPP10721155')
ProfessorB = Professor('W','FA','AAA10721055')
studentA.set_gender('dog')
print(studentA.get_gender())
ls = [studentA,studentB,ProfessorA,ProfessorB]
for item in ls:
    item.borrow_resources()

