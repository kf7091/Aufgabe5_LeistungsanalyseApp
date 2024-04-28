import json
import my_classes as mc

#Erstellung des Probanden
subject = mc.Subject(
    first_name=input("Geben Sie den Vornamen des Probande:in ein:"),
    last_name=input("Geben Sie den Nachnamen des Probande:in ein:"),
    birthdate=int(input("Geben Sie das Alter des Probande:in ein:"),
    sex=input("Geben sie das Geschlecht 'male' oder 'female'  an:"),)
   )
#Erstellung des Supervisors
supervisor = mc.Supervisor(
    input("Geben Sie den Vornamen des Supervisors ein:"),
    input("Geben Sie den Nachnamen des Supervisors ein:"),
)

#Input für Datum und Experimentname             
experiment = mc.Experiment(
    name=input("Geben Sie den Experimentnamen ein:"),
    date=input("Geben Sie das Datum ein:"),
    supervisor=supervisor.__dict__,
    subject=subject.__dict__
)

# Convert and write JSON object to file
with open("data.json", "w") as outfile: 
    json.dump(experiment, outfile)
    print("JSON-Datei mit folgenden Inhalt wurde erstellt:\n", experiment)
