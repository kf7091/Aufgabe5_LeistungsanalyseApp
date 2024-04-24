from datetime import datetime
import myclasses as mc

#create subject
subject = mc.Subject(
    input("Geben Sie den Vornamen des Probande:in ein:"),
    input("Geben Sie den Nachnamen des Probande:in ein:"),
    input("Geben sie das Geschlecht 'male' oder 'female' an:"),
    datetime.strptime(input("Geben Sie das Geburtsdatum des Probanden ein:"), '%d.%m.%Y')
   )

#create supervisor
supervisor = mc.Supervisor(
    input("Geben Sie den Vornamen des Supervisors ein:"),
    input("Geben Sie den Nachnamen des Supervisors ein:"),
)

#create experiment            
experiment = mc.Experiment(
    input("Geben Sie den Experimentnamen ein:"),
    datetime.strptime(input("Geben Sie das Datum ein:"), '%d.%m.%Y'),
    supervisor.__dict__,
    subject.__dict__
)

experiment.save()