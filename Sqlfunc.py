import sqlite3
from sqlite3 import IntegrityError
#sqlconn=sqlite3.connect(DATABASE)
#cursor = sqlconn.cursor()


'''
command ="""CREATE TABLE "INSTAGRAM" ( 'userid' VARCHAR(20) NOT NULL ,
                      'password' VARCHAR(50) NOT NULL ,  
                      PRIMARY KEY ('userid'));"""
#cursor.execute(command)

command ="""CREATE TABLE "TELEGRAM" ( 'USER' VARCHAR(20) ,
                      'TOKEN' VARCHAR(50));"""
cursor.execute(command)

command ="""CREATE TABLE "CREDENTIALS" ( 'USER' VARCHAR(20) NOT NULL ,
                      'PASSWORD' VARCHAR(50) NOT NULL ,  
                      PRIMARY KEY ('USER'));"""
cursor.execute(command)
sqlconn.close()
'''



class databaseHandler:
    DATABASE_NAME = "bIRTHDAY.DB"
    DATABSE_PATH = "static/database/"
    DATABASE = DATABSE_PATH+DATABASE_NAME

    def insert(self,username,name,DOB,message):
        try:
            connection = sqlite3.connect(self.DATABASE)
            query = f'INSERT INTO Birthday VALUES("{username}","{name}" ,"{DOB}","{message}");'
            connection.execute(query)
            connection.commit()
            connection.close()
            return [200, "DONE"]
        except IntegrityError:
            return [404, "NOT_UNIQUE"]
        except Exception as e:
            print(e)


    def update(self,username,name,DOB,message):
        try:
            connection = sqlite3.connect(self.DATABASE)
            query = f'UPDATE "Birthday" SET name = "{name}", DOB = "{DOB}", message = "{message}" WHERE username = "{username}";'
            connection.execute(query)
            connection.commit()
            connection.close()
            return [200,"DONE"]
        except Exception as e:
            print(e)

    def delete(self,username):
        try:
            connection = sqlite3.connect(self.DATABASE)
            query = f'DELETE FROM "Birthday" WHERE username = "{username}";'
            connection.execute(query)
            connection.commit()
            connection.close()
            return [200, "DONE"]
        except Exception as e:
            print(e)
    def completedata(self):
        try:
            connection = sqlite3.connect(self.DATABASE)
            query = "select * from Birthday"
            data = connection.execute(query)
            datalist = []
            for row in data:
                datalist.append(row)
            connection.close()
            return datalist
            
        except Exception as e:
            print(e)
    def onequery(self,username):
        try:
            connection = sqlite3.connect(self.DATABASE)
            query = f"select * from Birthday WHERE username = '{username}'"
            data = connection.execute(query)
            datalist = []
            for row in data:
                datalist.append(row)
            connection.close()
            return datalist
        except Exception as e:
            print(e)



class credHandler:
    DATABASE_NAME = "credentials.DB"
    DATABSE_PATH = "static/database/"
    DATABASE = DATABSE_PATH+DATABASE_NAME
        #self.cursor = self.connection.cursor()
    def insertinstagram(self,userid,password):
        """to be used only once to fill the creds"""
        try:
            connection = sqlite3.connect(self.DATABASE)
            query = f'INSERT INTO INSTAGRAM VALUES("{userid}","{password}");'
            connection.execute(query)
            connection.commit()
            connection.close()
            return [200, "DONE"]
        except IntegrityError:
            return [404, "NOT_UNIQUE"]
        except Exception as e:
            print(e)
    def deleteinstagram(self,userid):
        try:
            connection = sqlite3.connect(self.DATABASE)
            query = f'DELETE FROM "INSTAGRAM" WHERE userid = "{userid}";'
            connection.execute(query)
            connection.commit()
            connection.close()
            return [200, "DONE"]
        except Exception as e:
            print(e)

    def inserttelegram(self,user,token):
        """to be used only once to fill the creds"""
        try:
            connection = sqlite3.connect(self.DATABASE)
            query = f'INSERT INTO TELEGRAM VALUES("{user}","{token}");'
            connection.execute(query)
            connection.commit()
            connection.close()
            return [200, "DONE"]
        except IntegrityError:
            return [404, "NOT_UNIQUE"]
        except Exception as e:
            print(e)

    def deletetelegram(self,user):
        try:
            connection = sqlite3.connect(self.DATABASE)
            query = f'DELETE FROM "TELEGRAM" WHERE user = "{user}";'
            connection.execute(query)
            connection.commit()
            connection.close()
            return [200, "DONE"]
        except Exception as e:
            print(e)

    def insertcreds(self,user,password):
        """to be used only once to fill the creds"""
        try:
            connection = sqlite3.connect(self.DATABASE)
            query = f'INSERT INTO CREDENTIALS VALUES("{user}","{password}");'
            connection.execute(query)
            connection.commit()
            connection.close()
            return [200, "DONE"]
        except IntegrityError:
            return [404, "NOT_UNIQUE"]
        except Exception as e:
            print(e)
    def deletecreds(self,user):
        try:
            connection = sqlite3.connect(self.DATABASE)
            query = f'DELETE FROM "CREDENTIALS" WHERE user = "{user}";'
            connection.execute(query)
            connection.commit()
            connection.close()
            return [200, "DONE"]
        except Exception as e:
            print(e)
    def completedata(self,tableName):
        try:
            connection = sqlite3.connect(self.DATABASE)
            query = f"select * from {tableName}"
            data = connection.execute(query)
            datalist = []
            for row in data:
                datalist.append(row)
            connection.close()
            return datalist
            
        except Exception as e:
            print(e)

if __name__ == '__main__':
    p = credHandler()
    p.insertcreds("Siddhant","siddhant1234")
    #p.insertinstagram("s.i.d385","akjfviojlkdsa")
    #p.inserttelegram("mobileno","alkdfkjdlkfjaf")
    #print(p.completedata("INSTAGRAM"))
    print(p.completedata("CREDENTIALS"))
    print("Hellow wrold")
    #basedata = databaseHandler(DATABASE)
    #basedata.insert("pushz","Pushpraj Patel","09/11/2005","Happy Birthday Pushpraj")
    #print(basedata.onequery("s.i.d385"))




