import my_functions as mf
import json
import datetime
import my_classes
import requests

class Person:
    def __init__(self, first_name, last_name): 
        self.first_name = first_name
        self.last_name = last_name
        self.__dict__ = {"first_name":self.first_name, "last":self.last_name}
    def put(self):
            
            url = f"http://127.0.0.1:5000/person/{self.first_name}"
            
            data = {"name": self.first_name}
            response = requests.put(url, json=json.dumps(data))
            print(response.text)
            
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
    def update_email(self, email):
        url = f"http://127.0.0.1:5000/person/"
        data = {"name": self.first_name, "email": email}
        response = requests.post(url, json=json.dumps(data))
        print(response.text)


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

