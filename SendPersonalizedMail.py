# Save the excel sheet as .csv file

import getpass      # For hiding password input
import csv      # For reading excel sheet
import smtplib, ssl     # For Security
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

passwordChoice = input("Do your password to be shown on screen Y/N ")

mailServer = input("Type mail server and press Enter :")
CSVFileName = input("Type csv file name and press Enter :")
sender_email = input("Type sender email and press Enter :")
if passwordChoice == 'Y' or passwordChoice == 'y':
    password = input("Type your password and press Enter :")     # Taking password input from user
elif passwordChoice == 'N' or passwordChoice == 'n':
    password = getpass.getpass(prompt="Type your password and press Enter :",stream=None)

message = MIMEMultipart("alternative")

message["Subject"] = input("Enter subject of Email and press Enter :")       # Enter subject here
message["From"] = sender_email                  # Enter Email id from which you want to send

# Create the plain-text and HTML version of your message
text1 = """
Hi """
text2 = """,
We have campaigns of many big brands & startups who want to promote their brand through you.

We have brands like AXE Ticket, Myntra, Amazon, Oneplus6, Samsung, Azar etc. They are looking for either a product/app review or a 20-30 second promotion on YouTube or a simple promotion on other social media channels(Fb, Twitter, Instagram) the budget or pay will vary in both promotions.

If you are interested please share your pricing(that is the amount you charge per review/promotion) and your contact no. (WhatsApp no.) so that we can discuss further details.

Besides sponsorships, we also provide many other features to youtubers like affiliate marketing, event promotions etc.

Please fill the form given in the below link:-

https://goo.gl/forms/pIrEZxYNHNb9azSm2


If you have any query you can contact me at 9560750624 , 9917486405.

Thank you

Team GryNow

www.grynow.com"""

html1 = """
<html>
  <body>
    <img src="https://i.postimg.cc/W3C0FPFK/1.png">


    <p>Hi """
html2 = """,<br>
We have campaigns of many big brands & startups who want to promote their brand through you.
<br><br>We have brands like AXE Ticket, Myntra, Amazon, Oneplus6, Samsung, Azar etc. They are looking for either a product/app review or a 20-30 second promotion on YouTube or a simple promotion on other social media channels(Fb, Twitter, Instagram) the budget or pay will vary in both promotions.
<br><br>If you are interested please share your <b>pricing</b>(that is the amount you charge per review/promotion) and your <b>contact no.</b> (WhatsApp no.) so that we can discuss further details.
<br>Besides sponsorships, we also provide many other features to youtubers like affiliate marketing, event promotions etc.
<br><br><br><b>Please fill the form given in the below link:- </b>
<br><a href="https://goo.gl/forms/pIrEZxYNHNb9azSm2">https://goo.gl/forms/pIrEZxYNHNb9azSm2</a>
<br><br>If you have any query you can contact me at 9560750624 , 9917486405.
<br><br>Thank you
<br>Team GryNow
<br><a href="www.grynow.com">www.grynow.com</a>
  </body>
</html>"""

# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp." + mailServer + ".com", 465, context=context) as server:
    server.login(sender_email, password)
    with open(CSVFileName) as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for name, subs, avg, email, contact, pricing in reader:
            if len(email) > 0 and email.find("@") != -1:
                receiver_email = email

                # Building Message
                text = text1 + f"{name}" + text2
                html = html1 + f"{name}" + html2
                part1 = MIMEText(text, "plain")
                part2 = MIMEText(html, "html")

                message.attach(part1)
                message.attach(part2)
                server.sendmail(sender_email, receiver_email, message.as_string())
