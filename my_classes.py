import my_functions as mf
import json
import datetime
import my_classes

class Person:
    def __init__(self, first_name, last_name): 
        self.first_name = first_name
        self.last_name = last_name
        self.__dict__ = {"first_name":self.first_name, "last":self.last_name}

    def save(self, filename):
        with open(filename, "w") as outfile: 
            json.dump(self.__dict__, outfile)


class Subject(Person):
    def __init__(self, first_name, last_name, birthdate, sex):
        super().__init__(first_name, last_name)
        self.sex = sex
        self.__birthdate  = birthdate
        self.age = mf.calculate_age(birthdate)
        self.heartrate = mf.estimate_max_hr(self.age, sex)



class Supervisor(Person):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
   
 
class Experiment:
    def __init__(self, name, date, supervisor, subject):
        self.name = name
        self.date = date
        self.supervisor = supervisor
        self.subject = subject
        __dict__ = {"name":self.name, "date":self.date, "supervisor":self.supervisor.__dict__, "subject":self.subject.__dict__}
    def save(self, filename):
        with open(filename, "w") as outfile: 
            json.dump(self, outfile)

