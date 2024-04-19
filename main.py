from datetime import datetime
import myclasses as mc

#create subject
subject = mc.Person(
    input("Geben Sie den Vornamen des Probande:in ein:"),
    input("Geben Sie den Nachnamen des Probande:in ein:"),
    input("Geben sie das Geschlecht 'male' oder 'female' an:"),
    int(input("Geben Sie das Alter des Probande:in ein:"))
   )
#create supervisor
supervisor = mc.Person(
    input("Geben Sie den Vornamen des Supervisors ein:"),
    input("Geben Sie den Nachnamen des Supervisors ein:"),
    input("Geben sie das Geschlecht des Supervisors 'male' oder 'female' an:"),
    int(input("Geben Sie das Alter des Supervisors ein:"))
)
#create experiment            
experiment = mc.Experiment(
    input("Geben Sie den Experimentnamen ein:"),
    datetime.strptime(input("Geben Sie das Datum ein:"), '%d.%m.%y'),
    supervisor.__dict__,
    subject.__dict__
)

experiment.save()