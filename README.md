# Sachin
This is python code to send mails to recipients mail id stored in csv format file

Libraries used:
1. getpass module to hide the password inputted by the user
2. csv module to access csv format file
3. smtplib and ssl module to make a secure connection to mail server
4. MIMEText to build text i.e. body of mail
5. MIMEMultipart to to build layout of mail i.e. subject,to etc.

This code builds a secure ssl connection to mail server
SMTP_SSL() is used to build secure connection to port 465
