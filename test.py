from datetime import datetime
import myclasses as mc

#create subject
subject = mc.Subject(
    "Max",
    "Mustermann",
    "male",
    datetime.strptime("01.01.2001", '%d.%m.%Y'),
    "maxi@mustermann.at"
   )
#create supervisor
supervisor = mc.Supervisor(
    "Herbert",
    "Müller",
)
#create experiment            
experiment = mc.Experiment(
    "Experiment 1",
    datetime.strptime("24.4.2024", '%d.%m.%Y'),
    supervisor.__dict__,
    subject.__dict__
)
print(datetime.strptime("24.4.1930", '%d.%m.%Y'))

experiment.save()
subject.save()
supervisor.save()

server_ip = "localhost"
server_port = 5000
subject.put(server_ip, server_port)
supervisor.put(server_ip, server_port)
subject.update_email("max@mustermann.at", server_ip, server_port)
