
import RPi.GPIO as GPIO    # Import GPIO Library
import time                # Import time library
from time import sleep
import smtplib             # Import smtplib Library
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

GPIO.setmode(GPIO.BOARD)   # Use Physical Pin Numbering Scheme

switch1=16                 # Switch 1 is connected to physical pin 16
switch2=12                 # Switch 2 is connected to physical pin 12
switch3=31                 # Switch 3 is connected to physical pin 31
switch4=37                 # Switch 4 is connected to physical pin 37

GPIO.setup(switch1,GPIO.IN) # Make switch 1 an input
GPIO.setup(switch2,GPIO.IN) # Make switch 2 an input
GPIO.setup(switch3,GPIO.IN) # Make switch 3 an input
GPIO.setup(switch4,GPIO.IN) # Make switch 4 an input

BS1=False                  # Set Flag BS1 to indicate Switch is initially off
BS2=False                  # Set Flag BS2 to indicate Switch is initially off
BS3=False                  # Set Flag BS3 to indicate Switch is initially off
BS4=False                  # Set Flag BS4 to indicate Switch is initially off

''' Text Message email Function
Below is the function to send an email text message to the 
owners supplied phone number and cellular provider.
'''

def email_text(message):
    curtime = time.strftime("%c")

    fromaddr = "emailaddress@tosendmsgfrom"
    toaddr = "emailaddress@tosendmsgto"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = ""
 
    body = ( message + "\n" + curtime )
    msg.attach(MIMEText(body, 'plain'))
 
    server = smtplib.SMTP('smtp.gmail.com', 587)    # for gmail account
    server.starttls()
    server.login(fromaddr, "passwordforemailaccount")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()


try:
    while(1):                  # Create an infinite Loop
        if GPIO.input(switch1)==1:            # Look for switch 1 position
            if BS1==True:                # If the switch is on
                sleep(.5)             # Delay
            elif BS1==False:                         # If the switch is off
                email_text('Generator is running') #Run function to send txt
#                print("Generator is running")
                BS1=True               # Set Flag to show switch is now on
                sleep(.5)
        if GPIO.input(switch1)==0:            # Look for switch 1 position
            if BS1==False:                # If the switch is off
                sleep(.5)             # Delay
            elif BS1==True:                         # If the switch is on
                email_text('Generator has stopped') #Run function to send txt
#                print("Generator has stopped")
                BS1=False               # Set Flag to show switch is now Off
                sleep(.5)
        if GPIO.input(switch2)==1:            # Look for swtich 2 position
            if BS2==True:                # If the switch 2 is on
                sleep(.5)             # Delay
            elif BS2==False:                         # If the switch is off
                email_text('Generator has an Alarm Warning') #Run function to send txt
#                print("Generator has an Alarm Warning")
                BS2=True               # Set Flag to show switch is now On
                sleep(.5)
        if GPIO.input(switch2)==0:            # Look for switch 2 position
            if BS2==False:                # If the switch is off
                sleep(.5)             # Delay
            elif BS2==True:                         # If the switch is on
                email_text('Generator Alarm Warning is reset') #Run function to send txt
#                print("Generator Alarm Warning is reset")
                BS2=False               # Set Flag to show switch is now Off
                sleep(.5)
        if GPIO.input(switch3)==1:
            if BS3==True:
                sleep(.5)
            elif BS3==False:
                email_text('Generator has an Alarm Shutdown')
#                print("Generator has an Alarm Shutdown")
                BS3=True
                sleep(.5)
        if GPIO.input(switch3)==0:
            if BS3==False:
                sleep(.5)
            elif BS3==True:
                email_text('Generator Alarm Shutdown is reset')
#                print("Generator Alarm Shutdown is reset")
                BS3=False
                sleep(.5)
        if GPIO.input(switch4)==1:
            if BS4==True:
                sleep(.5)
            elif BS4==False:
                email_text('Generator is in Automatic Operation')
#                print("Generator IS in Automatic Operation")
                BS4=True
                sleep(.5)
        if GPIO.input(switch4)==0:
            if BS4==False:
                sleep(.5)
            elif BS4==True:
                email_text('Generator is NOT in Automatic Operation')
#                print("Generator is NOT in Automatic Operation")
                BS4=False
                sleep(.5)
except KeyboardInterrupt:
    GPIO.cleanup()
