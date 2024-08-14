import smtplib
import ssl
import datetime
from email.message import EmailMessage
import hashlib
import os
import json
import getpass

user = getpass.getuser()
json_file_path = f"/home/{user}/json/.json"
 
with open(json_file_path, "r") as f:
	data = json.load(f)
	boop = data['boop']
	sender = data['sender']
	recipient = data['recipient']

dt = datetime.datetime.now()
dt_sign =(dt.strftime("%c"))

subject = 'Beep, Ansible reminder of the URL links!'
with open('./textfile.txt', 'r') as f:
	textfile = f.read()
	
message = """\
From: %s
To: %s
Subject: %s

URL links status:

%s

%s
""" % (sender, (recipient), subject, textfile, dt_sign)

def smtp(sender, recipient, subject, textfile, dt_sign):
	port = 587
	server = "smtp.gmail.com"

	SSL_context = ssl.create_default_context()
	with smtplib.SMTP(server, port) as server:
		server.ehlo()
		server.starttls(context=SSL_context)
		server.login(sender, boop)
		server.sendmail(sender, recipient, message)
		server.close()

if __name__ == "__main__":
  smtp(sender, recipient, subject, textfile, dt_sign)
