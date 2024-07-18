from django.shortcuts import render
from .models import Form
from django.contrib import messages
from django.core.mail import EmailMessage

# Create your views here.

def index(request):
    if(request.method=='POST'):
        # form = Form(request.POST)
        # if form.is_valid():
        #     form.save()
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        date=request.POST.get('date')
        occupation=request.POST.get('occupation')
        form=Form(first_name=first_name,last_name=last_name,email=email,date=date,occupation
                  =occupation)
        form.save()

        message_body=f"""
                    Thank you for your form submittion:
                    Please Verify your Details
                    First Name     :{first_name}
                    Last Name      :{last_name}
                    Email_Provided :{email}
                    Submitted At   :{date}
                    Occupation     :{occupation}
                    """
        
        email_message=EmailMessage(subject="Your New Form Submission",
                        body=message_body,
                        to=[email]
                        )
        email_message.send()

        messages.success(request,f"{first_name} ,Form Submitted Successfully")

    return render(request,"index.html")

def about(request):
    return render(request,"about.html")