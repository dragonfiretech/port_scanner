import sys
from pyfiglet import Figlet
import datetime
import socket

f = Figlet(font='digital')
fs = Figlet(font='epic')
print(f.renderText("***********************************"))
print(fs.renderText("Dragon Port Scanner"))
print(f.renderText("***********************************"))

#text file
scn_fl = open("port scan.txt", "w")
scn_fl.write("here it is!\n\n")

#ask user for target
target = input("Host input:")
host_ip = socket.gethostbyname(target)
print("{} : {}".format(target, host_ip))

#print banner
print("please wait, scanning remote host -", host_ip)
print("-" * 50)

#time scan started
t1 = datetime.datetime.now()
print(t1)
scn_fl.write("starting time is" + str(t1) + "\n\n")

port = 1

#setup for scan loop
port = 1

try:

    for port in range(1, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.1)
        result = sock.connect_ex((host_ip, port))
        if result == 0:
            print("port {}: open".format(port))

            sock.close()

except KeyboardInterrupt:
    print("you pressed ctrl+c, exiting...")
    sys.exit()
except socket.gaierror:
    print('hostname could not be resolved. exiting...')
    sys.exit()
except socket.error:
    print("could not connect to server, exiting...")
    sys.exit()
finally:
    print('this is always executed')

#checking start time
t2 = datetime.datetime.now()
print(t2)
scn_fl.write("ending time is" + str(t2) + "\n\n")

#time for scan
t3 = t2 - t1

#print info on screen
scn_fl.write("the start time was {t1}\n the ending time was {t2}\n total time for scan {t3}\n")
print("Scan start time was {}\nScan end time was {}\nScan total time was {}\n".format(t1, t2, t3))

print(t3)
print("EAT A DICK")

scn_fl.close()

