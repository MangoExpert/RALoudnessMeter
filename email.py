import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# # comment implies that the field needs to be filled in

fromaddr = "SoylentFRA@gmail.com"    # from email address
toaddr = "nguyenut@bc.edu"      # destination email address
smtp_user = "SoylentFRA@gmail.com"    # SMTP username used for authentication
smtp_pass = "tim1995weiner"    # SMTP password used for authentication
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Soylent"    # subject

body = "I love Soylent."    # body
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)    # e.g. ('in-v3.mailjet.com', 587)
server.starttls()
server.login(smtp_user, smtp_pass)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
