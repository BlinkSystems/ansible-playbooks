import smtplib
import ssl
import datetime
from email.message import EmailMessage
import hashlib
import os

import os
import hashlib
 
def create_secure_password(password):
  salt = os.urandom(16)
  iterations = 100_000 
  hash_value = hashlib.pbkdf2_hmac(
    'sha256',  
    password.encode('utf-8'), 
    salt, 
    iterations
  )
  password_hash = salt + hash_value
  return password_hash
 

sender = "robot@blinkprods.com"
recipient = "systemshock@blinkprods.com"
dt = datetime.datetime.now()
dt_sign =(dt.strftime("%c"))

with open('./boop.txt', 'r') as f:
	beep = f.read().replace('\n','')
	print(create_secure_password(beep))


# subject = 'Beep, Ansible reminder of the URL links!'
# with open('./textfile.txt', 'r') as f:
# 	textfile = f.read()


# message = """\
# From: %s
# To: %s
# Subject: %s

# URL links status:

# %s

# %s
# """ % (sender, (recipient), subject, textfile, dt_sign)

# def smtp(sender, recipient, subject, textfile, dt_sign):
# 	port = 587
# 	server = "smtp.gmail.com"

# 	SSL_context = ssl.create_default_context()
# 	with smtplib.SMTP(server, port) as server:
# 	    server.ehlo()
# 	    server.starttls(context=SSL_context)
# 	    server.login(sender, beep)
# 	    server.sendmail(sender, recipient, message)
# 	    server.close()
