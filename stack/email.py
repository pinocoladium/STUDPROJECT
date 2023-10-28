import email
import smtplib
import imaplib
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart


gmail_smtp = "smtp.gmail.com"
gmail_imap = "imap.gmail.com"
login = "login@gmail.com"
password = "qwerty"
subject = "Subject"
recipients = ["vasya@email.com", "petya@email.com"]
message_content = "Message"


class Email(login, password, subject, gmail_smtp, gmail_imap):
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.subject = subject
        self.smtp = gmail_smtp
        self.imap = gmail_imap

    def send_message(self, recipients: list, subject, message_content: str):
        for recipient in recipients:
            message = MIMEMultipart()
            message["From"] = self.login
            message["To"] = recipient
            message["Subject"] = subject
            email.attach(MIMEText(message_content))
            email = smtplib.SMTP(self.smtp, 587)
            email.starttls()
            email.ehlo()
            email.login(self.login, self.password)
            email.sendmail(self.login, email, message.as_string())
            email.quit()

    def recieve_message(self, header="ALL"):
        email = imaplib.IMAP4_SSL(self.imap)
        email.login(self.login, self.password)
        email.list()
        email.select("inbox")
        criterion = f'(HEADER Subject "{header}")'
        result, data = email.uid("search", None, criterion)
        if not data[0]:
            print("There are no letters with current header")
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid("fetch", latest_email_uid, "(RFC822)")
        email_message = email.message_from_string(data[0][1])
        email.logout()


if __name__ == "__main__":
    pass
