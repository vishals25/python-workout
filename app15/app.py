from email import message
from flask import Flask,render_template,request,flash
from flask_mail import Mail,Message
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os


app=Flask(__name__)

app.config["SECRET_KEY"]="myapplication1234"
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///data.db"
app.config["MAIL_SERVER"]="smtp.gmail.com"
app.config["MAIL_PORT"]=465
app.config["MAIL_USE_SSL"]=True
app.config["MAIL_USERNAME"]="svs15324@gmail.com"
app.config["MAIL_PASSWORD"]=os.getenv("password1")

db=SQLAlchemy(app)

mail=Mail(app)

class Form(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    firstname=db.Column(db.String(40),nullable=False)
    lastname=db.Column(db.String(40),nullable=False)
    email=db.Column(db.String(40),nullable=False)
    date=db.Column(db.Date)
    occupation=db.Column(db.String(30),nullable=False)



@app.route("/",methods=["GET","POST"])
def index():
    if request.method =="POST":
        first_name=request.form["first_name"]
        last_name=request.form["last_name"]
        email=request.form["email"]
        date=request.form["date"]
        date=datetime.strptime(date,"%Y-%m-%d")
        occupation=request.form["occupation"]
        
        form=Form(firstname=first_name,lastname=last_name,email=email,date=date,occupation=occupation) # type: ignore
        db.session.add(form)
        db.session.commit()

        message_body=f"Thank you for your form submittion:\n Please Verify your Details\
                    \n First Name    :{first_name}\n Last Name      :{last_name} \
                    \n Email Provided:{email}\n Submitted At:{date}\n Occupation:{occupation}"

        message=Message(subject="Your New Form Submission",
                        sender=app.config["MAIL_USERNAME"],
                        recipients=[email],
                        body=message_body
                        )
        mail.send(message)

        flash(f"{first_name},Your Form was submitted Successfully","success")



    return render_template("index.html")

if __name__=="__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True,port=5001)