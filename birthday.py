

# Program to send message
# on Instagram using Python.

# importing Bot form instabot library.
from instagrapi import Client
from instagrapi.exceptions import LoginRequired
import logging
from datetime import datetime
import pytz
from Sqlfunc import databaseHandler,credHandler
from secure import decrypt
import os
import shutil
logger = logging.getLogger()
class birthdaySender:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.delfolder = "config"
        self.allgood = self.checkfolder()
        self.ready = self.getinstacreds()

    def checkfolder(self):
        if os.path.exists(self.delfolder):
            shutil.rmtree(self.delfolder)
            return True
        else:
            return True
    def getinstacreds(self):
        pdat = credHandler()
        data = pdat.completedata("INSTAGRAM")
        self.username = data[0][0]
        self.password = decrypt(bytes(data[0][1].encode()))
        return True


    def getpassword(self):
        pass

    def change_password_handler(self,username):
    # Simple way to generate a random string
        chars = list("abcdefghijklmnopqrstuvwxyz1234567890!&£@#")
        password = "".join(random.sample(chars, 8))
        return password

    def send_messages(self,username,message):
        cl = Client()
        session = cl.load_settings("session.json")

        login_via_session = False
        login_via_pw = False

        if session:
            try:
                cl.set_settings(session)
                cl.login(self.username, self.password)
                send_to = cl.user_id_from_username(username=username)
                cl.direct_send(text=message, user_ids=[send_to])

                # check if session is valid
                try:
                    cl.get_timeline_feed()
                except LoginRequired:
                    logger.info("Session is invalid, need to login via username and password")

                    old_session = cl.get_settings()

                    # use the same device uuids across logins
                    cl.set_settings({})
                    cl.set_uuids(old_session["uuids"])
                login_via_session = True
            except Exception as e:
                logger.info("Couldn't login user using session information: %s" % e)

        if not login_via_session:
            try:
                logger.info("Attempting to login via username and password. username: %s" % self.username)
                if cl.login(self.username, self.password):
                    login_via_pw = True
            except Exception as e:
                logger.info("Couldn't login user using username and password: %s" % e)

        if not login_via_pw and not login_via_session:
            raise Exception("Couldn't login user with either password or session")
            cl = Client()
            cl.change_password_handler = self.change_password_handler
        

    def checkdate(self,date):
        datetime_in_India = datetime.now(pytz.timezone('Asia/Kolkata'))
        strtime = datetime_in_India.strftime('%m-%d')
        date = date[5:]
        if strtime == date:
            return True
        else:
            return False
    def msgsender(self,data):
        if self.onetimechecker():
            for row in data:
                username = row[0]
                message = row[3]
                date = row[2]
                if self.checkdate(date):
                    self.send_messages(username,message)
                    self.tick()
                else:
                    pass
        else:
            pass

    def onetimechecker(self):
        datetime_in_India = datetime.now(pytz.timezone('Asia/Kolkata'))
        strtime = datetime_in_India.strftime('%m-%d')
        f = open("static/check.txt","r")
        date = f.read()
        if date == strtime:
            f.close()
            return False
        else:
            return True
    def tick(self):
        f = open("static/check.txt","w")
        datetime_in_India = datetime.now(pytz.timezone('Asia/Kolkata'))
        strtime = datetime_in_India.strftime('%m-%d')
        f.write(strtime)



if __name__=="__main__":
    #os.system("cls")
    a = birthdaySender()
    b = databaseHandler()
    data = b.completedata()
    print(data)
    a.msgsender(data)
    #a.send_messages("s.i.d385","Happy Birthday Bro tum jiyo hazaro saal")
    #a.checkdate("2006-01-04")



"""
shutil.rmtree("config")
# Creating bot variable.
bot = Bot()

# Login using bot.
bot.login(username=USERNAME,
        password=PASSWORD)

# Make a list of followers/friends
urer_ids = ["s.i.d385"]

# Message
text = "Happy Birthday Siddhant"

# Sending messages
bot.send_messages(text, urer_ids)
"""

