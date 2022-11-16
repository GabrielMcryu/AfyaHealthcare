from django.core.mail import EmailMessage
from django.conf import settings

def sendEmail(user_email, email_header, doctor_data, symptoms, date):
    email = user_email
    print(user_email)
    first_name = doctor_data['first_name']
    last_name = doctor_data['last_name']
    specialization = doctor_data['specialization']
    email = EmailMessage(
        f'{email_header}',
        f'Appointment Information \n\n Doctor Name: {first_name} {last_name} \n Specialization: {specialization} \n Appointment Date: {date} \n Symptoms:\n {symptoms}',
        settings.EMAIL_HOST_USER,
        ['gasaji8612@sopulit.com']
    )

    email.fail_silently = True
    email.send()