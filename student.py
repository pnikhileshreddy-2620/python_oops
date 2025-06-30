class Student:
    def __init__(self, sname,sid, saddress, sphone):
        self.sname= sname
        self.sid=sid
        self._saddress=saddress
        self.__sphone=sphone
    """"Using setter and getter """
    def get_sadress(self):
        return self._saddress
    def set_sphone(self,sphone):
        self.__sphone=sphone
    def get_sphone(self):
        return self.__sphone

my_student=Student("Nikhilesh",1,"NLR","123456789")
print(my_student.get_sadress())
my_student.set_sphone("098765432")
LIST=[my_student]
for student in LIST:
    print(student.get_sadress(),student.get_sphone())