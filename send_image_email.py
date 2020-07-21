import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def email():
    fromaddr = "The Email Address you'r sending from"
    toaddr = "The Email Address you'r sending it to"

    msg = MIMEMultipart()

    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "SUBJECT OF THE EMAIL"

    body = "TEXT YOU WANT TO SEND"

    msg.attach(MIMEText(body, 'plain'))

    filename = "name of the picture you want to send, e.g snippet0.png"
    attachment = open("the path file to where the picture is saved, e.g C:\\Users\\Name\\Pictures\\snippet0.png ", "rb")

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "your password")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()


email()