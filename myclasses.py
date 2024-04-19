import json
import os
from datetime import datetime

class Person():  
    def __init__(self, first_name : str, last_name : str, sex : str, age : int):
        self.first_name : str = first_name
        self.last_name : str = last_name
        self.sex : str = sex
        self.age : int = age
        self.est_max_hr : int = self.estimate_max_hr()
    
    #estimating the maximum heart rate with standard formulas
    def estimate_max_hr(self) -> int:
        """
        See https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4124545/ for different formulas
        """
        if self.sex == "male":
            max_hr_bpm =  223 - 0.9 * self.age
        elif self.sex == "female":
            max_hr_bpm = 226 - 1.0 *  self.age
        else:
            # der input() öffnet ein Eingabefenster für den Nutzer und speichert die Eingabe
            max_hr_bpm  = input("Enter maximum heart rate:")
        return int(max_hr_bpm)
    
    def save(self):
        '''
        saves the person object as a json file in the output/persons folder
        '''
        #creating the subfolder for the persons if it does not exist
        subfolder : str = "persons"
        if not os.path.exists("output"): os.makedirs("output")
        if not os.path.exists(os.sep.join(["output", subfolder])): os.makedirs(os.sep.join(["output", subfolder]))

        #writing the json file
        with open(os.sep.join(["output", subfolder, f"{self.first_name}_{self.last_name}.json"]), "w") as outfile: 
            json.dump(self.__dict__, outfile)
            print(f"JSON-Datei mit folgenden Inhalt wurde wurde in {os.sep.join(["output", subfolder])} erstellt:\n", self.__dict__)


class Experiment():
    def __init__(self, experiment_name : str, date : datetime, supervisor : dict, subject : dict):
        self.experiment_name : str = experiment_name
        self.date : str = date.strftime("%Y.%m.%d")
        self.supervisor : dict = supervisor
        self.subject : dict = subject

    def save(self):
        '''
        saves the experiment object as a json file in the output/experiments folder
        '''
        #creating the subfolder for the experiments if it does not exist
        subfolder : str = "experiments"
        if not os.path.exists("output"): os.makedirs("output")
        if not os.path.exists(os.sep.join(["output", subfolder])): os.makedirs(os.sep.join(["output", subfolder]))

        #writing the json file
        with open(os.sep.join(["output", subfolder, f"{self.date}_{self.experiment_name}.json"]), "w") as outfile: 
            json.dump(self.__dict__, outfile)
            print(f"JSON-Datei für diese Experiment mit folgenden Inhalt wurde wurde in {os.sep.join(["output", subfolder])} erstellt:\n", self.__dict__)