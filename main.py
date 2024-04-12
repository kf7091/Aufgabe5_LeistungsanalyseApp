import json
import my_functions as mf
#Erstellung des Probanden
subject = mf.build_person(
    input("Geben Sie den Vornamen des Probande:in ein:"),
    input("Geben Sie den Nachnamen des Probande:in ein:"),
    input("Geben sie das Geschlecht 'male' oder 'female' an:"),
    int(input("Geben Sie das Alter des Probande:in ein:"))
   )
#Erstellung des Supervisors
supervisor = mf.build_person(
    input("Geben Sie den Vornamen des Supervisors ein:"),
    input("Geben Sie den Nachnamen des Supervisors ein:"),
    input("Geben sie das Geschlecht des Supervisors 'male' oder 'female' an:"),
    int(input("Geben Sie das Alter des Supervisors ein:"))
)
#Input für Datum und Experimentname             
experiment = mf.build_experiment(
    input("Geben Sie den Experimentnamen ein:"),
    input("Geben Sie das Datum ein:"),
    supervisor,
    subject
)

# Convert and write JSON object to file
with open("data.json", "w") as outfile: 
    json.dump(experiment, outfile)
    print("JSON-Datei mit folgenden Inhalt wurde erstellt:\n", experiment)
