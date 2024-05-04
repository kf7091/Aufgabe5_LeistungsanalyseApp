import my_functions as mf
import json
import my_classes as mc


def main():
    #Erstellung des Probanden

    person = mc.Person(
        first_name=input("Geben Sie den Vornamen des Probande:in ein:"),
        last_name=input("Geben Sie den Nachnamen des Probande:in ein:"),
    )
    subject = mc.Subject(
        first_name=input("Geben Sie den Vornamen des Proband:in ein:"),
        last_name=input("Geben Sie den Nachnamen des Proband:in ein:"),
        sex=input("Geben sie das Geschlecht des Proband:in an:"),
        birthdate=int(input("Geben Sie das Alter des Proband:in ein:")),
    )
    mc.Person.put(person)
    mc.Subject.update_email(subject)

if __name__ == "__main__":
    main()