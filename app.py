from flask import Flask, render_template,request,url_for,redirect,session
from Sqlfunc import databaseHandler,credHandler
from secure import encrypt,decrypt
from birthday import birthdaySender
app = Flask(__name__)
app.secret_key = "secret key"

#cdat is databaseHandler
#pdat is credentialsHandler

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        pdat = credHandler()
        data = pdat.completedata("CREDENTIALS")
        databaseuser = data[0][0]
        databasepassword = data[0][1]
        query = request.form
        username = query['Username']
        password = query['Password']
        if databaseuser == username and databasepassword == password:
            session.permanent = True
            session["username"] = username
            cdat = databaseHandler()
            data = cdat.completedata()
            return render_template("home.html",rows=data)
            #return render_template('index.html',len = len(IDS),IDS = IDS,enumerate=enumerate)
        else:
            return render_template("login.html")
    else:
        if "username" in session:
            cdat = databaseHandler()
            data = cdat.completedata()
            return render_template("home.html",rows=data)
        return render_template("login.html")
    

@app.route("/delete/<user>")
def delete(user):
    cdat = databaseHandler()
    cdat.delete(user)
    return redirect("/")

@app.route("/modify/<user>",methods=["POST", "GET"])
def modify(user):
    if request.method == "POST":
        query = request.form
        name = query['NAME']
        dob = query['DOB']
        message = query['MESSAGE']
        cdat = databaseHandler()
        cdat.update(user,name,dob,message)
        return redirect("/")
    else:
        cdat = databaseHandler()
        data = cdat.onequery(user)
        name = data[0][1]
        dob = data[0][2]
        msg = data[0][3]
        return render_template("modify.html",name=name)

@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        query = request.form
        user = query['USER']
        name = query['NAME']
        dob = query['DOB']
        message = query['MESSAGE']
        cdat = databaseHandler()
        cdat.insert(user,name,dob,message)
        return redirect("/")
    else:
        return render_template("add.html")
@app.route("/admin", methods=["POST", "GET"])
def admin():
    if request.method == "POST":
        query = request.form
        user = query['USER']
        name = query['NAME']
        dob = query['DOB']
        message = query['MESSAGE']
        cdat = databaseHandler()
        cdat.insert(user,name,dob,message)
        return redirect("/")
    else:
        pdat = credHandler()
        instadata = pdat.completedata("INSTAGRAM")
        teledata = pdat.completedata("TELEGRAM")
        credata = pdat.completedata("CREDENTIALS")
        return render_template("admin.html",instauser=instadata[0][0],instapassword=instadata[0][1],telgramuser=teledata[0][0],token=teledata[0][1],credsuser=credata[0][0],credspassword=credata[0][1])

@app.route("/change/<user>",methods=["POST", "GET"])
def change(user):
    if request.method == "POST":
        if user == "instagram":
            query = request.form
            userid = query['userid']
            password = query['password']
            pdat = credHandler()
            data = pdat.completedata("INSTAGRAM")[0][0]
            
            pdat.deleteinstagram(data)
            pdat.insertinstagram(userid,encrypt(password).decode())
            return redirect("/admin")
        elif user == "telegram":
            query = request.form
            mobileno = query['telgramuser']
            token = query['token']
            pdat = credHandler()
            data = pdat.completedata("TELEGRAM")[0][0]
            
            pdat.deletetelegram(data)
            pdat.inserttelegram(mobileno,encrypt(token).decode())
            return redirect("/admin")
        elif user == "creds":
            query = request.form
            user = query['creduser']
            password = query['credpassword']
            pdat = credHandler()
            data = pdat.completedata("CREDENTIALS")[0][0]
            
            pdat.deletecreds(data)
            pdat.insertcreds(user,password)
            return redirect("/admin")
    elif user == "instagram":
        pdat = credHandler()
        instadata = pdat.completedata("INSTAGRAM")
        userid = instadata[0][0]
        return render_template("instamod.html",userid=userid)
    elif user == "telegram":
        pdat = credHandler()
        instadata = pdat.completedata("TELEGRAM")
        userid = instadata[0][0]
        return render_template("telemod.html",userid=userid)
    elif user == "creds":
        pdat = credHandler()
        instadata = pdat.completedata("CREDENTIALS")
        userid = instadata[0][0]
        return render_template("CREDSMOD.html",userid=userid)
        
    else:
        cdat = databaseHandler()
        data = cdat.onequery(user)
        name = data[0][1]
        dob = data[0][2]
        msg = data[0][3]
        return render_template("modify.html",name=name)


@app.route("/msgsender")
def msgsender():
    a = birthdaySender()
    b = databaseHandler()
    data = b.completedata()
    a.msgsender(data)
    return "<p>True</p>"

@app.route("/logout")
def logout():
    session.pop("username", None)
    return render_template("login.html")


    

if __name__ == "__main__":
    app.run(debug=True)