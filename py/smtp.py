import smtplib
import ssl
import datetime
from email.message import EmailMessage
from pathlib import Path
import json
import os

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

relative_path = [Path('ansible/py/url_status.txt'), Path('json/.json')]
txtfl = relative_path[0].resolve()
json_file_path = relative_path[1].resolve()

with open(json_file_path, "r") as f:
	data = json.load(f)
	boop = data['boop']
	sender = data['sender']
	recipient = data['recipient']

dt = datetime.datetime.now()
dt_sign =(dt.strftime("%c"))

subject = 'Beep, Ansible reminder - Daily URL Status Check!'
with open(txtfl, 'r') as f:
	textfile = f.read()
	
message = """\
From: %s
To: %s
Subject: %s

URL links status:

%s

%s
""" % (sender, (recipient), subject, textfile, dt_sign)

if __name__ == "__main__":
  smtp(sender, recipient, subject, textfile, dt_sign)
