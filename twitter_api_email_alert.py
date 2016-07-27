import smtplib
from twitter_api_auth import email, password, from_addr, to_addrs


def send_email_alert(error_report):
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(email, password)
    server.sendmail(from_addr, to_addrs, error_report)
    server.quit()


if __name__ == '__main__':
    send_email_alert('testing error random text not important')
