import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def sendmail(subject, body, reply_to_email, reply_to_name, send_to):
    try:
        # Update this line if you are using a sever webmail
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()

        # Replace this line with email and password
        server.login('user@gmail.com', 'password')

        msg = MIMEMultipart('alternative')
        # Replace this line with gmail or webmail email
        msg['From'] = 'user@gmail.com'
        msg['To'] = send_to
        msg['Subject'] = subject
        msg['Reply-To'] = f"{reply_to_name}<{reply_to_email}>"
        msg.attach(MIMEText(body, 'html'))

        server.sendmail(
            # Replace this line with gmail or webmail email
            'user@gmail.com',
            send_to,
            msg.as_string(),
        )

        server.quit()

        return 1
    except:
        return 0


# read html file that contains email template
with open('email.html', 'r') as file:
    data = file.read()

# I added the reply to because traditionally you will not want to receive email to same account you are sending to
# Also depending on the situation you might want a reply to 'support@mail.com' or 'hep@mail.com'
if sendmail('Mail Message', data, 'hello@mail.com', 'hellomail', 'example@gmail.com'):
    print('Message Sent Successfully')
else:
    print('Error Sending Message')