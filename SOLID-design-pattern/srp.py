import sqlite3
from sqlite3 import Error
from typing import Dict, List
import logging
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

"""
under SOLID principles , the first principle is to define methods , 
functions, classes with single responsibility method
"""
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%m/%d/%Y %H:%M:%S",
)


class User:
    def registeruser(self, uname: str, passwd: str, email: str):
        # set the sqlite db connection
        con = sqlite3.connect("userdb")
        # insert data into db
        sql = "insert into Users values ( '{0}' , '{1}' , '{2}' )".format(
            uname, passwd, email
        )
        con.execute(sql)
        con.commit()
        print(f"User Registered with {uname} and {passwd}")


# define the logging module
class Logger:
    def __init__(self) -> None:
        # define the logger
        self.logger = logging.getLogger(__name__)
        # add a handler
        file_handler = logging.FileHandler(filename="errors.log")
        # set logging level to the file handler
        file_handler.setLevel(level=logging.ERROR)
        # set log message format
        file_handler.setFormatter(
            logging.Formatter("%(name)s - %(levelname)s - %(message)s")
        )
        # attach the handler to the logger
        self.logger.addHandler(file_handler)

    def writeError(self, message: str) -> None:
        self.logger.error(msg=message)


# send email
class Email:
    def __init__(self) -> None:
        self.sender_email = "himasha0421@gmail.com"
        self.sg = SendGridAPIClient(api_key=os.environ.get("SENDGRID_API_KEY"))

    def send(
        self, to_email: str, message_content: str, subject: str = "User Registration"
    ) -> None:
        message = Mail(
            from_email=self.sender_email,
            to_emails=to_email,
            subject=subject,
            html_content=f"<strong>{message_content}  and easy to do anywhere, even with Python</strong>",
        )

        try:
            response = self.sg.send(message)  # type: ignore
            print(response.body)  # type: ignore
            print("Email Sent !!")

        except Exception as e:
            print(e.message)  # type: ignore


# apply facade design pattern
class RegistrationPortal:
    def __init__(self) -> None:
        self.logger = Logger()
        self.email_client = Email()

    def register(self, uname: str, pwd: str, email: str) -> None:
        try:
            # get the user into the db
            User().registeruser(uname=uname, passwd=pwd, email=email)
            # send the email
            self.email_client.send(
                to_email="himasha0421@gmail.com",
                message_content="Himasha J96",
            )

        except:
            self.logger.writeError(message="Error while Registering User ")


# run the application
if __name__ == "__main__":
    # define the portal
    portal = RegistrationPortal()
    # add a user
    portal.register(
        uname="Thamali Vidange", pwd="mora54637", email="himasha0421@gmail.com"
    )
