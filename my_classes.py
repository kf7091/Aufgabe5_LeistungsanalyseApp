import my_functions as mf
import json

class person:
    def __init__(self, first_name, last, age, sex): 
        self.first_name = first_name
        self.last = last
        self.age = age
        self.sex = sex
        self.heartrate = mf.estimate_max_hr(age, sex)
        __dict__ = {"first_name":self.first_name, "last":self.last}
    def save(self, filename):
        with open(filename, "w") as outfile: 
            json.dump(self, outfile)

            
    
 
class experiment:
    def __init__(self, name, date, supervisor, subject):
        self.name = name
        self.date = date
        self.supervisor = supervisor
        self.subject = subject
        __dict__ = {"name":self.name, "date":self.date, "supervisor":self.supervisor, "subject":self.subject}
    def save(self, filename):
        with open(filename, "w") as outfile: 
            json.dump(self, outfile)