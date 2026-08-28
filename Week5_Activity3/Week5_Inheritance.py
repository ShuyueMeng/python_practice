class person:
    def __init__(self,id,name):
        self.id=id
        self.name=name

class student(person):
    def __init__(self, id, name,student_id):
        super().__init__(id, name)
        self.student_id=student_id

class staff(person):
    def __init__(self,id, name,staff_id,tax_num):
        super().__init__(id,name)
        self.staff_id=staff_id
        self.tax_num=tax_num

class general(staff):
    def __init__(self,id, name,staff_id,tax_num,rate_of_pay):
        super().__init__(id, name,staff_id,tax_num)
        self.rate_of_pay=rate_of_pay
    def show_publications(self):
        print(f"{self.name}'s pay rate is: {self.rate_of_pay}")

class academic(staff):
    def __init__(self,id, name,staff_id,tax_num,publications):
        super().__init__(id, name,staff_id,tax_num)
        self.publications=publications
    def show_publications(self):
        print(f"{self.name} has {self.publications} publications")